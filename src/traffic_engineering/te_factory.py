from traffic_engineering.generic_traffic_engineering import GenericTrafficEngineering
from traffic_engineering.heuristic.shortest_path_throughput_te import ShortestPathThroughputTe
from traffic_engineering.ilp.ilp_throughput_joint import IlpThroughputJoint
from traffic_engineering.ilp.ilp_throughput_te import IlpThroughputTe
from traffic_engineering.lp.lp_throughput_joint import LpThroughputJoint
from traffic_engineering.lp.lp_throughput_te import LpThroughputTe


def get_te_algorithm(name: str) -> GenericTrafficEngineering:
    """ returns the requested topology engineering instance """
    name = name.lower()

    # throughput
    if name == "lp_throughput_joint":
        return LpThroughputJoint()
    if name == "lp_throughput_te":
        return LpThroughputTe()
    if name == "ilp_throughput_joint":
        return IlpThroughputJoint()
    if name == "ilp_throughput_te":
        return IlpThroughputTe()
    if name == "shortest_path_throughput":
        return ShortestPathThroughputTe()

    err_msg = f"TE algorithm not found: {name}"
    raise Exception(err_msg)
