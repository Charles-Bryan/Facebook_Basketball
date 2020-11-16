
class Children:

    survivors = 0
    score = 0
    network = []
    def __init__ (self, network, survivors):
        self.network = network
        self.survivors = survivors


    def setScore(self, score):
        self.score = score

    def getLayerQty(self):
        return len(self.network)

    def getLayerSize(self):
        return len(self.network)

    def getPerceptronSize(self):
        return len(self.network[0])

    def printChild(self):
        print(self.network)

    def getChild(self):
        return self.network

    def getLayerQty(self):
        return len(self.network)

    def getLayerSize(self):
        return len(self.network[0])

    def getWeightQty(self):
        return len(self.network[0][0])

    def getScore(self):
        return self.score