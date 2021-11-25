"""
# see config_sndlib.py for detailed info
"""
import os

from config.generic_config import GenericTopologyZooSetup
from utility.const import TOPOLOGY_ZOO_BASE_DIR as TOP_BASE

# GenericTopologyZooSetup
class Bsoneteurope(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'BsonetEurope.graphml')
        self.TM_FIXED_TOTAL_VALUES = [61665]


class Gridnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Gridnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [103607]


class Nordu2005(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Nordu2005.graphml')
        self.TM_FIXED_TOTAL_VALUES = [45538]


class Nordu1997(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Nordu1997.graphml')
        self.TM_FIXED_TOTAL_VALUES = [51739]


class Sanren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Sanren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [31937]


class Sprint(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Sprint.graphml')
        self.TM_FIXED_TOTAL_VALUES = [62983]


class Navigata(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Navigata.graphml')
        self.TM_FIXED_TOTAL_VALUES = [60158]


class Garr199905(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr199905.graphml')
        self.TM_FIXED_TOTAL_VALUES = [51482]


class Claranet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Claranet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [63096]


class Cesnet1999(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet1999.graphml')
        self.TM_FIXED_TOTAL_VALUES = [43123]


class Ai3(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ai3.graphml')
        self.TM_FIXED_TOTAL_VALUES = [33607]


class Atmnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Atmnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [41280]


class Janetlense(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Janetlense.graphml')
        self.TM_FIXED_TOTAL_VALUES = [137225]


class Renam(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renam.graphml')
        self.TM_FIXED_TOTAL_VALUES = [17024]


class Ans(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ans.graphml')
        self.TM_FIXED_TOTAL_VALUES = [59458]


class Goodnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Goodnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [83661]


class Karen(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Karen.graphml')
        self.TM_FIXED_TOTAL_VALUES = [64141]


class Belnet2005(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2005.graphml')
        self.TM_FIXED_TOTAL_VALUES = [165762]


class Hurricaneelectric(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HurricaneElectric.graphml')
        self.TM_FIXED_TOTAL_VALUES = [88007]


class Uran(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Uran.graphml')
        self.TM_FIXED_TOTAL_VALUES = [48430]


class Elibackbone(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'EliBackbone.graphml')
        self.TM_FIXED_TOTAL_VALUES = [95570]


class Crlnetworkservices(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'CrlNetworkServices.graphml')
        self.TM_FIXED_TOTAL_VALUES = [65585]


class Vinaren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Vinaren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [53261]


class Belnet2007(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2007.graphml')
        self.TM_FIXED_TOTAL_VALUES = [66365]


class York(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'York.graphml')
        self.TM_FIXED_TOTAL_VALUES = [43465]


class Geant2001(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Geant2001.graphml')
        self.TM_FIXED_TOTAL_VALUES = [99847]


class Garr200112(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200112.graphml')
        self.TM_FIXED_TOTAL_VALUES = [58079]


class Ernet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ernet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [64000]


class Twaren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Twaren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [39130]


class Bbnplanet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Bbnplanet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [54501]


class Marnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Marnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [67514]


class Nextgen(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Nextgen.graphml')
        self.TM_FIXED_TOTAL_VALUES = [46000]


class Belnet2010(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2010.graphml')
        self.TM_FIXED_TOTAL_VALUES = [56593]


class Abilene(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Abilene.graphml')
        self.TM_FIXED_TOTAL_VALUES = [44529]


class Globalcenter(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Globalcenter.graphml')
        self.TM_FIXED_TOTAL_VALUES = [237291]


class Integra(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Integra.graphml')
        self.TM_FIXED_TOTAL_VALUES = [75781]


class Kreonet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Kreonet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [63368]


class Easynet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Easynet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [60524]


class Kentmanjan2011(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'KentmanJan2011.graphml')
        self.TM_FIXED_TOTAL_VALUES = [65466]


class Noel(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Noel.graphml')
        self.TM_FIXED_TOTAL_VALUES = [68462]


class Iij(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Iij.graphml')
        self.TM_FIXED_TOTAL_VALUES = [123393]


class Cwix(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cwix.graphml')
        self.TM_FIXED_TOTAL_VALUES = [89317]


class Kentmanjul2005(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'KentmanJul2005.graphml')
        self.TM_FIXED_TOTAL_VALUES = [57541]


class Garr200404(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200404.graphml')
        self.TM_FIXED_TOTAL_VALUES = [68723]


class Oxford(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Oxford.graphml')
        self.TM_FIXED_TOTAL_VALUES = [54313]


class Singaren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Singaren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [39938]


class Garr200109(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200109.graphml')
        self.TM_FIXED_TOTAL_VALUES = [58034]


class Arpanet19728(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arpanet19728.graphml')
        self.TM_FIXED_TOTAL_VALUES = [53614]


class Compuserve(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Compuserve.graphml')
        self.TM_FIXED_TOTAL_VALUES = [67296]


class Arpanet19723(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arpanet19723.graphml')
        self.TM_FIXED_TOTAL_VALUES = [51320]


class Funet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Funet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [59791]


class Getnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Getnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [42222]


class Reuna(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Reuna.graphml')
        self.TM_FIXED_TOTAL_VALUES = [25576]


class Unic(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'UniC.graphml')
        self.TM_FIXED_TOTAL_VALUES = [50662]


class Belnet2009(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2009.graphml')
        self.TM_FIXED_TOTAL_VALUES = [45717]


class Cesnet2001(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet2001.graphml')
        self.TM_FIXED_TOTAL_VALUES = [56617]


class Grnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Grnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [74943]


class Gtspoland(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'GtsPoland.graphml')
        self.TM_FIXED_TOTAL_VALUES = [78870]


class Evolink(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Evolink.graphml')
        self.TM_FIXED_TOTAL_VALUES = [85527]


class Heanet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Heanet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [64015]


class Intranetwork(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Intranetwork.graphml')
        self.TM_FIXED_TOTAL_VALUES = [27670]


class Janetbackbone(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Janetbackbone.graphml')
        self.TM_FIXED_TOTAL_VALUES = [114697]


class Basnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Basnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [35130]


class Highwinds(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Highwinds.graphml')
        self.TM_FIXED_TOTAL_VALUES = [101700]


class Biznet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Biznet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [61250]


class Shentel(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Shentel.graphml')
        self.TM_FIXED_TOTAL_VALUES = [56268]


class Packetexchange(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Packetexchange.graphml')
        self.TM_FIXED_TOTAL_VALUES = [62110]


class Cesnet200304(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet200304.graphml')
        self.TM_FIXED_TOTAL_VALUES = [65208]


class Savvis(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Savvis.graphml')
        self.TM_FIXED_TOTAL_VALUES = [51796]


class Geant2012(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Geant2012.graphml')
        self.TM_FIXED_TOTAL_VALUES = [136139]


class Sanet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Sanet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [56517]


class Widejpn(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'WideJpn.graphml')
        self.TM_FIXED_TOTAL_VALUES = [61170]


class Marwan(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Marwan.graphml')
        self.TM_FIXED_TOTAL_VALUES = [43591]


class Gtsslovakia(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'GtsSlovakia.graphml')
        self.TM_FIXED_TOTAL_VALUES = [98819]


class Belnet2003(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2003.graphml')
        self.TM_FIXED_TOTAL_VALUES = [93337]


class Ilan(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ilan.graphml')
        self.TM_FIXED_TOTAL_VALUES = [63876]


class Palmetto(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Palmetto.graphml')
        self.TM_FIXED_TOTAL_VALUES = [96738]


class Garr201103(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201103.graphml')
        self.TM_FIXED_TOTAL_VALUES = [202252]


class Garr201012(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201012.graphml')
        self.TM_FIXED_TOTAL_VALUES = [195697]


class Niif(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Niif.graphml')
        self.TM_FIXED_TOTAL_VALUES = [77390]


class Bics(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Bics.graphml')
        self.TM_FIXED_TOTAL_VALUES = [118752]


class Digex(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Digex.graphml')
        self.TM_FIXED_TOTAL_VALUES = [51940]


class Gtshungary(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'GtsHungary.graphml')
        self.TM_FIXED_TOTAL_VALUES = [65200]


class Fatman(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Fatman.graphml')
        self.TM_FIXED_TOTAL_VALUES = [61000]


class Garr201110(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201110.graphml')
        self.TM_FIXED_TOTAL_VALUES = [206167]


class Surfnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Surfnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [87564]


class Garr201101(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201101.graphml')
        self.TM_FIXED_TOTAL_VALUES = [195697]


class Garr201107(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201107.graphml')
        self.TM_FIXED_TOTAL_VALUES = [204473]


class Nordu1989(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Nordu1989.graphml')
        self.TM_FIXED_TOTAL_VALUES = [37626]


class Chinanet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Chinanet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [110172]


class Uninet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Uninet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [77569]


class Garr201109(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201109.graphml')
        self.TM_FIXED_TOTAL_VALUES = [206167]


class Visionnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'VisionNet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [21612]


class Quest(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Quest.graphml')
        self.TM_FIXED_TOTAL_VALUES = [98961]


class Uunet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Uunet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [135994]


class Switchl3(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'SwitchL3.graphml')
        self.TM_FIXED_TOTAL_VALUES = [143755]


class Pacificwave(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Pacificwave.graphml')
        self.TM_FIXED_TOTAL_VALUES = [45710]


class Grena(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Grena.graphml')
        self.TM_FIXED_TOTAL_VALUES = [33555]


class Cynet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cynet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [58734]


class Kentmanfeb2008(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'KentmanFeb2008.graphml')
        self.TM_FIXED_TOTAL_VALUES = [61399]


class Internetmci(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Internetmci.graphml')
        self.TM_FIXED_TOTAL_VALUES = [115012]


class Bteurope(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'BtEurope.graphml')
        self.TM_FIXED_TOTAL_VALUES = [87629]


class Iinet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Iinet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [62821]


class Roedunet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Roedunet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [73480]


class Hiberniacanada(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HiberniaCanada.graphml')
        self.TM_FIXED_TOTAL_VALUES = [46226]


class Gblnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Gblnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [21498]


class Bren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Bren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [68377]


class Arpanet19719(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arpanet19719.graphml')
        self.TM_FIXED_TOTAL_VALUES = [63907]


class Pionierl1(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'PionierL1.graphml')
        self.TM_FIXED_TOTAL_VALUES = [87463]


class Jgn2Plus(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Jgn2Plus.graphml')
        self.TM_FIXED_TOTAL_VALUES = [35926]


class Cernet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cernet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [120931]


class Geant2010(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Geant2010.graphml')
        self.TM_FIXED_TOTAL_VALUES = [122744]


class Harnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Harnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [48869]


class Eenet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Eenet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [40364]


class Cesnet200511(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet200511.graphml')
        self.TM_FIXED_TOTAL_VALUES = [96127]


class Rhnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Rhnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [40720]


class Telecomserbia(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Telecomserbia.graphml')
        self.TM_FIXED_TOTAL_VALUES = [32906]


class Hostwayinternational(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HostwayInternational.graphml')
        self.TM_FIXED_TOTAL_VALUES = [56687]


class Renater2008(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renater2008.graphml')
        self.TM_FIXED_TOTAL_VALUES = [75235]


class Spiralight(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Spiralight.graphml')
        self.TM_FIXED_TOTAL_VALUES = [41244]


class Peer1(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Peer1.graphml')
        self.TM_FIXED_TOTAL_VALUES = [55921]


class Renater2006(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renater2006.graphml')
        self.TM_FIXED_TOTAL_VALUES = [75235]


class Canerie(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Canerie.graphml')
        self.TM_FIXED_TOTAL_VALUES = [67760]


class Arpanet196912(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arpanet196912.graphml')
        self.TM_FIXED_TOTAL_VALUES = [18008]


class Cesnet1997(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet1997.graphml')
        self.TM_FIXED_TOTAL_VALUES = [41199]


class Mren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Mren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [16470]


class Agis(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Agis.graphml')
        self.TM_FIXED_TOTAL_VALUES = [83201]


class Netrail(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Netrail.graphml')
        self.TM_FIXED_TOTAL_VALUES = [44641]


class Arn(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arn.graphml')
        self.TM_FIXED_TOTAL_VALUES = [62980]


class Arnes(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arnes.graphml')
        self.TM_FIXED_TOTAL_VALUES = [72883]


class Carnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Carnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [81376]


class Networkusa(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'NetworkUsa.graphml')
        self.TM_FIXED_TOTAL_VALUES = [57128]


class Fccn(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Fccn.graphml')
        self.TM_FIXED_TOTAL_VALUES = [56816]


class Abvt(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Abvt.graphml')
        self.TM_FIXED_TOTAL_VALUES = [73333]


class Iowastatewidefibermap(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'IowaStatewideFiberMap.graphml')
        self.TM_FIXED_TOTAL_VALUES = [72487]


class Rediris(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Rediris.graphml')
        self.TM_FIXED_TOTAL_VALUES = [95774]


class Iris(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Iris.graphml')
        self.TM_FIXED_TOTAL_VALUES = [81837]


class Psinet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Psinet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [44232]


class Cudi(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cudi.graphml')
        self.TM_FIXED_TOTAL_VALUES = [30002]


class Renater2004(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renater2004.graphml')
        self.TM_FIXED_TOTAL_VALUES = [83372]


class Sago(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Sago.graphml')
        self.TM_FIXED_TOTAL_VALUES = [20451]


class Myren(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Myren.graphml')
        self.TM_FIXED_TOTAL_VALUES = [141472]


class Bellsouth(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Bellsouth.graphml')
        self.TM_FIXED_TOTAL_VALUES = [105891]


class Belnet2004(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2004.graphml')
        self.TM_FIXED_TOTAL_VALUES = [93337]


class Btasiapac(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'BtAsiaPac.graphml')
        self.TM_FIXED_TOTAL_VALUES = [104669]


class Ibm(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ibm.graphml')
        self.TM_FIXED_TOTAL_VALUES = [64596]


class Hiberniauk(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HiberniaUk.graphml')
        self.TM_FIXED_TOTAL_VALUES = [41899]


class Airtel(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Airtel.graphml')
        self.TM_FIXED_TOTAL_VALUES = [89210]


class Istar(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Istar.graphml')
        self.TM_FIXED_TOTAL_VALUES = [47263]


class Cesnet1993(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet1993.graphml')
        self.TM_FIXED_TOTAL_VALUES = [32902]


class Amres(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Amres.graphml')
        self.TM_FIXED_TOTAL_VALUES = [46569]


class Belnet2006(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2006.graphml')
        self.TM_FIXED_TOTAL_VALUES = [165762]


class Garr201003(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201003.graphml')
        self.TM_FIXED_TOTAL_VALUES = [104972]


class Garr201004(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201004.graphml')
        self.TM_FIXED_TOTAL_VALUES = [104972]


class Nsfnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Nsfnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [47444]


class Internode(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Internode.graphml')
        self.TM_FIXED_TOTAL_VALUES = [199609]


class Tinet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Tinet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [121482]


class Rnp(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Rnp.graphml')
        self.TM_FIXED_TOTAL_VALUES = [31267]


class Roedunetfibre(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'RoedunetFibre.graphml')
        self.TM_FIXED_TOTAL_VALUES = [84009]


class Renater1999(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renater1999.graphml')
        self.TM_FIXED_TOTAL_VALUES = [51681]


class Garr199901(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr199901.graphml')
        self.TM_FIXED_TOTAL_VALUES = [65749]


class Xeex(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Xeex.graphml')
        self.TM_FIXED_TOTAL_VALUES = [95480]


class Beyondthenetwork(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'BeyondTheNetwork.graphml')
        self.TM_FIXED_TOTAL_VALUES = [112346]


class Gambia(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Gambia.graphml')
        self.TM_FIXED_TOTAL_VALUES = [60052]


class Garr201111(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201111.graphml')
        self.TM_FIXED_TOTAL_VALUES = [202571]


class Garr201201(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201201.graphml')
        self.TM_FIXED_TOTAL_VALUES = [112315]


class Garr200902(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200902.graphml')
        self.TM_FIXED_TOTAL_VALUES = [133094]


class Aarnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Aarnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [63838]


class Azrena(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Azrena.graphml')
        self.TM_FIXED_TOTAL_VALUES = [39276]


class Lambdanet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'LambdaNet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [54235]


class Napnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Napnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [32292]


class Itnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Itnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [38444]


class Aconet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Aconet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [96885]


class Garr200212(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200212.graphml')
        self.TM_FIXED_TOTAL_VALUES = [52632]


class Geant2009(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Geant2009.graphml')
        self.TM_FIXED_TOTAL_VALUES = [121172]


class Garr201008(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201008.graphml')
        self.TM_FIXED_TOTAL_VALUES = [133576]


class Switch(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Switch.graphml')
        self.TM_FIXED_TOTAL_VALUES = [89401]


class Epoch(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Epoch.graphml')
        self.TM_FIXED_TOTAL_VALUES = [38645]


class Hibernianireland(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HiberniaNireland.graphml')
        self.TM_FIXED_TOTAL_VALUES = [44662]


class Restena(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Restena.graphml')
        self.TM_FIXED_TOTAL_VALUES = [54050]


class Sunet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Sunet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [63656]


class Garr201104(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201104.graphml')
        self.TM_FIXED_TOTAL_VALUES = [204577]


class Dataxchange(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Dataxchange.graphml')
        self.TM_FIXED_TOTAL_VALUES = [44862]


class Hiberniaus(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HiberniaUs.graphml')
        self.TM_FIXED_TOTAL_VALUES = [66440]


class Latnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Latnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [102914]


class Darkstrand(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Darkstrand.graphml')
        self.TM_FIXED_TOTAL_VALUES = [59932]


class Tlex(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'TLex.graphml')
        self.TM_FIXED_TOTAL_VALUES = [48855]


class Belnet2008(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Belnet2008.graphml')
        self.TM_FIXED_TOTAL_VALUES = [66365]


class Garr201001(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201001.graphml')
        self.TM_FIXED_TOTAL_VALUES = [105276]


class Layer42(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Layer42.graphml')
        self.TM_FIXED_TOTAL_VALUES = [43322]


class Arpanet19706(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Arpanet19706.graphml')
        self.TM_FIXED_TOTAL_VALUES = [41481]


class Hiberniaireland(GenericTopologyZooSetup):

    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HiberniaIreland.graphml')
        self.TM_FIXED_TOTAL_VALUES = [35898]


class Attmpls(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'AttMpls.graphml')
        self.TM_FIXED_TOTAL_VALUES = [220750]


class Columbus(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Columbus.graphml')
        self.TM_FIXED_TOTAL_VALUES = [82629]


class Garr200908(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200908.graphml')
        self.TM_FIXED_TOTAL_VALUES = [132937]


class Cesnet200603(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet200603.graphml')
        self.TM_FIXED_TOTAL_VALUES = [96127]


class Gtsromania(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'GtsRomania.graphml')
        self.TM_FIXED_TOTAL_VALUES = [55394]


class Garr201010(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201010.graphml')
        self.TM_FIXED_TOTAL_VALUES = [195697]


class Bellcanada(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Bellcanada.graphml')
        self.TM_FIXED_TOTAL_VALUES = [81861]


class Garr199904(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr199904.graphml')
        self.TM_FIXED_TOTAL_VALUES = [49947]


class Renater2001(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renater2001.graphml')
        self.TM_FIXED_TOTAL_VALUES = [64144]


class Cesnet201006(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet201006.graphml')
        self.TM_FIXED_TOTAL_VALUES = [97046]


class Btnorthamerica(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'BtNorthAmerica.graphml')
        self.TM_FIXED_TOTAL_VALUES = [280954]


class Garr201102(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201102.graphml')
        self.TM_FIXED_TOTAL_VALUES = [118974]


class Xspedius(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Xspedius.graphml')
        self.TM_FIXED_TOTAL_VALUES = [140571]


class Gtsczechrepublic(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'GtsCzechRepublic.graphml')
        self.TM_FIXED_TOTAL_VALUES = [50405]


class Dfn(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Dfn.graphml')
        self.TM_FIXED_TOTAL_VALUES = [123802]


class Garr200912(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200912.graphml')
        self.TM_FIXED_TOTAL_VALUES = [105276]


class Garr201112(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201112.graphml')
        self.TM_FIXED_TOTAL_VALUES = [112315]


class Pionierl3(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'PionierL3.graphml')
        self.TM_FIXED_TOTAL_VALUES = [69736]


class Garr201007(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201007.graphml')
        self.TM_FIXED_TOTAL_VALUES = [133576]


class Renater2010(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Renater2010.graphml')
        self.TM_FIXED_TOTAL_VALUES = [93605]


class Litnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Litnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [104280]


class Garr200909(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr200909.graphml')
        self.TM_FIXED_TOTAL_VALUES = [132918]


class Esnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Esnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [82514]


class Uninett2010(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Uninett2010.graphml')
        self.TM_FIXED_TOTAL_VALUES = [148631]


class Garr201105(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201105.graphml')
        self.TM_FIXED_TOTAL_VALUES = [204473]


class Cesnet200706(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cesnet200706.graphml')
        self.TM_FIXED_TOTAL_VALUES = [119467]


class Garr201108(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201108.graphml')
        self.TM_FIXED_TOTAL_VALUES = [204473]


class Hiberniaglobal(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'HiberniaGlobal.graphml')
        self.TM_FIXED_TOTAL_VALUES = [90228]


class Garr201005(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Garr201005.graphml')
        self.TM_FIXED_TOTAL_VALUES = [133576]


class Ulaknet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ulaknet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [264925]


class Uninett2011(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Uninett2011.graphml')
        self.TM_FIXED_TOTAL_VALUES = [154959]


class Forthnet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Forthnet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [110765]


class Asnetam(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'AsnetAm.graphml')
        self.TM_FIXED_TOTAL_VALUES = [128583]


class Missouri(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Missouri.graphml')
        self.TM_FIXED_TOTAL_VALUES = [85736]


class Globenet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Globenet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [100594]


class Sinet(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Sinet.graphml')
        self.TM_FIXED_TOTAL_VALUES = [130576]


class Syringa(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Syringa.graphml')
        self.TM_FIXED_TOTAL_VALUES = [49426]


class Intellifiber(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Intellifiber.graphml')
        self.TM_FIXED_TOTAL_VALUES = [93037]


class Vtlwavenet2011(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'VtlWavenet2011.graphml')
        self.TM_FIXED_TOTAL_VALUES = [57512]


class Redbestel(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'RedBestel.graphml')
        self.TM_FIXED_TOTAL_VALUES = [69132]


class Vtlwavenet2008(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'VtlWavenet2008.graphml')
        self.TM_FIXED_TOTAL_VALUES = [60974]


class Deltacom(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Deltacom.graphml')
        self.TM_FIXED_TOTAL_VALUES = [117841]


class Pern(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Pern.graphml')
        self.TM_FIXED_TOTAL_VALUES = [111343]


class Ion(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Ion.graphml')
        self.TM_FIXED_TOTAL_VALUES = [88147]


class Interoute(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Interoute.graphml')
        self.TM_FIXED_TOTAL_VALUES = [132803]


class Gtsce(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'GtsCe.graphml')
        self.TM_FIXED_TOTAL_VALUES = [99555]


class Tatanld(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'TataNld.graphml')
        self.TM_FIXED_TOTAL_VALUES = [112488]


class Colt(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Colt.graphml')
        self.TM_FIXED_TOTAL_VALUES = [83404]


class Uscarrier(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'UsCarrier.graphml')
        self.TM_FIXED_TOTAL_VALUES = [82260]


class Cogentco(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Cogentco.graphml')
        self.TM_FIXED_TOTAL_VALUES = [102189]


class Kdl(GenericTopologyZooSetup):
    def __init__(self):
        super().__init__()
        self.TOPOLOGY_FILE = os.path.join(TOP_BASE,'Kdl.graphml')
        self.TM_FIXED_TOTAL_VALUES = [186676]
