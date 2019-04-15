#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot
# import math
# import numpy as np

# pyplot.plot(x1,y1,'b-',x2,y2,'r-',x3,y3,'g-')
# pyplot.legend('value 1', 'value 2', 'value 3')


class Graphic(object):
    def __init__(self, graphicsData, iterationLimit):
        self.maxValues = graphicsData['maxValues']
        self.maxOPs = graphicsData['maxOPs']
        self.averageOPs = graphicsData['averageOPs']
        self.generations = []
        for i in range(iterationLimit):
            self.generations.append(i)
        # pyplot.ion()

    # Show one Plot with all Graphs
    def showPlots(self):
        # with pyplot.style.context(('dark_background')):
        self.drawAll(self.maxValues, self.generations, "Valor Máximo", "Generación", "VALORES MÁXIMOS", 221, False)
        self.drawAll(self.maxOPs, self.generations, "Puntuación Objetiva", "Generación", "PUNTUACIÓN OBJETIVA MÁXIMA", 222, True)
        self.drawAll(self.averageOPs, self.generations, "Puntuación Objetiva", "Generación", "PUNTUACIÓN OBJETIVA PROMEDIO", 212, True)
        pyplot.show()  # Draw all the "Subplots"

    # Show one Graph in each Plot
    def showPlotsApart(self):
        self.draw(self.maxValues, self.generations, "Valor Máximo", "Generación", "VALORES MÁXIMOS", False)
        self.draw(self.maxOPs, self.generations, "Puntuación Objetiva", "Generación", "PUNTUACIÓN OBJETIVA MÁXIMA", True)
        self.draw(self.averageOPs, self.generations, "Puntuación Objetiva", "Generación", "PUNTUACIÓN OBJETIVA PROMEDIO", True)

    # Generate one Subplot for every Graph (and Show all Graphs)
    def drawAll(self, axisY, axisX, labY, labX, title, region, axisData):
        pyplot.subplot(region)
        if axisData:
            pyplot.axis([-1, len(self.generations), 0, 1])
        pyplot.grid(True)
        pyplot.plot(axisX, axisY)
        pyplot.ylabel(labY)
        pyplot.xlabel(labX)
        pyplot.title(title)

    # Generate one plot for every Graph
    def draw(self, axisY, axisX, labY, labX, title, axisData):
        if axisData:
            pyplot.axis([-1, len(self.generations), 0, 1])
        pyplot.grid(True)
        pyplot.plot(axisX, axisY)
        pyplot.ylabel(labY)
        pyplot.xlabel(labX)
        pyplot.title(title)
        pyplot.show()
