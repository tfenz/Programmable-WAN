"""
# config_sndlib.py defines the test run on real world data from SNDLib: http://sndlib.zib.de/home.action?show=/docu.formats.gml.action%3Fframeset
    For the simulations we used the topology data as well as the traffic data (accumulated data as traffic matrix),
    particularly, the dataset of Abilene, Geant and Brain
# Topology: each class represents a sub-test of test instances on a single topology and the  corresponding traffic matrices
# Reconfig Parameter:
    - alpha (:= Node Limiter) a node can distribute only a limited number of wavelengths which
    - beta (:= Wavelength link Limit) a link can carry only a limited number of wavelengths)
    - gamma (:= Wavelenght Capacity) capacity of a single wavelength
    alpha, beta, gamma are all constant and uniform for all nodes/links.
# Traffic Scaling: To tune the experiments, the traffic is scaled to a fixed amount of traffic, preserving
    the relation between the flows. The scale factor is topology dependent.
"""
import os

from config.generic_config import GenericSndLib, GenericSndLibSynTraffic
from utility.const import SNDLIB_TRAFFIC_BASE_DIR as TM_BASE_DIR
from utility.const import SNDLIB_TOPOLOGY_BASE_DIR as TOP_BASE_DIR

class Abilene(GenericSndLib):
    def __init__(self):
        super().__init__()
        self.TM_FIXED_TOTAL_VALUES = [44529]
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE_DIR,"abilene.xml")
        self.TRAFFIC_MATRIX_FILES = [
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-0200.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-0420.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-0600.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-0800.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-1000.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-1200.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-1405.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-1600.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-1805.xml"),
            os.path.join(TM_BASE_DIR,"abilene/demandMatrix-abilene-zhang-5min-20040310-2000.xml"),
        ]


class AbileneSyn(GenericSndLibSynTraffic):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE_DIR,"abilene.xml")
        self.TM_FIXED_TOTAL_VALUES = [44529]


class Geant(GenericSndLib):
    def __init__(self):
        super().__init__()
        self.TM_FIXED_TOTAL_VALUES = [136139]
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE_DIR,"geant.xml")
        self.TRAFFIC_MATRIX_FILES = [
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-0200.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-0400.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-0600.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-0800.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-1000.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-1200.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-1400.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-1600.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-1800.xml"),
            os.path.join(TM_BASE_DIR,"geant/demandMatrix-geant-uhlig-15min-20050615-2000.xml"),
        ]


class GeantSyn(GenericSndLibSynTraffic):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE_DIR,"geant.xml")
        self.TM_FIXED_TOTAL_VALUES = [136139]
