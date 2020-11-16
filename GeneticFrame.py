from GNN import GNN
import glob
import os
import numpy as np


class GeneticFrame:

    filePath = ""
    dataSet = []
    genFrame = []
    activations = []


    def __init__(self, filePath):
        self.filePath = filePath
        self.createNetwork()

    def __init__(self):
        layer1 = np.random.normal(loc=0.0, scale=1.5, size=(6, 6))
        layer2 = np.random.normal(loc=0.0, scale=1.5, size=(6, 6))
        layer3 = np.random.normal(loc=0.0, scale=1.5, size=(6, 1))

        self.dataSet = [[layer1, layer2, layer3]]

        self.createNetwork()

    def createNetwork(self):

        if self.filePath == '':
            for network in self.dataSet:
                self.genFrame.append(GNN(network))
        else:
            self.parseText()
            for network in self.dataSet:
                self.genFrame.append(GNN(network))

    def parseText(self):
        files_path = os.path.join(self.filePath, '*.txt')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        f = open(files[0], "r")

        layer = []
        network = []
        count = 0
        family = []

        for line in f.readlines():


            if line[0] == "*":

                network.append(layer)
                layer = []
                count = count +1
            elif line[0] == "%":
                network.append(layer)
                layer = []
                family.append(network)
                network = []

            elif line[0].isdigit() or line[0] == '-':

                weights = line.split(",")
                weights = list(map(float, weights))
                layer.append(weights)
                count = count + 1
            else:

                print('Text file structure incorrect. Please fix line:',  count)

        #for x in self.dataSet:
         #   print(x)

    def solve(self, inputs):
        #self.activations.append(self.genFrame[perceptronNumber].solve(inputs))
        for networks in self.genFrame:
           self.activations.append(networks.solve(inputs))
        print(self.activations)

    def getActivation(self):
        return self.activation

    #def setScore(self, score):
        #self.genFrame[perceptronNumber].setScore(score)
        #for i in range (0, self.genFrame):
        #   self.genFrame[i].setScore(score[i])
    def getScore(self, e):
        return e.getScore()


    def killPop (self):
        choppingBlock = 0
        self.genFrame.sort(key=self.getScore, reverse=True)
        self.printWeights()

    def getNetwork(self, networkNumber):
        return self.genFrame[networkNumber]

    def printWeights(self):
        for network in self.genFrame:
            network.printWeights()

    def getWeights (self):
        networks = []
        for network in self.genFrame:
            networks.append(network.getWeights())
        return networks

    # def saveWeights(self):
    #     data = self.getWeights(self)
    #     for network in data:
    #         for layer in network:
    #             for perceptron in layer:
    #                 # save line of weights
    #         # add a $
    #     # add a


