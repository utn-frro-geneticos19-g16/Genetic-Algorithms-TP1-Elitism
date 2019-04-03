#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Chromosome(object): 
    
    # Constructor / Instance Attributes
    def __init__(self, large):
        
        # Chromosome's Genes
        self.body = []
        self.large = large
        for _ in range (large):
            self.body.append(str((random.randint(0,1))))
        
        # Initialize Objective Adaptation and Fitness
        binStr = ''.join(self.body)
        self.objectiveAdaptation = int(binStr,2) # Real Number to pass on Objective Function
        self.fitness = 0;
    
    def getBody(self):
        return self.body
    
    def calcFitness(self,fitness):
        pass

    def copy(self,Chrom,num1,num2):
        pass
    
    def mutate(self):
        pass
    
    # Getters and Setters
    def getLarge(self):
        return self.large
    
    def setLarge(self,large):
        self.large = large
    
    def getObjectiveAdaptation(self):
        return self.objectiveAdaptation
    
    def setObjectiveAdaptation(self,objectiveAdaptation):
        self.objectiveAdaptation = objectiveAdaptation
    
    def getFitness(self):
        return self.fitness
    
    def setFintess(self,fitness):
        self.fitness = fitness
    