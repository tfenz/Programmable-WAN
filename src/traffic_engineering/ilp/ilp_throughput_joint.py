import gurobipy as gp

from traffic_engineering import shared
from traffic_engineering.generic_traffic_engineering import GenericTrafficEngineering
from utility.algorithm_result import AlgorithmResult


class IlpThroughputJoint(GenericTrafficEngineering):
    def solve(self, topology: dict, demand_matrix: dict, n_nodes: int, max_wavelengths_edge: int,
              wavelength_limiter: float, c_wavelength: float, log_file_name: str = "test.log",
              wl_map: dict = None) -> AlgorithmResult:
        """ see generic_traffic_engineering.py """
        links = gp.tuplelist(topology.keys())
        demand_matrix = gp.tupledict(demand_matrix)
        connection_pairs = gp.tuplelist(demand_matrix.keys())
        node_degree_dict = gp.tupledict(shared.get_node_degree_dict(links, n_nodes))
        max_wavelengths_node = gp.tupledict(
            {i: deg * int(max_wavelengths_edge / wavelength_limiter) for i, deg in node_degree_dict.items()})

        gp_model = shared.create_lp_model(self.get_name(), log_file_name)

        flows = gp_model.addVars(connection_pairs, lb=0.0, ub=1.0, vtype=gp.GRB.CONTINUOUS)  # := f
        paths = gp_model.addVars(connection_pairs, links, vtype=gp.GRB.BINARY)  # := x
        n_wavelengths_edge = gp_model.addVars(links, lb=0.0, ub=max_wavelengths_edge, vtype=gp.GRB.INTEGER)  # := c
        flow_paths = gp_model.addVars(connection_pairs, links, ub=1.0, lb=0.0,
                                      vtype=gp.GRB.CONTINUOUS)  # := var flow_paths to substitute flow * path

        # I: objective is to maximize throughput
        obj = gp.quicksum(demand_matrix[start, end] * flows[start, end] for start, end in demand_matrix.keys())
        gp_model.setObjective(obj, gp.GRB.MAXIMIZE)

        # II: the sum of wavelengths assigned to adjacent links must not exceed node wavelength maximum
        gp_model.addConstrs(
            (gp.quicksum(n_wavelengths_edge[i, j] for i in range(n_nodes) if (i, j) in n_wavelengths_edge) <=
             max_wavelengths_node[j] for j in range(n_nodes))
        )

        # III-a: Flow conservation (a: if demand source)
        gp_model.addConstrs(
            (paths.sum(start, end, start, '*') - paths.sum(start, end, '*', start) == 1 for start, end, in
             demand_matrix.keys())
        )

        # III-b: Flow conservation (b: if demand sink)
        gp_model.addConstrs(
            (paths.sum(start, end, end, '*') - paths.sum(start, end, '*', end) == -1 for start, end, in
             connection_pairs)
        )

        # III-c: Flow conservation (c: else)
        gp_model.addConstrs(
            (paths.sum(start, end, i, '*') - paths.sum(start, end, '*', i) == 0
             for start, end, i, _ in paths.keys() if i != start and i != end)
        )

        # sub-I
        gp_model.addConstrs(
            flow_paths[start, end, i, j] <= paths[start, end, i, j] for start, end, i, j in paths.keys())

        # sub-II
        gp_model.addConstrs(flow_paths[start, end, i, j] <= flows[start, end] for start, end, i, j in paths.keys())

        # sub-III
        gp_model.addConstrs(flow_paths[start, end, i, j] >= flows[start, end] - (1 - paths[start, end, i, j]) for
                            start, end, i, j in paths.keys())

        # IV: sum of flows at edge must not exceed its capacity
        gp_model.addConstrs(
            gp.quicksum(flow_paths[start, end, i, j] * demand_matrix[start, end] for start, end in connection_pairs)
            <= n_wavelengths_edge[i, j] * c_wavelength for i, j in links)

        # V: wavelength assignment is undirected: w[i, j] == w[j, i]
        gp_model.addConstrs((n_wavelengths_edge[i, j] == n_wavelengths_edge[j, i] for i, j in links))

        # VI: no edge can carry more wavelengths than max-wavelengths-constant
        gp_model.addConstrs(n_wavelengths_edge[i, j] <= max_wavelengths_edge for i, j in links)

        # start computation
        exe_time, objective = shared.optimize(gp_model)

        result = shared.create_result_lp(c_wavelength, connection_pairs, demand_matrix, exe_time, flow_paths, flows,
                                         links, n_wavelengths_edge, objective)

        return result

    def get_name(self):
        """ see generic_traffic_engineering.py """
        return "ilp_throughput_joint"
