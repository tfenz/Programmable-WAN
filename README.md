# On Efficient Oblivious Wavelength Assignments for Programmable Wide-Area Topologies

## Overview 
The code has been the basis for computational evaluations within the publication '**On Efficient Oblivious Wavelength Assignments for Programmable Wide-Area Topologies**'.
This repository contains all implemented algorithms, traffic generators and topology data reader. 
Additionally, we provide the config containing the parameter sets used in the evaluations.

## Dependencies and Requirements
We implemented the proposed algorithms in [Python (3.7.4)](https://www.python.org/downloads/release/python-374/) leveraging the library [NetworkX (2.4)](https://networkx.github.io/documentation/networkx-2.4/). 
To solve the ILP we used [Gurobi (9.1.0)](https://www.gurobi.com/downloads/gurobi-software/).  
We used [conda (4.8.2)](https://anaconda.org/anaconda/beautifulsoup4/files?version=4.8.2) as a package manager - see the conda [environment.yml](environment.yml) for further details of packages used in this repository.

The host machine was running Ubuntu 18.04.5 LTS.

## Structure

| Dir                                                        | Description                                                                      |
|------------------------------------------------------------|----------------------------------------------------------------------------------|
| **[data/](data)**                                          | real world traffic and topology data                                             |
| **[log/](log)**                                            | Default directory for log files                                                  |
| **[out/](out)**                                            | Default directory for output (result csv files will be stored there)             |
| **[src/](src)**                                            | Source root containing *main.py* - which is used as entry point of the program.  |
| **[src/config/](src/config)**                              | Config provider (defines parameter for evaluations)                              |
| **[src/topology_programming/](src/topology_programming)**  | Algorithms to compute topology programming (= wavelengths assignment) in WANs    |
| **[src/topology_provider/](src/topology_provider)**        | Topology provider (reads/prepares available real-world topology data)            |
| **[src/traffic_engineering/](src/traffic_engineering)**    | Routing algorithms for reconfigurable WANs                                       |
| **[src/traffic_provider/](src/traffic_provider)**          | Reads/prepares real world traffic data / generates synthetic traffic             |
| **[src/utility/](src/utility)**                            | Globally shared src                                                              |

## Prerequisites
### Conda
We use conda as package manager and provide an environment.yml defining the conda environment used in the evaluations.
For details go to: [install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

### Gurobi
We used Gurobi to solve linear problems. To reproduce the results a licence is required (academic licences: 
[info](https://www.gurobi.com/academia/academic-program-and-licenses/)). 
Download and install the Gurobi Optimizer (9.1.0) from [download](https://www.gurobi.com/downloads/).

## Real-World Data
To tune our experiments interestingly, we use real world data for both - topologies and demands from [SNDLib](http://sndlib.zib.de/home.action) and [TopologyZoo](http://www.topology-zoo.org/dataset.html).

### SNDLib Data
We use traffic and topology data from SNDLib, which we redistribute under the [ZIB ACADEMIC LICENSE](data/LICENSE_SNDLib).
The data is stored in the directory **[data/](data)**.

### TopologyZoo Data
Additionally, we use the topology data available from [TopologyZoo](http://www.topology-zoo.org/dataset.html).

**Note:** The data from topology zoo is **NOT** included in the repository and must be manually added:
1. Download the whole dataset: [Download](http://www.topology-zoo.org/files/archive.zip)
2. Unzip the data
3. Save the *.graphml files in the directory [data/topologies/topology_zoo](data/topologies/topology_zoo/))

## Install Dependencies
Create a conda environment and install all python dependencies with:
```bash
conda env create -f environment.yml
```
The created environment is named 'wan_ancs', activate with:
```bash 
conda activate wan_ancs
```

## Run Tests
Navigate to source code root:
```bash 
cd ./src
```

### Configuration
We provide two predefined configurations which store multiple sets of parameters controlling the test flow.
1. config_sndlib
2. config_topology_zoo

*Note: All config files must be stored in ./src/config/* 

### Start 
Run evaluation with:
```bash 
python main.py [-c <config name>] [-l <dir>] [-o <dir>] [--debug]
```
### Optional Parameters:
| Arg           | Description                                                  | Default            |
|---------------|--------------------------------------------------------------|--------------------|
| -c \<config\> | Defines the config file (as in ./config/\<config name\>.py)  | **config_sndlib**  |
| -l \<dir\>    | Defines the path to log dir                                  | **./log/**         |
| -o \<dir\>    | Defines the path to out dir                                  | **./out/**         |
| --debug       | Extends logging                                              |                    |

### Example
Start the evaluation using data from [Topology Zoo](http://www.topology-zoo.org/dataset.html) (config defined in: *./src/config/config_topology_zoo.py*) with:
```bash 
python main.py -c config_topology_zoo
```

Start the evaluation using data from [SNDLib data](http://sndlib.zib.de/home.action?show=/docu.formats.gml.action%3Fframeset) (config defined in: *./src/config/config_sndlib.py*) with:
```bash 
python main.py -c config_sndlib
```

### Output
The results are stored in a csv file located in the defined out directory

## Contact
*[Contact Me](mailto:thomas.fenz@univie.ac.at)* or visit [University of Vienna | Communication Technologies](https://ct.cs.univie.ac.at/) for more infos.

*This project is licensed under the [MIT License](LICENSE)*.

