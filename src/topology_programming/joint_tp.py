from topology_programming.generic_topology_programming import GenericTopologyProgramming


class JointTP(GenericTopologyProgramming):
    def get_assignment(self, topology: dict, max_wavelengths_edge: int, wavelength_limiter: float,
                       demand_matrix: dict = None, distribute_leftover: str = None) -> dict:
        """see generic_topology_programming.py"""
        wl_assignment = dict()
        return wl_assignment

    def get_name(self):
        """see generic_topology_programming.py"""
        return f"joint_tp"
