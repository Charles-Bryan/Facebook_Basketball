#************** The first class *****************
import math
class internalPerceptron:
    import math
    w1 = 0.0
    w2 = 0.0
    x1 = 0.0
    x2 = 0.0
    eta = 0.0
    delta = 0.0
    activity = 0
    output =0
    delta = 0.0
    bias = 0

    def __init__(self, w1, w2, eta, bias):
        self.w1 = w1
        self.w2 = w2
        self.eta = eta
        self.bias = bias

    def setActivation(self):
        self.activity = self.w1 * self.x1 + self.w2 * self.x2 + self.bias
        self.output = 1 / (1 + math.exp(-1 * self.activity))

    def feedInputs(self, a, b):
        self.x1 = a
        self.x2 = b
        self.setActivation()

    def calcDelta(self, outputWeight, outputDelta):
        #self.setActivation()
        self.delta = (1-self.output) * self.output * outputWeight * outputDelta

    def updateWeights(self, outputWeight, outputDelta):
        self.calcDelta(outputWeight, outputDelta)
        self.w1 = self.w1 + self.eta * self.delta * self.x1
        self.w2 = self.w2 + self.eta * self.delta * self.x2
        self.bias = self.bias + self.eta * self.delta * 1

    #
    def getDelta(self, outputWeight, outputDelta, input):
        #self.calcDelta(outputWeight, outputDelta, self.x1)
        return self.calcDelta(outputWeight, outputDelta, input)
        #return self.delta

    def getOutput(self):
        return self.output

    def getWeights(self):
        print(self.w1)
        print(self.w2)