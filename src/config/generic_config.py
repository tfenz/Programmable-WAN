""" contains generic test setup classes """
import itertools


class GenericTestSetup:
    def __init__(self):
        # reconfig parameters
        self.WAVELENGTH_EDGE_VALUES = [100]
        self.NODE_LIMITER_VALUES = [2]
        self.CAPACITY_WAVELENGTH_VALUES = [100]

        # topology specific
        self.TOPOLOGY_PROVIDER = None
        self.TOPOLOGY_FILE = None

        # traffic matrix
        self.TRAFFIC_MATRIX_PROVIDER = None
        self.TM_TOTAL_SAMPLES = 1
        self.TRAFFIC_MATRIX_FILES = [-1]
        self.TM_MULTIPLIER_VALUES = [1]
        self.TM_FIXED_TOTAL_VALUES = [-1]

        # gravity-model specific
        self.GM_TYPE = ['2_random_var']  # ['1_random_var', '2_random_var']
        self.GM_DISTRIBUTION = ['exp']  # ['exp', 'gauss']
        self.GM_LOC = [0]  # if gauss => gm_loc must be gte GM_SCALE (negative demands are set to 0)
        self.GM_SEED = 42986

        # TP/TE combinations:
        self.ALGORITHM_COMBO = [
            # ( TE-algorithm, TP-strategy, TP-leftover-strategy)
            # ("shortest_path_throughput", "uniform_tp", None),
            # ("shortest_path_throughput", "ssp_oblivious_tp", "Basic"),

            ("lp_throughput_joint", "joint_tp", None),
            ("lp_throughput_te", "uniform_tp", None),
            ("lp_throughput_te", "ssp_oblivious_tp", "Basic"),
        ]

    def generate_parameter_sets(self):
        """
        returns the cross product of all parameters as a list of tuples,
            where each tuple is a set of parameters defining a single test
        """
        parameter_set = itertools.product(
            self.WAVELENGTH_EDGE_VALUES, self.NODE_LIMITER_VALUES, self.CAPACITY_WAVELENGTH_VALUES,
            range(self.TM_TOTAL_SAMPLES), self.TM_MULTIPLIER_VALUES, self.TM_FIXED_TOTAL_VALUES, self.GM_TYPE,
            self.GM_DISTRIBUTION, self.GM_LOC, self.ALGORITHM_COMBO)

        return list(parameter_set)


class GenericSndLib(GenericTestSetup):
    def __init__(self):
        super().__init__()

        # topology parameter
        self.TOPOLOGY_PROVIDER = 'snd_lib'

        # tm parameter
        self.TRAFFIC_MATRIX_PROVIDER = "snd_lib"
        self.TM_TOTAL_SAMPLES = 10


class GenericSndLibSynTraffic(GenericTestSetup):
    def __init__(self):
        super().__init__()

        # topology parameter
        self.TOPOLOGY_PROVIDER = 'snd_lib'

        # tm parameter
        self.TRAFFIC_MATRIX_PROVIDER = "gravity_model"
        self.TM_TOTAL_SAMPLES = 10
        self.GM_SEED = 66134533
        self.GM_TYPE = ["2_random_var"]
        self.GM_DISTRIBUTION = ["exp"]
        self.GM_LOC = [0]


class GenericTopologyZooSetup(GenericTestSetup):
    def __init__(self):
        super().__init__()

        # topology parameter
        self.TOPOLOGY_PROVIDER = 'topology_zoo'

        # tm parameter
        self.TRAFFIC_MATRIX_PROVIDER = "gravity_model"
        self.TM_TOTAL_SAMPLES = 10
        self.GM_SEED = 66134533
        self.GM_TYPE = ["2_random_var"]
        self.GM_DISTRIBUTION = ["exp"]
        self.GM_LOC = [0]
