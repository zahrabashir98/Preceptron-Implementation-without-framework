import numpy as np
import csv

import matplotlib.pyplot as plt
import numpy as np

# notice that you should run it only with python3
y = 0
b = 0.2
w1 = -0.5
w2 = -0.6
x1 = 0
x2 = 0
learning_rate = 0.1
error = 100

while(error>0.01):
    y = b + x1*w1 + x2*w2
    
    if x1 ==0 and x2==0:
        b = b + learning_rate*(1-y)
        w1 = w1 + learning_rate*(1-y) * x1
        w2 = w2 + learning_rate*(1-y) * x2
        error = learning_rate*(1-y)
        x1 = 1
        x2 = 0
        

    elif x1==1 and x2==0:
        b = b + learning_rate*(0-y)
        w1 = w1 + learning_rate*(0-y) * x1
        w2 = w2 + learning_rate*(0-y) * x2
        error =learning_rate*(0-y)
        x1 = 0
        x2 = 1

    elif x1==0 and x2==1:
        b = b + learning_rate*(0-y)
        w1 = w1 + learning_rate*(0-y) * x1
        w2 = w2 + learning_rate*(0-y) * x2
        error =learning_rate*(0-y)
        x1 = 1
        x2 = 1
    
    elif x1==1 and x2==1:
        b = b + learning_rate*(0-y)
        w1 = w1 + learning_rate*(0-y) * x1
        w2 = w2 + learning_rate*(0-y) * x2
        error =learning_rate*(0-y)
        x1 = 0
        x2 = 0
    print(b)
    print(w1)
    print(w2)