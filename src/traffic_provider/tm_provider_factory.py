from traffic_provider.generic_tm_provider import GenericTM
from traffic_provider.gravity_model.gravity_model_traffic_provider import GravityModel
from traffic_provider.snd_lib.sndlib_traffic_provider import SndLibTM


def get_traffic_matrix_factory(
        tm_name: str, node_info: dict, tm_sample_nr: int, gm_type: str = "2_random_var", gm_seed: float = 0,
        tm_files: list = None, dm: float = 1, gm_distribution: str = "exp", gm_loc: float = 0,
        tm_fixed_total: float = None) -> GenericTM:
    """ returns the requested traffic matrix factory """
    tm_name = tm_name.lower()
    if tm_name == "snd_lib":
        if tm_sample_nr >= len(tm_files):
            raise Exception(f"list of traffic matrix files does't have enough entries "
                            f"for the defined number of samples (TM_TOTAL_SAMPLES)")
        return SndLibTM(tm_file=tm_files[tm_sample_nr], node_info=node_info, t_sample_nr=tm_sample_nr, dm=dm,
                        tm_fixed_total=tm_fixed_total)
    if tm_name == "gravity_model":
        return GravityModel(node_info=node_info, tm_sample_nr=tm_sample_nr, gm_scale=dm, gm_type=gm_type,
                            gm_distribution=gm_distribution, gm_loc=gm_loc, gm_seed=gm_seed,
                            tm_fixed_total=tm_fixed_total)
    raise Exception(f"traffic matrix factory not found: {tm_name}")
