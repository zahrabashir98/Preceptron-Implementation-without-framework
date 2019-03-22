import numpy as np
import csv
import matplotlib.pyplot as plt


# notice that you should run it only with python3

class Perceptron(object):

    def __init__(self, no_of_inputs, learning_rate=0.5, bios_learning_rate=0.5):
        # self.threshold = threshold
        self.learning_rate = learning_rate
        self.bios_learning_rate = bios_learning_rate
        self.weights = [0.1,0.2,0.3]
           
    def getter(self):
        return self.weights

    def train(self, training_inputs, target):
        # print(training_inputs)
        group1_x  = training_inputs[0]
        x2 = training_inputs[1]
        b = self.weights[2]
        w1 = self.weights[0]
        w2 = self.weights[1]
        y = b + group1_x * w1 + x2 * w2

        if y > 0:
            y = 1.0
        else:
            y = 0.0
        
        self.weights[2] = b + self.bios_learning_rate * (target - y)
        self.weights[0] = w1 + self.learning_rate * (target - y) * group1_x
        self.weights[1] = w2 + self.learning_rate * (target - y) * x2
        return y


network = Perceptron(2)
training_inputs = []
label = []
group0_x = []
group0_y = []
group1_x = []
group1_y = []
epochs = 5000
num_of_miss = {}
accuracy_of_each_epoch = {}
miss = 0
for i in range(epochs):

    with open("data.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            training_inputs = [float(row[0]),float(row[1])]
            label = float(row[2])
            prediction = network.train(training_inputs, label)
            if prediction != label:
                miss += 1
    
            if label == 1.0:
                group1_x.append(float(row[0]))
                group1_y.append(float(row[1]))
            if label == 0.0:
                group0_x.append(float(row[0]))
                group0_y.append(float(row[1]))

        num_of_miss[i] = miss
        accuracy_of_each_epoch[i] = ((200-num_of_miss[i])/200)*100
        print("accuracy of epoch %d -----> %f "%(i,accuracy_of_each_epoch[i]))
        print("loss of epoch %d is %f "%(i,(((num_of_miss[i])/200.0)*100)))
        print()
        miss = 0

t = []
for i in range(epochs):
    # print(num_of_miss[i])
    t.append(float(num_of_miss[i])/200.0)

weights = network.getter()
w1 = weights[0]
w2 = weights[1]
b = weights[2]

# Create data
x_g0 = np.array(group0_x)
y_g0 = np.array(group0_y)
x_g1 = np.array(group1_x)
y_g1 = np.array(group1_y)
g0 = (x_g0,y_g0)
g1 = (x_g1, y_g1)
data = (g0, g1)

colors = ("blue", "red")
groups = ("Group1", "Group2")
 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30)

a = -w1 / w2
b = -b / w2
lineX = [-200, -60]
lineY = [-200 * a + b, -60 * a + b]

ax.plot(lineX, lineY)
plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()

# x = np.arange(0,epochs,1)
# z = np.array(t)
# markerline, stemlines, baseline = plt.stem(x, z, '-.')
# plt.title('error percentage durate all epochs')
# plt.setp(baseline, color='r', linewidth=2)


# plt.plot(x,z)
# plt.title("error percentage durate all epochs")
# ax = plt.axes()
# ax.plot(np.array(t))
X = np.linspace(0, epochs, len(t))
plt.plot(X, np.array(t))
# ax.yaxis.set_major_locator(plt.NullLocator())
# ax.xaxis.set_major_formatter(plt.NullFormatter())
plt.show()
