import math

class Gperceptron:
        activity = 0
        activation = 0
        weights = []
        inputs = []

        def __init__(self, weights):
            self.weights = weights
            #print(weights)

        def getInputs(self, inputs):
            self.inputs = inputs

        def calcActivity(self):
            #print(self.weights)
            #print(self.inputs)
            for i in range (0, len(self.weights)):
                self.activity = self.activity + self.weights[i] * self.inputs[i]

        def calcActivation(self):
            self.calcActivity()
            self.activation = 1 / (1 + math.exp(-1 * self.activity))


        def printWeights(self):
            for value in self.weights:

                print(value)


        def solve(self, inputs):
            self.getInputs(inputs)
            self.calcActivation()

        def getActivation(self):
            return self.activation

        def printWeights(self):
            print(self.weights)

        def getWeights(self):
            return self.weights

