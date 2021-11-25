""" An instance of AlgorithmResult is returned by all TE algorithms """


class AlgorithmResult:
    def __init__(self):
        self.objective = -1
        self.execution_time = -1
        self.err_msg = ""
        self.success = False

        # wavelength_assignment {(i, j):#wavelengths} stores number of assigned wavelengths for each link;
        self.wavelength_assignment = dict()

        # utilization_map {(i, j): utilization } stores the util. value of a link; 1 := fully utilized, 0 := not in use
        self.utilization_map = dict()

        # flow_paths {(s,t):[s, ..., i, ..., t]} stores an ordered list of nodes as list from source of flow to its sink
        self.flow_paths = dict()
