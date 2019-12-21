import pyswarms
from pyswarms.utils.functions import single_obj

## COPYRIGHT FROM PYSWARMS LIBRARY --> THIS LIBRARY IS CREATED BY A COMMUNITY

def rosenbrockFunction(**kwargs):

    try:

        #DECLARE DICT OF PSO OPTIONS
        options = kwargs.get('options')

        optimizer = pyswarms.single.GlobalBestPSO(n_particles=kwargs.get('particles'), dimensions=kwargs.get('dimensions'), options=options)

        cost, pos = optimizer.optimize(single_obj.rosenbrock, iters=kwargs.get('iters'))

        return cost, pos
    except:
        raise