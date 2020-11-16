import pickle
import os
import glob
from Children import Children
import numpy as np
import random
import operator as op
from functools import reduce


def loadFamily(fileName):
    files_path = os.path.join(fileName, '*.p')
    files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
    return pickle.load(open(files[0], "rb"))


def createFamily (childrenQty, layerQty, layerSize, weightQty):

    survivors = childrenQty

    size = 60 * ncr(survivors, 2)
    family = []
    for j in range(0, int(size)):
        network = []

        for i in range(0, layerQty-1):
            bimodal_lower = np.random.normal(loc=-1.0, scale=3.0, size=(layerSize, weightQty+1))
            bimodal_upper = np.random.normal(loc=1.0, scale=3.0, size=(layerSize, weightQty+1))
            choice = np.random.randint(2, size=(layerSize, weightQty + 1)).astype(bool)
            network.append(np.where(choice, bimodal_lower, bimodal_upper))

        bimodal_lower = np.random.normal(loc=-1.0, scale=3.0, size=(1, weightQty+1))
        bimodal_upper = np.random.normal(loc=1.0, scale=3.0, size=(1, weightQty+1))
        choice = np.random.randint(2, size=(1, weightQty+1)).astype(bool)
        network.append(np.where(choice, bimodal_lower, bimodal_upper))

        family.append(Children(network, survivors))
    return family


def saveFamily(family, fileName):
    pickle.dump(family, open(fileName, "wb"))


def makeBabies(parent1, parent2):
    layers = len(parent1.network)
    result = []

    # Each run (of 5) generates a unique crossover pair based on the two parents
    # and a unique mutated pair based on the corresponding crossover pair.
    # 6 combinations from best 4 parents. 10 children per parent combination. Therefore 60 children per generation
    for i in range(0, 30):
        offspringM = []
        offspring = []
        for index in range(layers):
            temp_layer = []
            temp_mutant = []
            flattenedLayer1 = parent1.network[index].flatten('C')
            flattenedLayer2 = parent2.network[index].flatten('C')

            for element in range(len(flattenedLayer1)):

                temp_layer.append(np.random.normal(loc=flattenedLayer1[element], scale=1.5, size=1))
                temp_mutant.append(np.random.normal(loc=flattenedLayer2[element], scale=1.5, size=1))

            offspring.append(np.asarray(temp_layer).reshape(parent1.network[index].shape))
            offspringM.append(np.asarray(temp_mutant).reshape(parent1.network[index].shape))
        result.append(Children(offspring, parent1.survivors))
        result.append(Children(offspringM, parent1.survivors))
    return result


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def standardized(score1, score2):
    values = []
    while True:
        score1 -= 10
        score2 -= 10
        if score1 < 0 or score2 < 0:
            score1 += 10
            values.append(score1)
            score2 += 10
            values.append(score2)
            values.append(score1 + score2)
            break

    return values
