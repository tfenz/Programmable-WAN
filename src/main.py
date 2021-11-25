"""
run all tests of the specified in the setup classes configured in config file. Run with:

python main.py [-o <dir>] [-l <dir>] [-c <config>] [--debug]
    --debug:     to extend logging
    -o <dir>     path to out dir
    -l <dir>     path to log dir
    -c <config>  config file name (as in ./config/<config>.py)
"""

import argparse
import concurrent
import logging
import os
from concurrent.futures import ProcessPoolExecutor

from config import config_factory
from topology_programming import tp_factory
from topology_provider import topology_factory
from traffic_engineering import te_factory
from traffic_provider import tm_provider_factory
from utility import const, utils
from utility.ignored_topologies import ignored_tops

# default values if no parameters were passed
DEFAULT_OUT_DIR = os.path.abspath("../out")  # -o <dir>
DEFAULT_LOG_DIR = os.path.abspath("../log")  # -l <dir>
DEFAULT_CONFIG = "config_sndlib"  # -c <config> (as in ./config/<config>.py)


def single_test_worker(
        te_name, tp_name, leftover, dm, ca, wl, tm_sample_nr, setup, li, tm_fixed_total, out, log, config, debug):
    """
    performs a single test and appends the result to the out csv file
    :param te_name: name of traffic engineering algorithm
    :param tp_name: name of topology programming
    :param leftover: name of left over strategy (part of topology programming)
    :param dm: demand multiplier
    :param ca: capacity of a single wavelength
    :param wl: number of wavelengths a edge can carry at max
    :param tm_sample_nr: sample of traffic matrix
    :param setup: setup class name
    :param li: node limiter
    :param tm_fixed_total: the sum of all demanded flows get scaled to 'tm_fixed_total'
    :param out: out directory for result csv
    :param log: log file directory
    :param config: config name
    :param debug: debug mode
    :return: True if success else False
    """
    utils.init_logging(log, debug, config)
    logging.info(f'start with: te_name="{te_name}", tp_name="{tp_name}", leftover_strategy="{leftover}", '
                 f'dm="{dm}", ca="{ca}", wl="{wl}", tm_sample_nr="{tm_sample_nr}", setup="{setup}", li="{li}", '
                 f'tm_fixed_total="{tm_fixed_total}", out="{out}", log="{log}"')
    try:
        # get topology
        top_provider = topology_factory.get_topology_factory(
            setup.TOPOLOGY_PROVIDER, topology_file=setup.TOPOLOGY_FILE)

        if top_provider.get_name() in ignored_tops:
            f"{const.HIGHLIGHT}TOPOLOGY IGNORED {top_provider.get_name()}:  {const.CEND}"
            return True
        topology, nodes = top_provider.get_topology()
        n = len(nodes)

        # get traffic matrix
        gm_seed = tm_sample_nr + setup.GM_SEED
        tm_provider = tm_provider_factory.get_traffic_matrix_factory(
            setup.TRAFFIC_MATRIX_PROVIDER, nodes, tm_sample_nr=tm_sample_nr, gm_seed=gm_seed,
            tm_files=setup.TRAFFIC_MATRIX_FILES, dm=dm, tm_fixed_total=tm_fixed_total)
        traffic_matrix = tm_provider.get_traffic_matrix()
        total, n_entries, mean = tm_provider.get_basic_stats(traffic_matrix)

        tp_algo = tp_factory.get_tp_algorithm(tp_name)
        te_algo = te_factory.get_te_algorithm(te_name)
        log_file = os.path.join(log, f"{te_algo.get_name()}__tp_{tp_algo.get_name()}_gurobi.log")

        # compute topology programming
        try:
            wl_map = tp_algo.get_assignment(topology, wl, li, traffic_matrix, distribute_leftover=leftover)
        except Exception as ex:
            logging.error(str(ex))
            return False

        # compute traffic engineering
        try:
            res = te_algo.solve(topology, traffic_matrix, n, wl, li, ca, log_file, wl_map)
        except Exception as ex:
            logging.error(str(ex))
            return False

        # append result to csv file
        file_name = os.path.join(out, f"result_{config}.csv")
        utils.store_test_result(
            file_name=file_name, config=config, tm_provider=tm_provider.get_name(), tm_entries=n_entries,
            demand_multiplier=dm, total_demand=total, capacity_wavelength=ca, n_total=len(nodes), n_wavelengths_edge=wl,
            mean_demand=mean, tm_sample_nr=tm_sample_nr, gm_seed=gm_seed, topology_provider=top_provider.get_name(),
            wavelength_limiter=li, te_name=te_algo.get_name(), error_msg=res.err_msg, success=res.success,
            exe_time=res.execution_time, objective=res.objective, tp_name=tp_algo.get_name(),
            distribute_leftover=leftover)

    except Exception as ex:
        logging.error(str(ex))
        return False
    return True


def main(out, log, debug, config):
    """ starts each configured single tests in a process """
    out, log = utils.create_out_dirs(out, log)
    utils.init_logging(log, debug, config)

    # define number of workers
    executor = ProcessPoolExecutor(max_workers=8)

    # get setup objects from config file
    setup_names = config_factory.get_setup_list(config)

    # submit jobs
    future_map = dict()
    for setup_name in setup_names:
        print(f"Submit tests in setup {setup_name}")
        logging.info(f"Submit tests in {setup_name}")
        setup = config_factory.get_test_setup(config, setup_name)
        parameter_sets = setup.generate_parameter_sets()

        for i, (wl, li, ca, tm_sample_nr, dm, tm_fixed_total, _, _, _, (te, tp, leftover)) in enumerate(parameter_sets):
            print(f"SUBMIT: Test {i + 1}/{len(parameter_sets)}")
            logging.info(f"\tSUBMIT: Test {i + 1}/{len(parameter_sets)}")
            future = executor.submit(
                single_test_worker, te, tp, leftover, dm, ca, wl, tm_sample_nr, setup, li, tm_fixed_total, out, log,
                config, debug)
            future_map[future] = (setup_name, i, len(parameter_sets))

    # wait and print output
    for future in concurrent.futures.as_completed(future_map):
        setup_name, i, n_tests = future_map[future]
        success = False
        try:
            success = future.result()
        finally:
            print(f"Setup {setup_name}, Test {i + 1}/{n_tests} "
                  f"SUCCESS: {const.OK if success else const.FAIL}{success}{const.CEND}")
            logging.info(f"finished '{setup_name}', Test {i + 1}/{n_tests} with {'success' if success else 'error(s)'}")
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', action="store", type=str, default=DEFAULT_CONFIG,
                        help='config file name as in ["config_sndlib", "config_topology_zoo"]')
    parser.add_argument('-o', '--out', dest='out', action="store", type=str, default=DEFAULT_OUT_DIR,
                        help='define dir for result.csv')
    parser.add_argument('-l', '--log', dest='log', action="store", type=str, default=DEFAULT_LOG_DIR,
                        help='define log directory')
    parser.add_argument('--debug', action='store_true', help='start in debug mode: affects logging')

    args = parser.parse_args()
    print(f"--config \"{args.config}\"")
    print(f"--out \"{args.out}\"")
    print(f"--log \"{args.log}\"")
    print(f"--debug \"{args.debug}\"")

    main(args.out, args.log, args.debug, args.config)
