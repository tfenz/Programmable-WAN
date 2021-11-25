import ntpath
import os
from xml.dom import minidom

from topology_provider.generic_topology import GenericTopology


class SndLibTop(GenericTopology):
    def __init__(self, topology_file_name):
        self.topology_file_name = topology_file_name

    def __read_network_xml(self) -> (dict, dict):
        full_file_name = os.path.abspath(self.topology_file_name)
        abilene_xml = minidom.parse(full_file_name)
        node_list = abilene_xml.getElementsByTagName('node')
        edge_list = abilene_xml.getElementsByTagName('link')

        node_map = dict()
        index = 0
        for node in node_list:
            name = node.getAttribute('id')
            # note mapping between name and id is necessary since Traffic will be mapped by name in snd lib tm reader
            node_map[name] = {
                'index': index,
                'x': node.getElementsByTagName('x')[0].firstChild.data,
                'y': node.getElementsByTagName('y')[0].firstChild.data,
            }
            index += 1

        topology = dict()
        for edge in edge_list:
            src_name = edge.getElementsByTagName('source')[0].firstChild.data
            i = node_map[src_name]['index']
            dst_name = edge.getElementsByTagName('target')[0].firstChild.data
            j = node_map[dst_name]['index']
            topology[(i, j)] = topology[(j, i)] = {
                'capacity': edge.getElementsByTagName('capacity')[0].firstChild.data,
                'cost': edge.getElementsByTagName('cost')[0].firstChild.data,
            }

        return topology, node_map

    def get_topology(self) -> (dict, dict):
        topology, node_name_index_map = self.__read_network_xml()
        return topology, node_name_index_map

    def get_name(self) -> str:
        return ntpath.basename(self.topology_file_name)
