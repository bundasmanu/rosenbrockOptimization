import pygmo as pg

## COPYRIGHT FROM PYGMO LIBRARY --> THIS LIBRARY IS CREATED BY A COMMUNITY

def applyACO(**kwargs):

    try:

        prob = pg.problem(pg.rosenbrock(dim=kwargs.get('dim')))
        pop = pg.population(prob, size=kwargs.get('tamPopulation'), seed=23)
        algo = pg.algorithm(pg.gaco(kwargs.get('iters'), kwargs.get('kernel'), 1.0, 1e9, 0.0, 1, 7, 100000, 100000, 0.0, False, 23))
        algo.set_verbosity(1)
        pop = algo.evolve(pop)

        uda = algo.extract(pg.gaco)
        return uda.get_log()

    except:
        raise