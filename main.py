import PsoOptimization
import ACO_Optimization

def main():

    '''
        APLICACAO DO PSO
    '''
    print("\n-----------------------------\n")
    print("-------------------PSO---------------\n")
    print("-------------------------------------\n")

    args = {'options' : {'c1': 0.3, 'c2' : 0.3, 'w' : 0.9}, 'particles': 200, 'dimensions' : 60, 'iters' : 200}

    cost, pos = PsoOptimization.rosenbrockFunction(**args)
    print(cost, pos)

    '''
        APLICACAO DO ACO
    '''
    print("\n-----------------------------\n")
    print("-------------------ACO---------------\n")
    print("-------------------------------------\n")

    args = {'dim' : 60, 'tamPopulation' : 200, 'iters' : 200, 'kernel' : 200} #KERNEL EQUAL OR LOWER THAN POPULATION LENGTH

    logIterations = ACO_Optimization.applyACO(**args)
    print(logIterations)

if __name__ == "__main__":
    main()