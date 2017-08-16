import random
import math
import matplotlib.pyplot as py

num_drunk = input("Enter number of drunk guys:") # 50
num_steps = input("Enter number of steps:") # radius = 1
radius = input("Enter radius: ")
counter = 0
radius_dict = {}

for n in range(int(num_drunk)):
    # origin = 0
    one_x = 0    
    one_y = 0
    one_z = 0
    for j in range(0,int(num_steps)):
        a_vec = random.uniform(-1*int(num_steps),int(num_steps))
        b_vec = random.uniform(-1*int(num_steps),int(num_steps))
        c_vec = random.uniform(-1*int(num_steps),int(num_steps))
        vec_mod = math.sqrt((a_vec-one_x)*(a_vec-one_x) + (b_vec-one_y)*(b_vec-one_y) + (c_vec-one_z)*(c_vec-one_z))
        tem1 = (one_x-a_vec)/vec_mod
        tem2 = (one_y-b_vec)/vec_mod
        tem3 = (one_z-c_vec)/vec_mod
        one_x += tem1
        one_y += tem2
        one_z += tem3

    square_mod = math.pow(one_x,2)+math.pow(one_y,2)+math.pow(one_z,2)
    mod = math.sqrt(square_mod)
    if int(mod) in radius_dict.keys():
        radius_dict[int(mod)] += 1
    else:
        radius_dict[int(mod)] = 1
    # if(int(mod) == int(radius)):
    #     counter += 1
key = radius_dict.keys()
grad = []
gnum = []
for i in range(len(key)):
    grad.append(key[i])
    gnum.append(radius_dict[key[i]])

py.plot(grad,gnum)
py.show()
print(counter)
