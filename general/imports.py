

# mprof run evolve\arc.py
# mprof plot




from memory_profiler import profile # 21 Mb
import time # 21 Mb
from os import sep, makedirs # 21 Mb
from deap import base, creator # 32 Mb

import uuid
from pct.nodes import PCTNode
from pct.functions import WeightedSum
from pct.putils import UniqueNamer, FunctionsList, list_of_ones
from pct.functions import BaseFunction, HPCTFUNCTION # 34 Mb


import gym, math, os
import numpy as np
from abc import abstractmethod
from typing import Any, List, Optional

import pct.putils as vid
from pct.functions import BaseFunction, Constant
from pct.putils import FunctionsList, SingletonObjects, NumberStats, map_to_int_even_range, map_to_int_odd_range, get_rel_tol, get_abs_tol
from pct.network import ClientConnectionManager
from pct.webots import WebotsHelper # 36 Mb

# from pct.yaw_module import YawEnv  # 83 Mb

# arcenv
from time import sleep # 36 Mb
# import pygame # + 10 Mb 
# from matplotlib import colors  # + 10 Mb  


from pct.arc import ARCEnv
from pct.helpers import ListChecker, ChallengesDataManager

from pct.environments import EnvironmentFactory # 93 Mb
from pct.errors import BaseErrorCollector
from pct.putils import floatListsToString, PCTRunProperties



from pct.hierarchy import PCTHierarchy # 93 Mb
from epct.evolvers import CommonToolbox
from epct.po_evolvers import HPCTIndividual, HPCTEvolveProperties
# from pct.environment_processing import EnvironmentProcessingFactory

# from comet_ml import Experiment
# from comet_ml import api
# from comet_ml import Artifact

@profile
def main():
    # toc = time.perf_counter()
    # print(toc)
    print('Hello World')

if __name__ == "__main__":
    main()