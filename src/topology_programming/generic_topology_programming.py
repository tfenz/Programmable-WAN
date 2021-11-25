import operator

import matplotlib.pyplot as plt
import networkx as nx

from utility import const


class GenericTopologyProgramming:
    @staticmethod
    def _temp_plot_top(nx_graph: nx.Graph, file: str = "temp.pdf", req: bool = False):
        if req:
            val = nx.get_edge_attributes(nx_graph, 'demand')
            node_color = "orange"
            title = "Requested capacity"
        else:
            node_color = "blue"
            val = nx.get_edge_attributes(nx_graph, 'wavelengths')
            title = "Wavelength assignment"

        nx_g_layout = nx.kamada_kawai_layout(nx_graph)
        plt.figure()
        nx.draw(nx_graph, nx_g_layout, edge_color='black', node_size=100, with_labels=True, font_color="white",
                font_size=4, labels={node: node for node in nx_graph.nodes()}, node_color=node_color)
        nx.draw_networkx_edge_labels(nx_graph, nx_g_layout, edge_labels=val, font_size=3)
        plt.title(title.title())
        plt.axis('off')
        plt.savefig(file)
        plt.close()

    @staticmethod
    def _get_nx_graph(topology, wl, li):
        nx_graph = nx.Graph(list(topology.keys()))
        nx.set_node_attributes(nx_graph, 0, "wl_left")
        nx.set_node_attributes(nx_graph, 0, "demand_adj")
        nx.set_edge_attributes(nx_graph, 0, "demand")
        nx.set_edge_attributes(nx_graph, 0, "wavelengths")

        for node in nx_graph.nodes:
            nx_graph.nodes[node]["wl_left"] = wl * nx.degree(nx_graph, node) / li
        return nx_graph

    @staticmethod
    def _set_edge_weights(nx_graph: nx.Graph, demand_matrix: dict):
        raise Exception("Abstract Algorithm - use a concrete class")

    def _set_base_assignment(self, nx_graph, wl_max):
        e_weights = nx.get_edge_attributes(nx_graph, 'demand')
        e_order = sorted(e_weights, key=operator.itemgetter(1), reverse=True)
        wl_used = dict()
        for (i, j) in e_order:
            demand_i = max(1, nx_graph.nodes[i]["demand_adj"])
            demand_j = max(1, nx_graph.nodes[j]["demand_adj"])
            wl_i = int(nx_graph.nodes[i]["wl_left"] * nx_graph[i][j]["demand"] / demand_i)
            wl_j = int(nx_graph.nodes[j]["wl_left"] * nx_graph[i][j]["demand"] / demand_j)
            wl_ij = int(min(wl_i, wl_j, wl_max))
            nx_graph[i][j]["wavelengths"] = wl_ij
            if i not in wl_used:
                wl_used[i] = 0
            if j not in wl_used:
                wl_used[j] = 0
            wl_used[i] += wl_ij
            wl_used[j] += wl_ij
        for i in nx_graph.nodes:
            nx_graph.nodes[i]["wl_left"] -= wl_used[i]
        return

    @staticmethod
    def _set_leftover_assignment(nx_graph, wl_max):
        e_weights = nx.get_edge_attributes(nx_graph, 'demand')
        e_order = sorted(e_weights, key=operator.itemgetter(1), reverse=True)
        n_assigned = -1
        rounds = 0
        while n_assigned != 0:
            rounds += 1
            n_assigned = 0
            for (i, j) in e_order:
                wl_i = nx_graph.nodes[i]["wl_left"]
                wl_j = nx_graph.nodes[j]["wl_left"]
                wl_ij = int(min(1, wl_i, wl_j, wl_max - nx_graph[i][j]["wavelengths"]))
                nx_graph[i][j]["wavelengths"] += wl_ij
                nx_graph.nodes[i]["wl_left"] -= wl_ij
                nx_graph.nodes[j]["wl_left"] -= wl_ij

    @staticmethod
    def _set_node_demand_adj(nx_graph):
        e_weights = nx.get_edge_attributes(nx_graph, 'demand')
        for node in nx_graph.nodes:
            sum_weights = 0
            for adj in nx_graph.neighbors(node):
                if (node, adj) in e_weights:
                    sum_weights += e_weights[(node, adj)]
                else:
                    sum_weights += e_weights[(adj, node)]

            nx_graph.nodes[node]["demand_adj"] = sum_weights
        return

    def get_assignment(self, topology: dict, max_wavelengths_edge: int, wavelength_limiter: float,
                       demand_matrix: dict = None, distribute_leftover: str = "Basic") -> dict:
        """
        computes the wavelength assignment for a given topology
        :param topology: dict with: {(i, j): info_dict, ...}
        :param max_wavelengths_edge : defines how many wavelength a link can carry
        :param wavelength_limiter: limits the number of wavelength a node can process
        :param demand_matrix: dict with: {(src_node, dst_node): packet_length, ...}
        :param distribute_leftover: distribute wavelengths which couldn't be assigned deterministicly
        :return: wavelength assignment as dict with {(i, j): #wavelengths, ...}
        """
        wl_map = dict()
        nx_graph = self._get_nx_graph(topology, max_wavelengths_edge, wavelength_limiter)

        self._set_edge_weights(nx_graph, demand_matrix)
        self._set_node_demand_adj(nx_graph)
        self._set_base_assignment(nx_graph, max_wavelengths_edge)
        if distribute_leftover:
            self._set_leftover_assignment(nx_graph, max_wavelengths_edge)

        nx_wl_map = nx.get_edge_attributes(nx_graph, 'wavelengths')
        for (i, j) in nx_wl_map:
            wl_map[i, j] = wl_map[j, i] = nx_wl_map[i, j]

        return wl_map

    def get_name(self):
        """ returns name of algorithm """
        err_msg = "Abstract Algorithm - use a concrete class"
        raise Exception(err_msg)

    def validate(self, topology, wl_map, wl, li):
        """ validates the wavelength assignment"""
        if len(wl_map) == 0:
            return

        if max(wl_map.values()) > wl:
            msg = f"max value exceeded on link: {max(wl_map.values())}/{wl}"
            raise Exception(f"{const.FAIL}warning: {self.get_name()}: {msg}")

        nx_graph = nx.Graph(list(topology.keys()))
        for node in nx_graph.nodes:
            node_wl_adj_max = wl * nx.degree(nx_graph, node) / li
            node_wl_adj_assigned = 0
            for adj in nx_graph.neighbors(node):
                node_wl_adj_assigned += wl_map[node, adj]
            if node_wl_adj_assigned > node_wl_adj_max:
                raise Exception(f"{const.FAIL}{self.get_name()}: max exceeded on node: {node}:"
                                f"{node_wl_adj_assigned}/{node_wl_adj_max}{const.CEND}")
        return
