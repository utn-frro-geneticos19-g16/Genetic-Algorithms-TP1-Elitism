#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GeneticAlgorithms.Chromosome import Chromosome

class Population(object):
    
    # Class Attributes
    population = [] # Initial Population (Array of Chromosomes)
    totalObjPunc = 0 # The Sum of All Objective Functions Punctuation
    totalFitness = 0 # The Sum of All Objective Values
    
    # Constructor / Instance Attributes
    def __init__(self,numChroms,chromSize,crossProb,mutProb):
        self.numChroms = numChroms
        self.chromSize = chromSize
        self.crossProb = crossProb
        self.mutProb = mutProb
        
        for _ in range(numChroms):
            oneChrom = Chromosome(chromSize) # Initialization of Chromosomes
            self.addChrom(oneChrom) # Add to Population
            oneObjectivePunctuation = oneChrom.getObjectivePunctuation() # Objective Function Punctuation of Chromosomes
            self.updateTotalObjPunc(oneObjectivePunctuation) # Update Class Attribute 
    
    # Show Actual Population and Stats
    def showPopulation(self,numIter):
        self.setTotalFitness(0)
        large = self.getChromSize()
        averageObjPunc = self.getTotalObjPunc()/len(self.population)
        fitness = 0
        maxVal = 0
        minVal = 0
        maxChrom = 0
        minChrom = 0
        print("Population ",(numIter+1),":")
        for i in range(len((self.population))):
            fitness = self.population[i].calcFitness(self.getTotalObjPunc())
            self.updateTotalFitness(fitness)
            if i==0:
                maxVal=fitness
                minVal=fitness
            elif fitness>maxVal:
                maxVal=fitness
                maxChrom=i
            elif fitness<minVal:
                minVal=fitness
                minChrom=i 
            for j in range(large):
                print(self.population[i].getBody()[j],end='')
            print()
        fitness = self.getTotalFitnessAverage()
        print()
        print("Chromosome --- Value --- Objective Punctuation --- Fitness")
        print("Max Values: Chrom Nº",maxChrom,"with:",self.population[maxChrom].getRealValue(),"Val,",self.population[maxChrom].getObjectivePunctuation(),"OP,",maxVal,"Fit")
        print("Min Values: Chrom Nº",minChrom,"with:",self.population[minChrom].getRealValue(),"Val,",self.population[minChrom].getObjectivePunctuation(),"OP,",minVal,"Fit")
        print("Average OP:",averageObjPunc,"--- Average Fitness:",fitness)
        print()
        
    # Update Total of Objective Functions Punctuation
    @classmethod
    def updateTotalObjPunc(cls,oneObjectiveValue):
        cls.totalObjPunc += oneObjectiveValue
    
    # Update Total Fitness
    @classmethod
    def updateTotalFitness(cls,fitness):
        cls.totalFitness += fitness
    
    # Add to Population
    def addChrom(self,Chrom):
        self.population.append(Chrom)
    
    
    def crossProb(self,vector):
        pass
    
    def cross(self,Chrom1,Chrom2,vector):
        pass
    
    def mutation(self,chrom):
        pass
    
    # Reproduction
    def reproduce(self):
        self.setTotalObjPunc(0)
        pass
    
    
    # Class Getters and Setters
    @classmethod
    def getTotalObjPunc(cls):
        return cls.totalObjPunc

    @classmethod
    def setTotalObjPunc(cls,total):
        cls.totalObjPunc = total
    
    @classmethod
    def getTotalFitness(cls):
        return cls.totalFitness
    
    @classmethod
    def setTotalFitness(cls,total):
        cls.totalFitness = total   
    
    @classmethod
    def getTotalFitnessAverage(cls):
        return cls.totalFitness/len(cls.population)
    
    
    # Getters and Setters 
    def getNumChroms(self):
        return self.numChroms
    
    def setNumChroms(self,numChroms):
        self.numChroms = numChroms
    
    def getChromSize(self):
        return self.chromSize
    
    def setChromSize(self,chromSize):
        self.chromSize = chromSize
    
    def getCrossProb(self):
        return self.crossProb
    
    def setCrossProb(self,crossProb):
        self.crossProb = crossProb
    
    def getMutProb(self):
        return self.mutProb
    
    def setMutProb(self,mutProb):
        self.mutProb = mutProb
    