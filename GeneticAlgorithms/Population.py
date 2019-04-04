#!/usr/bin/env python
# -*- coding: utf-8 -*-
from GeneticAlgorithms.Chromosome import Chromosome

class Population(object):
    
    # Class Attributes
    population = [] # Initial Population (Array of Chromosomes)
    totalObjAdapt = 0 # The Sum of All Objective Functions
    
    # Constructor / Instance Attributes
    def __init__(self,numChroms,chromSize,crossProb,mutProb):
        self.numChroms = numChroms
        self.chromSize = chromSize
        self.crossProb = crossProb
        self.mutProb = mutProb
        
        for _ in range(numChroms):
            oneChrom = Chromosome(chromSize) # Initialization of Chromosomes
            self.addChrom(oneChrom) # Add to Population
            oneObjectiveFunction = oneChrom.getObjectiveAdaptation() # Objective Function of Chromosomes
            self.updateTotalObjAdapt(oneObjectiveFunction) # Update Class Attribute 
    
    # Show Actual Population and Stats
    def showPopulation(self,numIter):
        large = self.getChromSize()
        averageAdapt = self.getTotalObjAdapt()/len(self.population)
        averageFit = 0
        maxVal = 0
        minVal = 0
        maxChrom = 0
        minChrom = 0
        print("Population ",(numIter+1),":")
        for i in range(len((self.population))):
            averageFit += self.population[i].calcFitness(self.getTotalObjAdapt())
            if averageFit>maxVal:
                maxVal=averageFit
                maxChrom=i
            elif averageFit<minVal:
                minVal=averageFit
                minChrom=i 
            for j in range(large):
                print(self.population[i].getBody()[j],end='')
            print()
        averageFit = averageFit/len(self.population)
        print()
        print("Chromosome --- Value --- Objective Punctuation --- Fitness")
        print("Max Values: Chrom Nº",maxChrom,"with:",self.population[maxChrom].getRealValue(),"Val,",self.population[maxChrom].getObjectiveAdaptation(),"OP,",maxVal,"Fit")
        print("Min Values: Chrom Nº",minChrom,"with:",self.population[minChrom].getRealValue(),"Val,",self.population[minChrom].getObjectiveAdaptation(),"OP,",minVal,"Fit")
        print("Average OP:",averageAdapt,"--- Average Fitness:",averageFit)
        print()
        
    # Update Total of Objective Functions
    @classmethod
    def updateTotalObjAdapt(self,oneObjectiveValue):
        self.totalObjAdapt += oneObjectiveValue
    
    # Add to Population
    def addChrom(self,Chrom):
        self.population.append(Chrom)
    
    # Reproduction
    def reproduce(self):
        pass
    
    def crossProb(self,vector):
        pass
    
    def cross(self,Chrom1,Chrom2,vector):
        pass
    
    def mutation(self,chrom):
        pass
    
    # def calculateAllFitness(self):
    
    
    # Class Methods
    @classmethod
    def getTotalObjAdapt(cls):
        return cls.totalObjAdapt

    @classmethod
    def setTotalObjAdapt(cls,total):
        cls.totalObjAdapt = total
        
    
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
    