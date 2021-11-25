import time
import timeit

import networkx as nx

from traffic_engineering import shared
from traffic_engineering.generic_traffic_engineering import GenericTrafficEngineering
from utility.algorithm_result import AlgorithmResult


class ShortestPathThroughputTe(GenericTrafficEngineering):
    def __get_route_final_route(self, nx_graph, s, t, d):
        flow_throughput = d

        if not nx.has_path(nx_graph, s, t):
            return 0, []
        final_path = nx.shortest_path(nx_graph, s, t, weight='weight')

        # compute max flow
        for idx, current in enumerate(final_path[:-1]):
            successor = final_path[idx + 1]
            flow_throughput = min(flow_throughput, nx_graph[current][successor]['capacity'])

        # update capacity
        for idx, current in enumerate(final_path[:-1]):
            successor = final_path[idx + 1]
            nx_graph[current][successor]['capacity'] -= flow_throughput
            if nx_graph[current][successor]['capacity'] <= 0:
                nx_graph.remove_edge(current, successor)
        return flow_throughput, final_path,

    @staticmethod
    def __get_nx_graph(links: list, cp, wl_map) -> nx.DiGraph:
        nx_graph = nx.DiGraph(links)
        nx.set_edge_attributes(nx_graph, 1, "weight")
        nx.set_edge_attributes(nx_graph, 0, "capacity")
        for (i, j) in list(nx_graph.edges):
            nx_graph[i][j]["capacity"] = wl_map[i, j] * cp
        return nx_graph

    def solve(self, topology: dict, demand_matrix: dict, n_nodes: int, max_wavelengths_edge: int,
              wavelength_limiter: float, c_wavelength: float, log_file_name: str = "test.log",
              wl_map: dict = None) -> AlgorithmResult:
        """ see generic_traffic_engineering.py """
        # 1 Prepare
        nx_graph = self.__get_nx_graph(list(topology.keys()), c_wavelength, wl_map)

        start_time = timeit.default_timer()

        # 2 Sort Demands
        objective = 0
        flow_paths = dict()
        flows = dict()

        shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(nx_graph))
        sorted_demands = [(i, j, demand_matrix[i, j]) for (i, j) in
                          sorted(demand_matrix.keys(), key=lambda k: shortest_path_lengths[k[0]][k[1]])]

        for s, t, d in sorted_demands:
            flow, path = self.__get_route_final_route(nx_graph, s, t, d)
            flow_paths[s, t] = path
            flows[s, t] = flow / d
            objective += flow

        exe_time = timeit.default_timer() - start_time

        # create db_result
        result = shared.create_heuristics_result(exe_time, flow_paths, flows, objective, wl_map,
                                                 c_wavelength)
        return result

    def get_name(self):
        """ see generic_traffic_engineering.py """
        return f"shortest_path_throughput_te"
