from utility.algorithm_result import AlgorithmResult


class GenericTrafficEngineering:
    def solve(self, topology: dict, demand_matrix: dict, n_nodes: int, max_wavelengths_edge: int,
              wavelength_limiter: float, c_wavelength: float, log_file_name: str = "test.log",
              wl_map: dict = None) -> AlgorithmResult:
        """
        computes the traffic engineering
        :param topology: dict of tuples with: {(src_node, dst_node):info_dict}
        :param demand_matrix: dict with: {(src_node, dst_node): packet_length, ...}
        :param n_nodes: number of nodes in topology
        :param max_wavelengths_edge : defines how many wavelength a link can carry
        :param wavelength_limiter: limits the number of wavelength a node can process
        :param c_wavelength: defines the capacity of one wavelength
        :param log_file_name: full file name of log file
        :param wl_map: predefined wavelength assignment as dict with: {(i, j): #wavelengths, ...}
        :return: AlgorithmResult
        """
        raise Exception("Abstract Algorithm - use a concrete class")

    def get_name(self):
        """ returns name of algorithm """
        raise Exception("Abstract Algorithm - use a concrete class")
