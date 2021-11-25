""" TP algorithm factory method """
import logging

from topology_programming.generic_topology_programming import GenericTopologyProgramming
from topology_programming.joint_tp import JointTP
from topology_programming.uniform_tp import UniformTP
from topology_programming.ssp_oblivious_tp import SSPObliviousTP


def get_tp_algorithm(name: str) -> GenericTopologyProgramming:
    """ returns the requested topology programming instance """
    name = name.lower()
    if name == "uniform_tp":
        return UniformTP()
    if name == "joint_tp":
        return JointTP()
    if name == "ssp_oblivious_tp":
        return SSPObliviousTP()

    err_msg = f"wan tp name not found: {name}"
    logging.error(err_msg)
    raise Exception(err_msg)
