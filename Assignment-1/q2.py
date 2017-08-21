import random
import math
import matplotlib.pyplot as py

num_drunk = input("Enter number of drunk guys:") # 50
num_steps = input("Enter number of steps:") # radius = 1
radius = input("Enter radius: ")
counter = 0
radius_dict = {}

dicts = [{'x':0,'y':0,'z':0} for k in range(int(num_drunk))]
filename = open("output.xyz","w+")

for n in range(int(num_steps)):
    if n%10 == 0:
        filename.write("100\nSTEP\t\t"+str(n/10+1)+"\n")
    for j in range(0,int(num_drunk)):
        a_vec = random.uniform(-1*int(num_steps),int(num_steps))
        b_vec = random.uniform(-1*int(num_steps),int(num_steps))
        c_vec = random.uniform(-1*int(num_steps),int(num_steps))
        vec_mod = math.sqrt((a_vec-dicts[j]['x'])*(a_vec-dicts[j]['x']) + (b_vec-dicts[j]['y'])*(b_vec-dicts[j]['y']) + (c_vec-dicts[j]['z'])*(c_vec-dicts[j]['z']))
        tem1 = (dicts[j]['x']-a_vec)/vec_mod
        tem2 = (dicts[j]['y']-b_vec)/vec_mod
        tem3 = (dicts[j]['z']-c_vec)/vec_mod
        dicts[j]['x'] += tem1
        dicts[j]['y'] += tem2
        dicts[j]['z'] += tem3
        if n%10 == 0:
            temp = ""
            temp = "He\t" + str(dicts[j]['x']) + "\t" + str(dicts[j]['y']) + "\t" + str(dicts[j]['z']) + "\n"
            filename.write(temp)
            


    square_mod = math.pow(dicts[j]['x'],2)+math.pow(dicts[j]['y'],2)+math.pow(dicts[j]['z'],2)
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
