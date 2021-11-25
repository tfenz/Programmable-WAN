import gurobipy as gp

from traffic_engineering import shared
from traffic_engineering.generic_traffic_engineering import GenericTrafficEngineering
from utility.algorithm_result import AlgorithmResult


class LpThroughputJoint(GenericTrafficEngineering):
    def solve(self, topology: dict, demand_matrix: dict, n_nodes: int, max_wavelengths_edge: int,
              wavelength_limiter: float, c_wavelength: float, log_file_name: str = "test.log",
              wl_map: dict = None) -> AlgorithmResult:
        """ see generic_traffic_engineering.py """

        # region ILP Preparation
        links, demand_matrix, connection_pairs, node_degree_dict, max_wavelengths_node = shared.prepare_input(
            demand_matrix, max_wavelengths_edge, n_nodes, topology, wavelength_limiter)
        # endregion

        # region ILP Model creation
        gp_model = shared.create_lp_model(self.get_name(), log_file_name)
        # endregion

        # region decision var
        flows = gp_model.addVars(connection_pairs, lb=0.0, ub=1.0, vtype=gp.GRB.CONTINUOUS)  # := f
        flow_paths = gp_model.addVars(connection_pairs, links, lb=0.0, ub=1.0, vtype=gp.GRB.CONTINUOUS)  # := x
        n_wavelengths_edge = gp_model.addVars(links, lb=0.0, ub=max_wavelengths_edge, vtype=gp.GRB.CONTINUOUS)  # := c
        # endregion

        # region objective
        # I: objective is to maximize throughput
        obj = gp.quicksum(demand_matrix[start, end] * flows[start, end] for start, end in demand_matrix.keys())
        gp_model.setObjective(obj, gp.GRB.MAXIMIZE)
        # endregion

        # region constraints
        # II: the sum of wavelengths assigned to adjacent links must not exceed node wavelength maximum
        gp_model.addConstrs(
            gp.quicksum(n_wavelengths_edge[i, j] for i in range(n_nodes) if (i, j) in n_wavelengths_edge) <=
            max_wavelengths_node[j] for j in range(n_nodes))

        # III-a: Flow conservation (a: if demand source) (relaxed)
        gp_model.addConstrs(
            flow_paths.sum(start, end, start, '*') - flow_paths.sum(start, end, '*', start) == flows[start, end] for
            start, end, in demand_matrix.keys())

        # III-b: Flow conservation (b: if demand sink) (relaxed)
        gp_model.addConstrs(
            flow_paths.sum(start, end, end, '*') - flow_paths.sum(start, end, '*', end) == -flows[start, end] for
            start, end, in demand_matrix.keys())

        # III-c: Flow conservation (c: else) (relaxed)
        gp_model.addConstrs(flow_paths.sum(start, end, i, '*') - flow_paths.sum(start, end, '*', i) == 0
                            for start, end, i, _ in flow_paths.keys() if i != start and i != end)

        # IV: sum of flows at edge must not exceed its capacity (relaxed)
        gp_model.addConstrs(
            gp.quicksum(flow_paths[start, end, i, j] * demand_matrix[start, end] for start, end in connection_pairs)
            <= n_wavelengths_edge[i, j] * c_wavelength for i, j in links)

        # V: wavelength assignment is undirected: w[i, j] == w[j, i]
        gp_model.addConstrs((n_wavelengths_edge[i, j] == n_wavelengths_edge[j, i] for i, j in links))

        # VI: no edge can carry more wavelengths than max-wavelengths-constant
        gp_model.addConstrs(n_wavelengths_edge[i, j] <= max_wavelengths_edge for i, j in links)
        # endregion

        # start computation
        exe_time, objective = shared.optimize(gp_model)

        result = shared.create_result_lp(c_wavelength, connection_pairs, demand_matrix, exe_time, flow_paths, flows,
                                         links, n_wavelengths_edge, objective)

        return result

    def get_name(self):
        """ see generic_traffic_engineering.py """
        return "lp_throughput_joint"
