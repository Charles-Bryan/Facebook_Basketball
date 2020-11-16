import LoadSave as ls
import GNN
import numpy as np
import DarwinTasks as dt
import random

inputs = np.random.normal(loc=0.0, scale=1.5, size=(1,6))
inputs = inputs[0]

family = ls.createFamily(12, 3, 6, 6)
print('Test1')
for child in family:
    child.printChild()
ls.saveFamily(family, 'test.p')
family2 = ls.loadFamily(r'C:\Users\Matt\PycharmProjects\Neural\Facebook-Basketball-master')
print('test2')
for child in family:
    child.printChild()

print("----------inputs--------")
print(inputs)
answer = GNN.solve(family[0], inputs)
print("this is the answer")
print(answer)

for child in family:
    child.setScore(random.randint(1, 101))
newFamily = dt.nextEpoch(family, 12)
for child in newFamily:
    child.printChild()