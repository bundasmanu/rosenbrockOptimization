import PsoOptimization
import ACO_Optimization

def main():

    '''
        APLICACAO DO PSO
    '''
    print("\n-----------------------------\n")
    print("-------------------PSO---------------\n")
    print("-------------------------------------\n")

    args = {'options' : {'c1': 0.3, 'c2' : 0.3, 'w' : 0.9}, 'particles': 100, 'dimensions' : 10, 'iters' : 50}

    cost, pos = PsoOptimization.rosenbrockFunction(**args)
    print(cost, pos)

    '''
        APLICACAO DO ACO
    '''
    print("\n-----------------------------\n")
    print("-------------------ACO---------------\n")
    print("-------------------------------------\n")

    args = {'dim' : 10, 'tamPopulation' : 100, 'iters' : 50, 'kernel' : 100} #KERNEL EQUAL OR LOWER THAN POPULATION LENGTH

    logIterations = ACO_Optimization.applyACO(**args)
    print(logIterations)

if __name__ == "__main__":
    main()