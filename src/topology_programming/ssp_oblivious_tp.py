import networkx as nx

from topology_programming.generic_topology_programming import GenericTopologyProgramming


# Note: get_assignment(..) defined in GenericTP
class SSPObliviousTP(GenericTopologyProgramming):
    def _set_edge_weights(self, nx_graph: nx.Graph, unused: dict):
        """see generic_topology_programming.py"""
        n = len(nx_graph.nodes)
        shortest_paths = dict(nx.all_pairs_dijkstra_path(nx_graph, weight="weight"))
        for s in range(n):
            for t in range(s + 1, n):
                for idx in range(len(shortest_paths[s][t]) - 1):
                    i = shortest_paths[s][t][idx]
                    j = shortest_paths[s][t][idx + 1]
                    nx_graph[i][j]["demand"] += 1
        return

    def get_name(self):
        """see generic_topology_programming.py"""
        return "ssp_oblivious_tp"
