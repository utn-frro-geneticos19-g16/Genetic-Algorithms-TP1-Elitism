#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GeneticAlgorithms.Chromosome import Chromosome
import random


class Population(object):
    # Class Attributes
    population = []  # Initial Population (Array of Chromosomes)
    totalObjPunc = 0  # The Sum of All Objective Functions Punctuation
    totalFitness = 0  # The Sum of All Objective Values

    # Constructor / Instance Attributes
    def __init__(self, numChroms, chromSize, crossProb, mutProb):
        self.numChroms = numChroms
        self.chromSize = chromSize
        self.crossProb = crossProb
        self.mutProb = mutProb
        print("Objective Function Coeficient:", Chromosome.getCoef())
        for _ in range(numChroms):
            oneChrom = Chromosome(chromSize, None)  # Initialization of Chromosomes
            self.addChrom(oneChrom)  # Add to Population
            oneObjectivePunctuation = oneChrom.getObjectivePunctuation()  # Objective Function Punctuation of Chromosome
            self.updateTotalObjPunc(oneObjectivePunctuation)  # Update Class Attribute

    # Show Actual Population and Stats
    def showPopulation(self, numIter):
        self.setTotalFitness(0)
        large = self.getChromSize()
        averageObjPunc = self.getTotalObjPunc() / len(self.population)
        fitness = 0
        maxVal = 0
        minVal = 0
        maxChrom = 0
        minChrom = 0
        print("Population ", (numIter + 1), ":")
        for i in range(len((self.population))):
            fitness = self.population[i].calcFitness(self.getTotalObjPunc())
            self.updateTotalFitness(fitness)
            if i == 0:
                maxVal = fitness
                minVal = fitness
            elif fitness > maxVal:
                maxVal = fitness
                maxChrom = i
            elif fitness < minVal:
                minVal = fitness
                minChrom = i
            for j in range(large):
                print(self.population[i].getBody()[j], end='')
            print()
        fitness = self.getTotalFitnessAverage()
        print()
        print("Chromosome --- Value --- Objective Punctuation --- Fitness")
        print("Max Values: Chrom Nº", maxChrom, "with:", self.population[maxChrom].getRealValue(), "Val,",
              self.population[maxChrom].getObjectivePunctuation(), "OP,", round(maxVal, 4), "Fit")
        print("Min Values: Chrom Nº", minChrom, "with:", self.population[minChrom].getRealValue(), "Val,",
              self.population[minChrom].getObjectivePunctuation(), "OP,", round(minVal, 4), "Fit")
        print("Average OP:", averageObjPunc, "--- Average Fitness:", fitness)  # round(fitness,6)
        print()

    # Update Total of Objective Functions Punctuation
    @classmethod
    def updateTotalObjPunc(cls, oneObjectiveValue):
        cls.totalObjPunc += oneObjectiveValue

    # Update Total Fitness
    @classmethod
    def updateTotalFitness(cls, fitness):
        cls.totalFitness += fitness

    # Add to Population
    def addChrom(self, Chrom):
        self.population.append(Chrom)

    # Reproduction
    def reproduce(self):
        parents = []  # List of Potential Parents
        newGeneration = [] # List of Children
        print("Roulette Results: ", end='')
        for _ in range(len(self.population)):
            parents.append(self.population[self.roulette()])  # Parents Selected by Roulette
        print()
        for i in range(0, len(parents), 2):
            father1 = parents[i]
            father2 = parents[i + 1]
            if self.crossPosibility():  # CrossOver Probability Evaluation
                son1, son2 = self.cross(father1, father2)  # CrossOver
                print("Successful CrossOver in reproduction:", (i + 2) / 2)  # Comment this One when Finish
            else:
                son1, son2 = self.copy(father1, father2)  # Direct Assignation (Without CrossOver)
                print("CrossOver didn't happen in reproduction:", (i + 2) / 2)  # Comment this One when Finish
            # Individual Mutation Probability Evaluation
            if self.mutationPosibility():
                son1 = self.mutation(son1)
            if self.mutationPosibility():
                son2 = self.mutation(son2)
            self.addChildren(son1, son2, newGeneration)
        self.replacePopulation(newGeneration)
        self.setTotalFitness(0)

    # Genetic Operator (Roulette Method)
    def roulette(self):
        # Generator of a Bidimensional List (Fitness Range of Chromosomes)
        newRoulette = [[0] * 2 for _ in range(len(self.population))]
        acum = 0  # Acumulator of Relative Fitness from 0 to 1 (Fills Roulette)
        for i in range(len(self.population)):
            newRoulette[i][0] = acum  # Range Min: Last Acum Value
            acum += round(self.population[i].getFitness(), 6)  # Acum's Value From Zero
            newRoulette[i][1] = acum  # Range Max: New Acum Value
        ranNum = round(random.uniform(0, 1), 6)  # Random Number from 0.000000 to 0.999999
        # print("Random: ", ranNum)  # Comment this One when Finish
        for i in range(len(newRoulette)):
            if newRoulette[i][0] < ranNum < newRoulette[i][1]:
                # Return Selected Chromosome if the Random Number Exists in its Range
                print(i, end=', ')
                return i
        print("Error")
        return "Error"

    def crossPosibility(self):  # CrossOver posibility evaluation
        if (self.getCrossProb() * 100 >= random.randint(1, 100)):
            return True
        else:
            return False

    def cross(self, chrom1, chrom2):
        newBody1 = []
        newBody2 = []
        cut = random.randint(1, len(chrom1.getBody()) - 2)  # Random Cut Point (Except by zero or all genes)
        for i in range(0, cut):  # Genetic Material Exchange (Genes)
            newBody1.append(chrom1.getBody()[i])  # Each Chromosome Exchange Genes With the Other One
            newBody2.append(chrom2.getBody()[i])
        for i in range(cut, len(chrom1.getBody())):
            newBody1.append(chrom2.getBody()[i])
            newBody2.append(chrom1.getBody()[i])
        # newGeneration.append(Chromosome(self.chromSize, newBody1))
        # newGeneration.append(Chromosome(self.chromSize, newBody2))
        son1 = Chromosome(self.chromSize, newBody1)
        son2 = Chromosome(self.chromSize, newBody2)
        print()
        print("Son 1:", self.listToInt(newBody1))  # Comment this One when Finish
        print("Son 2:", self.listToInt(newBody2))  # Comment this One when Finish
        print("Cut Point on:", cut)  # Comment this One when Finish
        return son1, son2

    def copy(self, chrom1, chrom2):
        # newGeneration.append(chrom1)
        # newGeneration.append(chrom2)
        son1 = chrom1
        son2 = chrom2
        print()
        print("Son 1 (Identical):", self.listToInt(chrom1.getBody()))  # Comment this One when Finish
        print("Son 2 (Identical):", self.listToInt(chrom2.getBody()))  # Comment this One when Finish
        return son1, son2

    def mutationPosibility(self):  # Mutation posibility evaluation
        if self.getMutProb() * 100 >= random.randint(1, 100):
            return True
        else:
            return False

    def mutation(self, chrom):  # Select one random Gen and Switch its Value
        mutPos = random.randint(1, len(self.population))
        newBody = []
        for i in range(len(chrom.getBody())):
            if i != mutPos:
                newBody.append(chrom.getBody()[i])
            else:
                if chrom.getBody()[mutPos] == 1:  # If is a '0' then change to '1', and vice-versa
                    newBody.append(0)
                else:
                    newBody.append(1)
        # newGeneration.append(Chromosome(self.chromSize, newBody))
        son = Chromosome(self.chromSize, newBody)
        print("Mutated Chrom in position:", mutPos, ":", self.listToInt(chrom.getBody()))
        # Comment this One when Finish
        return son

    def addChildren(self, son1, son2, newGeneration):
        newGeneration.append(son1)
        newGeneration.append(son2)

    def replacePopulation(self, newGeneration):  # Replace All Population in every Iteration
        self.population = []
        for i in range(len(newGeneration)):
            # print(newGeneration[i].getBody())
            # print(population[i.getBody())
            self.population.append(newGeneration[i])

    def listToInt(self, arr):
        num = ''.join(str(i) for i in arr)
        return int(num)

    # Class Getters and Setters
    @classmethod
    def getTotalObjPunc(cls):
        return cls.totalObjPunc

    @classmethod
    def setTotalObjPunc(cls, total):
        cls.totalObjPunc = total

    @classmethod
    def getTotalFitness(cls):
        return cls.totalFitness

    @classmethod
    def setTotalFitness(cls, total):
        cls.totalFitness = total

    @classmethod
    def getTotalFitnessAverage(cls):
        return cls.totalFitness / len(cls.population)

    # Getters and Setters 
    def getNumChroms(self):
        return self.numChroms

    def setNumChroms(self, numChroms):
        self.numChroms = numChroms

    def getChromSize(self):
        return self.chromSize

    def setChromSize(self, chromSize):
        self.chromSize = chromSize

    def getCrossProb(self):
        return self.crossProb

    def setCrossProb(self, crossProb):
        self.crossProb = crossProb

    def getMutProb(self):
        return self.mutProb

    def setMutProb(self, mutProb):
        self.mutProb = mutProb
