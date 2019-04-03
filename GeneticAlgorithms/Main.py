#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
--- Acá hay que escribir el enunciado, alta paja ---
Created on 3 abr. 2019

@author: Antonelli, Nicolás - Recalde, Alejando - Rohn, Alex
'''
from GeneticAlgorithms.Population import Population
# from GeneticAlgorithms import Chromosome

# ImportantValues
iterationLimit = 3 #900
initPopulationNum = 4
chromsomeSize = 5
crossoverProb = 95
mutationProb = 2

# Constructor
if __name__ == '__main__':
    # First Population
    pob = Population(initPopulationNum,chromsomeSize,crossoverProb,mutationProb)
    
    # Iterations
    for iterationCount in range(iterationLimit):
        print()
        pob.showPopulation(iterationCount);

        # In the last iteration, the chromosome population mustn't reproduce
        if(iterationCount<iterationLimit):
            pob.reproduce();
    
    # End Comparation
    print("Convergence has occurred correctly")
    