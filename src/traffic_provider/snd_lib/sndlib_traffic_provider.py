import ntpath
import os
from xml.dom import minidom

from traffic_provider.generic_tm_provider import GenericTM


class SndLibTM(GenericTM):
    def __init__(self, tm_file: str, node_info: dict, t_sample_nr: int = 0, dm: float = 1,
                 tm_fixed_total: float = None):
        self.node_name_index_map = node_info
        self.traffic_matrix_file = tm_file
        self.sample_nr = t_sample_nr
        self.dm = dm
        self.tm_fixed_total = tm_fixed_total
        return

    def __get_transformed_tm(self, tm):
        total_demand, n_entries, mean = super().get_basic_stats(tm)
        dm = self.tm_fixed_total / total_demand
        tm.update((pair, demand * dm) for pair, demand in tm.items())
        return tm

    def __read_demand_xml(self) -> dict:
        full_file_name = os.path.abspath(self.traffic_matrix_file)
        abilene_xml = minidom.parse(full_file_name)
        demand_items = abilene_xml.getElementsByTagName('demand')
        demand_matrix = dict()
        for demand_item in demand_items:
            src_name = demand_item.getElementsByTagName('source')[0].firstChild.data
            src = self.node_name_index_map[src_name]['index']
            dst_name = demand_item.getElementsByTagName('target')[0].firstChild.data
            dst = self.node_name_index_map[dst_name]['index']
            if src == dst:
                continue
            value = float(demand_item.getElementsByTagName('demandValue')[0].firstChild.data) * self.dm
            if (src, dst) not in demand_matrix:
                demand_matrix[(src, dst)] = 0
            demand_matrix[(src, dst)] += value
        return demand_matrix

    def get_traffic_matrix(self) -> dict:
        tm = self.__read_demand_xml()
        if self.tm_fixed_total is None or self.tm_fixed_total <= 0:
            return tm
        return self.__get_transformed_tm(tm)

    def get_name(self) -> str:
        file_basename = ntpath.basename(self.traffic_matrix_file)
        return f"SndLib_{file_basename}"
