#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ENUNCIADO DEL TRABAJO PRÁCTICO N° 1

Hacer un programa que utilice un Algoritmo Genético Canónico para buscar un máximo de la función:
f(x) = (x/coef)^2 en el dominio [0 , 230-1] --> Error Enunciado: dominio [0 , (2^30)-1]
-Donde coef = 230-1 --> Error Enunciado: coef = (2^30)-1

Teniendo en cuenta los siguientes datos:
–Probabilidad de Crossover = 0,75
–Probabilidad de Mutación = 0,05
–Población Inicial: 10 individuos
-Genes de cada Cromosoma: 30
–Ciclos del programa: 20
–Método de Selección: Ruleta
–Método de Crossover: 1 Punto
–Método de Mutación: invertida

El programa debe mostrar, finalmente, el Cromosoma correspondiente al valor máximo, el valor máximo, mínimo y promedio
obtenido de cada población.

Mostrar la impresión de las tablas de mínimos, promedios y máximos para 20, 100 y 200 corridas.
Deben presentarse las gráficas de los valores Máximos, Mínimos y Promedios de la función objetivo por cada generación
luego de correr el algoritmo genético 20, 100 y 200 iteraciones (una gráfica por cada conjunto de iteraciones)

Realizar comparaciones de las salidas corriendo el mismo programa en distintos ciclos de corridas y además realizar
todos los cambios que considere oportunos en los parámetros de entrada de manera de enriquecer sus conclusiones.


FECHA DE ENTREGA DEL TRABAJO PRÁCTICO: 30 de Abril de 2019

--> Genetic-Algorithm TP1 --- V4.5 ---  Created on 3 abr. 2019

            Antonelli, Nicolás - Recalde, Alejando - Rohn, Alex
"""

from GeneticAlgorithmsElitism.Population import Population
from GeneticAlgorithmsElitism.Graphs import Graphic
# from GeneticAlgorithmsElitism.Chromosome import Chromosome
# import random


if __name__ == '__main__':
    # ImportantValues
    iterationLimit = 50  # 20,100,200  # Population Iterations
    initPopulationNum = 10  # Initial Population Size
    chromsomeSize = 30  # Chromosome Size
    crossoverProb = 0.75  # Probability of CrossOver
    mutationProb = 0.05  # Probability of Mutation

    # Initialize
    class Main(object):
        # First Population
        pob = Population(initPopulationNum, chromsomeSize, crossoverProb, mutationProb)
        graphicsData = {'averageOPs': [], 'minOPs': [], 'maxOPs': []}  # Dictionary for Graphics

        # Iterations
        for iterationCount in range(iterationLimit):
            print()
            averageOP, minOP, maxOP, elitChrom, secondElitChrom = pob.showPopulation(iterationCount)  # Show Actual Population and Return Data

            # Update Dictionary with important values
            graphicsData['averageOPs'].append(averageOP)
            graphicsData['minOPs'].append(minOP)
            graphicsData['maxOPs'].append(maxOP)

            # In the last iteration, the chromosomes population mustn't reproduce
            if iterationCount < iterationLimit - 1:
                pob.reproduce(elitChrom, secondElitChrom)  # Reproduction of Actual Generation

        # Graph Population's Evolution
        graph = Graphic(graphicsData, iterationLimit)
        graph.showPlots()

        # Last Reproduction Message
        print("Last Generation Reached Correctly")
        print("------------")
        print()
        print()

        # Final Tables
        print("TABLAS FINALES")
        print()
        print("Población ------------ Mínimo ------------ Máximo ------------ Promedio")
        for value in range(iterationLimit):
            print("Generación ", value, ":", graphicsData['minOPs'][value], "---", graphicsData['maxOPs'][value], "---",
                  graphicsData['averageOPs'][value])
