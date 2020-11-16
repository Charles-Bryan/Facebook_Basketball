#*************** Second Class *******************
import math
class OutputPerceptron:
    w1 = 0.0
    w2 = 0.0
    x1 = 0.0
    x2 = 0.0
    eta = 0.0
    delta = 0.0
    doutput = 0.0
    activity = 0
    output = 0
    delta = 0
    bias = 0
    biasInput = 0

    def __init__(self, w1, w2, eta, bias):
        import math
        self.w1 = w1
        self.w2 = w2
        self.eta = eta
        self.bias = bias


    def setActivation(self):
        self.activity = self.w1 * self.x1 + self.w2 * self.x2 + self.bias
        self. output = 1/(1 + math.exp(-1 * self.activity))

    def feedInputs(self, a, b):
        self.x1 = a
        self.x2 = b
        self.setActivation()
        self.setDelta()

    def setDelta(self):
        self.setActivation()
        self.delta = (self.doutput - self.output) * (1 - self.output) * self.output

    def updateWeights(self):
        self.setDelta()
        self.w1 = self.w1 + self.eta * self.delta * self.x1
        self.w2 = self.w2 + self.eta * self.delta * self.x2
        self.bias = self.bias + self.eta * self.delta * 1.0

    def getDelta(self):
        self.setDelta()
        return self.delta

    def getOutput(self):
        return self.output

    def updateDoutput(self, value):
        self.doutput = value

    def calcBigE(self):
        self.setActivation()
        bigE = .5 * (self.doutput - self.output) * (self.doutput - self.output)
        return bigE
