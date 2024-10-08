
from epct.evolve import evolve_setup
from cutils.paths import get_gdrive, get_root_path    
from memory_profiler import profile

#*
# mprof run evolve\arc.py
# mprof plot
#

@profile
def main():
    env_name = 'ARC' 
    filename = 'ARC0101-FitnessError-MovingAverageError-Mode00-2000'

    hierarchy_plots = "scEdges,scZero,scFitness"
    max=False        

    draw_file = False
    hpct_verbose= False
    save_arch_all = False

    plots_dir = '/tmp/ARC'

    drive = get_gdrive()
    root_path=get_root_path()
    configs_dir = 'Versioning/python/performance/testfiles/'

    verbosed = {'debug': 0,  'evolve_verbose': 1, 'deap_verbose': False, 'save_arch_all': save_arch_all,
                    'save_arch_gen': False, 'run_gen_best':True, 'display_env': False, 'hpct_verbose':hpct_verbose}

    arg = {'file': filename, 'env_name':env_name,  'draw_file' :draw_file, 'verbosed':verbosed, 
                            'max':max, 'drive':drive, 'root_path':root_path, 'configs_dir':configs_dir, 'hierarchy_plots': hierarchy_plots,
                            'plots_dir': plots_dir } 

    arg['seed']=1
    score = evolve_setup(arg)

    return score


if __name__ == "__main__":
    
    main()