import os
import networkx as nx

from topology_provider.generic_topology import GenericTopology


class TopologyZoo(GenericTopology):
    def __init__(self, topology_file_name: str):
        super().__init__()
        self.topology_file_name = os.path.abspath(topology_file_name)

    def __update_node_positions(self, nodes_no_position, nodes, edges):
        mean_x = sum(nodes[i]['x'] for i in nodes if i not in nodes_no_position) / (len(nodes) - len(nodes_no_position))
        mean_y = sum(nodes[i]['y'] for i in nodes if i not in nodes_no_position) / (len(nodes) - len(nodes_no_position))

        left = nodes_no_position
        while len(left) > 0:
            for current_i in nodes_no_position:
                adjacent_all = [j for i, j in edges.keys() if current_i == i]

                if len(adjacent_all) == 0:
                    nodes[current_i]['x'] = mean_x
                    nodes[current_i]['y'] = mean_y
                    left.remove(current_i)
                    continue

                adjacent_with_pos = [j for j in adjacent_all if j not in left]
                if len(adjacent_with_pos) == 0:
                    continue

                elif len(adjacent_with_pos) > 1:
                    pos_x = sum(nodes[j]['x'] for j in adjacent_with_pos) / len(adjacent_with_pos)
                    pos_y = sum(nodes[j]['y'] for j in adjacent_with_pos) / len(adjacent_with_pos)
                else:
                    # if only 1 adjacent node => use overall position mean for approximation
                    pos_x = (3 * nodes[adjacent_with_pos[0]]['x'] + mean_x) / 4
                    pos_y = (3 * nodes[adjacent_with_pos[0]]['y'] + mean_y) / 4

                nodes[current_i]['x'] = pos_x
                nodes[current_i]['y'] = pos_y
                left.remove(current_i)
            nodes_no_position = left
        return

    def get_topology(self) -> (dict, dict):
        if not os.path.exists(self.topology_file_name):
            msg = f"topology file not found: {self.topology_file_name}"
            raise Exception(msg)
        nx_graph = nx.read_graphml(self.topology_file_name, node_type=int)

        g_labels = nx.get_node_attributes(nx_graph, 'label')
        g_longitudes = nx.get_node_attributes(nx_graph, 'Longitude')
        g_latitude = nx.get_node_attributes(nx_graph, 'Latitude')

        node_map = dict()
        nodes_no_position = list()
        for index, node in enumerate(nx_graph.nodes):
            label = ""
            if index in g_labels:
                label = g_labels[index]

            if index in g_longitudes and index in g_latitude:
                x = g_longitudes[index]
                y = g_latitude[index]
            else:
                nodes_no_position.append(index)
                x = 0
                y = 0

            node_map[index] = {
                'label': label,
                'index': index,
                'x': x,
                'y': y,
            }

        g_link_speed = nx.get_edge_attributes(nx_graph, 'LinkSpeed')
        g_link_speed_units = nx.get_edge_attributes(nx_graph, 'LinkSpeedUnits')
        g_link_label = nx.get_edge_attributes(nx_graph, 'LinkLabel')
        g_link_note = nx.get_edge_attributes(nx_graph, 'LinkNote')
        g_link_speed_raw = nx.get_edge_attributes(nx_graph, 'LinkSpeedRaw')

        topology = dict()
        for edge in nx_graph.edges:
            i = edge[0]
            j = edge[1]
            speed = -1
            if edge in g_link_speed:
                speed = g_link_speed[edge]
            speed_units = None
            if edge in g_link_speed_units:
                speed_units = g_link_speed_units[edge]
            label = ""
            if edge in g_link_label:
                label = g_link_label[edge]
            note = None
            if edge in g_link_note:
                note = g_link_note[edge]
            speed_raw = None
            if edge in g_link_speed_raw:
                speed_raw = g_link_speed_raw[edge]

            topology[(i, j)] = topology[(j, i)] = {
                'speed': speed,
                'speed_units': speed_units,
                'label': label,
                'note': note,
                'speed_raw': speed_raw,
            }

        # approximate unknown position by neighbours
        try:
            self.__update_node_positions(nodes_no_position, node_map, topology)
        except:
            pass
        return topology, node_map

    def get_name(self) -> str:
        return os.path.basename(self.topology_file_name).replace('.', '_')
