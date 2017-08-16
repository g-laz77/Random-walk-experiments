import random
import math
count=0
crad=0
def retCount(r,M,N):
    radcount = 0
    count1=0
    while(count1<N):
        x=0
        y=0
        z=0
        count=0
        while(count<M):
            a=0
            b=0
            c=0
            a=random.randint(-M,M)
            b=random.randint(-M,M)
            c=random.randint(-M,M)
            diffa = (x-a)
            diffb = (y-b)
            diffc = (z-c)
            totalabc = math.pow(diffa,2)+math.pow(diffb,2)+math.pow(diffc,2)
            troot = pow(totalabc,0.5)
            newa = (diffa)/troot
            newb = diffb/troot
            newc = diffc/troot
            x = x+newa
            y = y+newb
            z = z+newc
            count=count+1
        rsqr = math.pow(x,2)+math.pow(y,2)+math.pow(z,2)
        rroot = math.pow(rsqr, 0.5)
        if(int(rroot)==r):
            radcount = radcount + 1
        count1=count1+1
    return radcount

radcount = retCount(31,1000,5000)
print("B is ")
print(radcount)
