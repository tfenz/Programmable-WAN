import numpy as np


class GenericTM:
    def get_traffic_matrix(self) -> dict:
        """ creates and returns a traffic matrix as dict with {(s,t):demand} """
        raise Exception("Abstract traffic matrix factory - use a concrete class")

    def get_name(self) -> str:
        """ returns the name of the TrafficMatrix provider"""
        raise Exception("Abstract traffic matrix factory - use a concrete class")

    @staticmethod
    def get_basic_stats(demand_matrix: dict) -> (float, float, float):
        """
        :param demand_matrix: demand as matrix
        :return: sum of traffic, number of entries, mean
        """
        total_demand = np.sum(np.array(list(demand_matrix.values())))
        n_entries = len(demand_matrix.values())
        mean = np.mean(np.array(list(demand_matrix.values())))
        return total_demand, n_entries, mean
