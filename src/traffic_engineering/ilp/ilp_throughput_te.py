import gurobipy as gp

from traffic_engineering import shared
from traffic_engineering.generic_traffic_engineering import GenericTrafficEngineering
from utility.algorithm_result import AlgorithmResult


class IlpThroughputTe(GenericTrafficEngineering):
    def solve(self, topology: dict, demand_matrix: dict, n_nodes: int, max_wavelengths_edge: int,
              wavelength_limiter: float, c_wavelength: float, log_file_name: str = "test.log",
              wl_map: dict = None) -> AlgorithmResult:
        """ see generic_traffic_engineering.py """

        connection_pairs, const_edge_capacity, demand_matrix, links, const_wavelengths_edge = shared.prepare_input_baseline(
            c_wavelength, demand_matrix, max_wavelengths_edge, topology, wavelength_limiter)
        gp_model = shared.create_lp_model(self.get_name(), log_file_name)

        flows = gp_model.addVars(connection_pairs, lb=0.0, ub=1.0, vtype=gp.GRB.CONTINUOUS)  # := f
        paths = gp_model.addVars(connection_pairs, links, vtype=gp.GRB.BINARY)  # := x
        flow_paths = gp_model.addVars(connection_pairs, links, lb=0.0, ub=1.0,
                                      vtype=gp.GRB.CONTINUOUS)  # := var flow_paths to substitute flow * path
        n_wavelengths_edge = gp_model.addVars(links, lb=0, ub=max(wl_map.values()),
                                              vtype=gp.GRB.CONTINUOUS)  # := wl (const in baseline)

        # I: objective is to maximize throughput
        obj = gp.quicksum(demand_matrix[start, end] * flows[start, end] for start, end in demand_matrix.keys())
        gp_model.setObjective(obj, gp.GRB.MAXIMIZE)

        # XXX: only to store correct wl in result
        gp_model.addConstrs(n_wavelengths_edge[i, j] == wl_map[(i, j)] for i, j in n_wavelengths_edge)

        # II-a: Flow conservation (a: if demand source)
        gp_model.addConstrs(
            (paths.sum(start, end, start, '*') - paths.sum(start, end, '*', start) == 1 for start, end, in
             demand_matrix.keys())
        )

        # II-b: Flow conservation (b: if demand sink)
        gp_model.addConstrs(
            (paths.sum(start, end, end, '*') - paths.sum(start, end, '*', end) == -1 for start, end, in
             connection_pairs)
        )

        # II-c: Flow conservation (c: else)
        gp_model.addConstrs(
            (paths.sum(start, end, i, '*') - paths.sum(start, end, '*', i) == 0
             for start, end, i, _ in paths.keys() if i != start and i != end)
        )

        # substitute: flow*paths (https://orinanobworld.blogspot.com/2010/10/binary-variables-and-quadratic-terms.html)
        # sub-I
        gp_model.addConstrs(
            flow_paths[start, end, i, j] <= paths[start, end, i, j] for start, end, i, j in paths.keys())

        # sub-II
        gp_model.addConstrs(flow_paths[start, end, i, j] <= flows[start, end] for start, end, i, j in paths.keys())

        # sub-III
        gp_model.addConstrs(flow_paths[start, end, i, j] >= flows[start, end] - (1 - paths[start, end, i, j]) for
                            start, end, i, j in paths.keys())

        # III: sum of flows at edge must not exceed its capacity
        gp_model.addConstrs(
            gp.quicksum(flow_paths[start, end, i, j] * demand_matrix[start, end] for start, end in connection_pairs)
            <= wl_map[(i, j)] * c_wavelength for i, j in links)

        # start computation
        exe_time, objective = shared.optimize(gp_model)

        result = shared.create_result_lp(c_wavelength, connection_pairs, demand_matrix, exe_time, flow_paths, flows,
                                         links, n_wavelengths_edge, objective)
        return result

    def get_name(self):
        """ see generic_traffic_engineering.py """
        return "ilp_throughput_te"
