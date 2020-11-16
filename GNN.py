import math

def solve(child, inputs):

    activations = []
    network = child.getChild()

    for layer in network:
        for perceptron in layer:

            activations.append(calcActivation(perceptron, inputs))
        if len(layer) == 1:
            answer = activations[0]
            return answer
        else:
            inputs = activations


def calcActivity(perceptron, inputs):
    activity = 0
    for i in range (0, len(perceptron)):
        if perceptron[i] == perceptron[-1]:
            activity = activity + perceptron[i] * 1
        else:
            activity = activity + perceptron[i] * inputs[i]
    return activity


def calcActivation(perceptron, inputs):
    activity = calcActivity(perceptron, inputs)
    activation = 1 / (1 + math.exp(-1 * activity))
    return activation
