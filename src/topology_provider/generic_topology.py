class GenericTopology:
    def get_topology(self) -> (dict, dict):
        """ returns topology map (i,j):info, node_info_dict i:info """
        msg = "Abstract topology provider - use a concrete class"
        raise Exception(msg)

    def get_name(self) -> str:
        """ returns name of topology """
        msg = "Abstract topology provider - use a concrete class"
        raise Exception(msg)
