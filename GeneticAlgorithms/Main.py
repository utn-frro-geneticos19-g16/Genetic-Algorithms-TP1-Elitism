#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
ENUNCIADO DEL TRABAJO PRÁCTICO N° 1

Hacer un programa que utilice un Algoritmo Genético Canónico para buscar un máximo de la función:
f(x) = (x/coef)^2 en el dominio [0 , 230-1]
-donde coef = 230-1

Teniendo en cuenta los siguientes datos:
–Probabilidad de Crossover = 0,75
–Probabilidad de Mutación = 0,05
–Población Inicial: 10 individuos
-Genes de cada Cromosoma: 32 (2^5)
–Ciclos del programa: 20
–Método de Selección: Ruleta
–Método de Crossover: 1 Punto
–Método de Mutación: invertida

El programa debe mostrar, finalmente, el Cromosoma correspondiente al valor máximo, el valor máximo, mínimo y promedio obtenido de cada población.
Mostrar la impresión de las tablas de mínimos, promedios y máximos para 20, 100 y 200 corridas.
Deben presentarse las gráficas de los valores Máximos, Mínimos y Promedios de la función objetivo por cada generación luego de correr el algoritmo genético 20, 100 y 200 iteraciones (una gráfica por cada conjunto de iteraciones)
Realizar comparaciones de las salidas corriendo el mismo programa en distintos ciclos de corridas y además realizar todos los cambios que considere oportunos en los parámetros de entrada de manera de enriquecer sus conclusiones.

FECHA DE ENTREGA DEL TRABAJO PRÁCTICO: 30 de Abril de 2019

--> Genetic-Algorithm TP1 --- V1.1 ---  Created on 3 abr. 2019
@author: Antonelli, Nicolás - Recalde, Alejando - Rohn, Alex
'''

from GeneticAlgorithms.Population import Population
# from GeneticAlgorithms.Chromosome import Chromosome
# import random

# ImportantValues
iterationLimit = 3 #20,100,200  # Population Iterations
initPopulationNum = 10          # Initial Population Size
chromsomeSize = 32              # Chromosome Size
crossoverProb = 0.75            # Probability of CrossOver
mutationProb = 0.05             # Probability of Mutation

# Main Constructor
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
    