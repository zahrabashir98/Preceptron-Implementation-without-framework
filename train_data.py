import numpy as np
import csv
from perceptron import Perceptron

training_inputs = []
labels = []

with open("data.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        training_inputs.append(np.array([float(row[0]),float(row[1])]))
        labels.append(float(row[2]))

    # cast to numpy array
    lables = np.array(labels)

    # print checks
    # for t,l in zip(training_inputs,labels):
    #     print(t)
    #     print(l)


perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)

for i in training_inputs:
    inputs = np.array([i[0],i[1]])
    result = perceptron.predict(inputs)
    print(result)


# inputs = np.array([0, 1])
# perceptron.predict(inputs) 

