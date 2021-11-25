import logging

from topology_provider.generic_topology import GenericTopology
from topology_provider.snd_lib.sndlib_top import SndLibTop
from topology_provider.topology_zoo.topology_zoo_top import TopologyZoo


def get_topology_factory(name: str, topology_file: str = "") -> GenericTopology:
    """ returns the requested topology provider instance """
    name = name.lower()
    if name == "topology_zoo":
        return TopologyZoo(topology_file)
    if name == "snd_lib":
        return SndLibTop(topology_file)
    msg = f"Topology Provider not found with: {name}\n" \
          f"Test setup probably misconfigured. Check if topology_provider and topology_file are correctly defined"
    logging.error(msg)
    raise Exception(msg)
