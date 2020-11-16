
import LoadSave as ls

def rank(family):
    newlist = sorted(family, key=getScore, reverse=True)

def kill(rankedFamily):

    del rankedFamily[3:]

def nextEpoch(family):
    survivors = family[0].survivors
    # print(survivors)
    rankedFamily = sorted(family, key=getScore, reverse=True)
    del rankedFamily[survivors:]
    newFamily = crossover(rankedFamily)
    return newFamily

def crossover(parents):

#    assert len(parents) == 4, "Expecting 4 parents at this point"

    offspring = []
    for i in range(0, len(parents)):
        for j in range(0, i):
            babies = ls.makeBabies(parents[i], parents[j])
            for baby in babies:
                offspring.append(baby)
            # offspring.append(babies[0])
            # offspring.append(babies[1])
            # offspring.append(babies[2])
            # offspring.append(babies[3])

    return offspring

def getScore(e):
    return e.getScore()