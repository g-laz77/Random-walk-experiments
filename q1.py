import random
import matplotlib.pyplot as py
# import plotly.graph_objs as go
N = list(range(0, 100))
probs = []
# Create random data with numpy
import numpy as np
number = input("Enter max number of steps per drunk:")
tc = input("Enter number of testcases: ")
for n in range(number):
    origin = 0
    for i in range(tc):
        one_x = 0
        two_x = 0
        for j in range(0,lo):
            temp = random.uniform(0,1)
            if temp > 0.5:
                one_x += 1
            else:
                one_x -= 1

        for j in range(0,lo):
            temp1 = random.uniform(0,1)
            if temp1 > 0.5:
                two_x += 1
            else:
                two_x -= 1
    
        if one_x == two_x:
            origin += 1

    probability = float(origin)/5000
    print(probability)
    probs.append(N,probability)

py.plot(N,probs)
# N = 500
# random_x = np.linspace(0, 1, N)
# random_y = np.random.randn(N)

# Create a trace
# trace = go.Scatter(
#     x = N,
#     y = probs
# )

# data = [trace]

# py.iplot(data, filename='basic-line')

py.show()
