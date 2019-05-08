#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


class Chromosome(object):
    # Class Attribute (Constant)
    # coef = random.randint(1, 230 - 1)
    coef = (2**30)-1  # (2^30)-1

    # Constructor / Instance Attributes
    def __init__(self, large, newBody):

        # Chromosome's Genes
        if newBody is None:
            self.body = []
            for _ in range(large):
                self.body.append(str((random.randint(0, 1))))
        else:
            self.body = newBody
        self.large = large
        # Initialize Objective Function Punctuation and Fitness
        self.setObjectivePunctuation()
        self.fitness = 0

    # Show All Genes of the Chromosome
    def getBody(self):
        return self.body

    def toBinInteger(self):
        str_bin_num = ''.join(str(i) for i in self.body)

        return int(str_bin_num)

    # Real Number to pass on Objective Function
    def getRealValue(self):
        num = ''.join(str(i) for i in self.body)
        return int(num, 2)  # Convert body to String and then to Binary Int

    def calcObjPunc(self):
        return (self.getRealValue() / self.getCoef()) ** 2

    def calcFitness(self, totalObj):
        # if totalObj == 0: totalObj = 1  # Prevent Division by Zero Error
        self.fitness = (self.getObjectivePunctuation() / totalObj)  # Update Fitness
        return self.fitness

    # def copy(self, Chrom, num1, num2): pass
    # def mutate(self): pass

    # Class Methods
    @classmethod
    def getCoef(cls):
        return cls.coef

    @classmethod
    def setCoef(cls, coeficient):
        cls.coef = coeficient

    # Getters and Setters
    def getLarge(self):
        return self.large

    def setLarge(self, large):
        self.large = large

    def getObjectivePunctuation(self):
        return self.objectivePunctuation

    def setObjectivePunctuation(self):
        self.objectivePunctuation = self.calcObjPunc()

    def getFitness(self):
        return self.fitness

    def setFintess(self, fitness):
        self.fitness = fitness

    def copy(self, another_crom, start, end):
        for i in range(start, end):
            self.body[i] = (another_crom.body[i])
