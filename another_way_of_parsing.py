
data =''
with open ("data.txt") as datafile:
    data = datafile.read()
    data = data.splitlines()
    # print(data)
    
for d in data :
    d = d.split(',')
    training_inputs.append(np.array([float(d[0]),float(d[1])]))
    labels.append(float(d[2]))
# print checks
for t,l in zip(training_inputs,labels):
    print(t)
    print(l)


lables = np.array(labels)


perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)
