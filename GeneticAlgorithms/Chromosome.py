#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Chromosome(object): 
    
    # Constructor / Instance Attributes
    def __init__(self, large):
        
        # Chromosome's Genes
        self.body = []
        for _ in range (large):
            self.body.append(str((random.randint(0,1))))
        
        # Initialize Objective Adaptation and Fitness
        binStr = ''.join(self.body)
        self.objectiveAdaptation = int(binStr,2)
        self.fitness = 0;
        
    # Getters and Setters 
    def getObjectiveAdaptation(self):
        return self.objectiveAdaptation
    
    def setObjectiveAdaptation(self,objectiveAdaptation):
        self.objectiveAdaptation = objectiveAdaptation
    
    def getFitness(self):
        return self.fitness
    
    def setFintess(self,fitness):
        self.fitness = fitness
    
    def getBody(self):
        return self.body
    