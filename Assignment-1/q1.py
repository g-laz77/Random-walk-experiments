import random
import matplotlib.pyplot as py
import operator as op
import functools

# import plotly.graph_objs as go
N = list(range(0, 100))
probs = []
theoretical = []
# Create random data with numpy
import numpy as np

def combinatorics(n, r):
    r = min(r, n - r)
    if r == 0:
        return 1
    numb = functools.reduce(op.mul, range(n, n - r, -1))
    den = functools.reduce(op.mul, range(1, r + 1))
    return numb // den

number = input("Enter max number of steps per drunk:")
tc = input("Enter number of testcases: ")
for n in range(int(number)):
    origin = 0
    for i in range(int(tc)):
        one_x = 0
        two_x = 0
        for j in range(0,n):
            temp = random.uniform(0,1)
            if temp > 0.5:
                one_x += 1
            else:
                one_x -= 1

        for j in range(0,n):
            temp1 = random.uniform(0,1)
            if temp1 > 0.5:
                two_x += 1
            else:
                two_x -= 1
    
        if one_x == two_x:
            origin += 1

    probability = float(origin)/5000
    print(probability)
    probs.append(probability)
    up = combinatorics(2 * n, n)
    down = 4 ** n
    theoretical.append(float(up) / float(down))

l1 = py.plot(N, probs, label='Computational')
l2 = py.plot(N, theoretical, label='Analytical')
py.legend(loc='upper right')
py.plot(N,probs)
py.show()
