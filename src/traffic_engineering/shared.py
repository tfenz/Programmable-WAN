"""
contains shared methods used in multiple algorithm
"""
import math
import operator
import os
import timeit

import gurobipy as gb

from utility.algorithm_result import AlgorithmResult
from utility import const


def create_lp_model(name, log_file_name):
    """creates a named Gurobi model for lps with some options"""
    gp_model = gb.Model(name)
    gp_model.setParam('LogToConsole', const.OUTPUT_FLAG)
    gp_model.setParam('TimeLimit', const.TIME_LIMIT)
    gp_model.setParam('threads', const.MAX_THREADS)
    gp_model.setParam('NonConvex', const.NON_CONVEX)
    gp_model.setParam('LogFile', os.path.abspath(log_file_name))
    return gp_model


def get_degree_of(links: list, node_i: int) -> int:
    """
     computes the degree of each node and maps the node id to its degree
    :param links: a list of tuples with [(src, dst), ...]
    :param node_i: index i of node
    :return: degree of node i
    """
    deg_i = sum(1 if node_i == i else 0 for i, _ in links)
    return deg_i


def get_node_degree_dict(links: list, n_nodes: int) -> dict:
    """
     maps the node id to its degree
    :param links: a list of tuples with [(src, dst), ...]
    :param n_nodes: number of nodes in the topology
    :return: dict with key: (node_index) and value: degree
    """
    node_deg_dict = {i: get_degree_of(links, i) for i in range(n_nodes)}
    return node_deg_dict


def get_sorted_accumulated_demand_sequence(demand_matrix: dict) -> list:
    """
    converts the matrix into a demand sequence ordered by its demand size
    :param demand_matrix: dict with {(src, dst) :  demand_size}
    :return:
    """
    acc_demands = [(i, j, demand_matrix[(i, j)]) for (i, j) in demand_matrix]
    acc_demands.sort(key=operator.itemgetter(2), reverse=True)
    return acc_demands


def accumulate_demand_sequence(demand_sequence: list) -> dict:
    """
    :param demand_sequence: a list of tuples with [(src, dst, demand_size)]
    :return demand_matrix: accumulated demand matrix with {(src, dst) :  demand_size}
    """
    demand_matrix = dict()
    for src, dst, demand_size in demand_sequence:
        if (src, dst) not in demand_matrix:
            demand_matrix[(src, dst)] = 0

        demand_matrix[(src, dst)] += demand_size
    return demand_matrix


def prepare_input(demand_matrix, max_wavelengths_edge, n_nodes, topology, wavelength_limiter):
    """creates Gurobi data structures from input variables for all non-baseline LPs"""
    links = gb.tuplelist(topology.keys())
    demand_matrix = gb.tupledict(demand_matrix)
    connection_pairs = gb.tuplelist(demand_matrix.keys())
    node_degree_dict = gb.tupledict(get_node_degree_dict(links, n_nodes))
    max_wavelengths_node = gb.tupledict(
        {i: deg * int(max_wavelengths_edge / wavelength_limiter) for i, deg in node_degree_dict.items()})
    return links, demand_matrix, connection_pairs, node_degree_dict, max_wavelengths_node


def prepare_input_baseline(c_wavelength, demand_matrix, max_wavelengths_edge, topology, wavelength_limiter):
    """creates Gurobi data structures from input variables for all baseline LPs"""
    links = gb.tuplelist(topology.keys())
    demand_matrix = gb.tupledict(demand_matrix)
    connection_pairs = gb.tuplelist(demand_matrix.keys())
    const_wavelengths_edge = int(max_wavelengths_edge / wavelength_limiter)
    const_edge_capacity = c_wavelength * const_wavelengths_edge
    return connection_pairs, const_edge_capacity, demand_matrix, links, const_wavelengths_edge


def optimize(gp_model):
    """starts lp computation with time measurement"""
    start_time = timeit.default_timer()
    gp_model.optimize()
    objective = gp_model.objVal
    exe_time = timeit.default_timer() - start_time
    return exe_time, objective


def create_lp_util_map(
        c_wavelength, connection_pairs, demand_matrix, gb_links, gb_wavelengths_edge_map, gb_paths, gb_flows):
    """ extracts the utilization map from gurobi vars """
    util_map = dict()
    for i, j in gb_links:

        n_wavelengths = math.ceil(gb_wavelengths_edge_map[i, j].X)
        cap = n_wavelengths * c_wavelength

        flow_sum_edge = 0
        for start, end in connection_pairs:
            flow_sum_edge += gb_paths[start, end, i, j].X * gb_flows[start, end].X * demand_matrix[start, end]

        if cap > 0:
            util = flow_sum_edge / cap
        else:
            util = 0

        util_map[i, j] = util
    return util_map


def create_lp_flow_paths(gb_paths: gb.tupledict):
    """ extracts the flow paths from gurobi vars"""
    flow_map = {(source, sink, i, j): gb_paths[source, sink, i, j].X for source, sink, i, j in gb_paths}
    return flow_map


def create_result_lp(c_wavelength, connection_pairs, demand_matrix, exe_time, flow_paths, flows, links,
                     gb_wavelengths_edge_map, objective) -> AlgorithmResult:
    """ creates AlgorithmResult for ILP/LP TE algorithms"""
    result = AlgorithmResult()
    result.objective = objective
    result.execution_time = exe_time
    result.utilization_map = create_lp_util_map(
        c_wavelength, connection_pairs, demand_matrix, links, gb_wavelengths_edge_map, flow_paths, flows)
    result.flow_paths = create_lp_flow_paths(flow_paths)
    result.wavelength_assignment = {(i, j): int(gb_wavelengths_edge_map[i, j].X) for i, j in gb_wavelengths_edge_map}
    result.success = True
    return result


def get_utilization_map(flow_paths, flows, wavelength_assignment, cp):
    """ extracts the utilization map (used by heuristic TE algorithms) """
    flow_map = dict()
    utilization = dict()
    link_flow_sums = dict()
    for s, t in flow_paths:
        if len(flow_paths[s, t]) == 0:
            continue
        for idx in range(len(flow_paths[s, t]) - 1):
            i = flow_paths[s, t][idx]
            j = flow_paths[s, t][idx + 1]
            flow_map[s, t, i, j] = flows[s, t]
            if (i, j) not in link_flow_sums:
                link_flow_sums[i, j] = 0
            link_flow_sums[i, j] += flows[s, t]
    for i, j in link_flow_sums:
        if wavelength_assignment[i, j] == 0:
            continue
        utilization[i, j] = link_flow_sums[i, j] / (wavelength_assignment[i, j] * cp)
    return utilization, flow_map


def create_heuristics_result(exe_time, flow_paths, flows, objective,
                             wavelength_assignment, cp) -> AlgorithmResult:
    """ extracts the utilization for heuristic TE algorithms """
    result = AlgorithmResult()
    link_utilization = dict()
    flow_map = dict()
    if len(flows) > 0:
        link_utilization, flow_map = get_utilization_map(flow_paths, flows, wavelength_assignment, cp)
    result.wavelength_assignment = wavelength_assignment
    result.objective = objective
    result.execution_time = exe_time
    result.flow_paths = flow_map
    result.utilization_map = link_utilization
    result.success = True
    return result
