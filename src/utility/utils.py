import csv
import logging
import os


def create_out_dirs(out_dir, log_dir):
    """ make dirs """
    try:
        log_dir = os.path.abspath(log_dir)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        out_dir = os.path.abspath(out_dir)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        log_dir = os.path.abspath(log_dir)
    except Exception as ex:
        print(f"Fatal Error: create_out_dirs(...) throws: {str(ex)} ")
        raise ex
    return out_dir, log_dir


def store_test_result(file_name, **kwargs):
    """add row to result csv file"""
    try:
        if not os.path.exists(file_name):
            # write header when file is created;
            with open(file_name, 'w', newline='') as csvfile:
                logging.info("result.csv created")
                writer = csv.DictWriter(csvfile, fieldnames=kwargs.keys())
                writer.writeheader()

        with open(file_name, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=kwargs.keys())
            writer.writerow(dict(kwargs))
    except Exception as ex:
        logging.error(ex)
        exit(-1)


def init_logging(log, debug, config):
    f_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_lvl = logging.DEBUG if debug else logging.WARNING
    log_file = os.path.join(log, f'main_{config}.log')
    logging.basicConfig(filename=log_file, filemode='a+', level=log_lvl, format=f_format)
