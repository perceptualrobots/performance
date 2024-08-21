

from memory_profiler import profile


from os import sep
import random
from deap import base, creator

from epct.evolvers import CommonToolbox
from epct.po_evolvers import HPCTIndividual, HPCTEvolveProperties, HPCTEvolverWrapper


# mprof run evolve\individual.py
# mprof plot

# @profile
def main():

    env_name = 'ARC' 
    filename = 'ARC0101-FitnessError-MovingAverageError-Mode00-100'
    root = 'testfiles'
    file = root + sep + env_name + sep + filename + ".properties"

    max = False
    if max:
        pass
        min=False
        if hasattr(creator, 'FitnessMax'):
                pass
        else:
                creator.create("FitnessMax", base.Fitness, weights=(1.0,))
                creator.create("Individual", HPCTIndividual, fitness=creator.FitnessMax)
    else:
        # flip=False
        min=True
        if hasattr(creator, 'FitnessMin'):
                pass
        else:
                creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
                creator.create("Individual", HPCTIndividual, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        CommonToolbox.getInstance().set_toolbox(toolbox)

        verbose = {'debug': 2,  'evolve_verbose': 1, 'deap_verbose': False, 'save_arch_all': False,
                        'save_arch_gen': False, 'run_gen_best':False, 'display_env': False, 'hpct_verbose':False}


    seed = 1
    hep = HPCTEvolveProperties()
    hash_num, desc, properties_str = hep.configure_evolver_from_properties_file(file=file, seed=seed, verbose=verbose, toolbox=toolbox,  
                    min=min, print_properties=False)        
    evr = HPCTEvolverWrapper(**hep.wrapper_properties)

    print(f'seed={seed}')
    random.seed(seed)
    ind = evr.toolbox.individual()
    print(ind.get_grid())	


if __name__ == "__main__":
    main()
