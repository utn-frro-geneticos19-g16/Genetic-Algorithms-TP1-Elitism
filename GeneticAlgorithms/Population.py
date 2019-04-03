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
    
    # Show Actual Population
    def showPopulation(self,num):
        large = self.getChromSize()
        print("Population ",(num+1),":")
        for chroms in (self.population):
            for i in range(large):
                print(chroms.getBody()[i],end='')
            print()
        print()
    
    # Reproduction
    def reproduce(self):
        pass
    
    # Update Total of Objective Functions
    def updateTotalObjAdapt(self,oneObjectiveValue):
        self.totalObjAdapt += oneObjectiveValue
    
    # Add to Population
    def addChrom(self,Chrom):
        self.population.append(Chrom)
    
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
    