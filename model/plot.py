import matplotlib.pyplot as plt
import sys
import numpy as np
import math as mt
sys.path.insert(0, '../model')

# user made models
# import host
# import package
# import router
import utils

## AREA DESCRIPTION ##

hosts_quantity = 5

# values below corresponds to a measurement in kilometers
width = 15
height = 15

# get arrays containing coordinates
x, y = utils.generate_coordinates(hosts_quantity, width, height)

# static host positions for testing purposes
# x = [1, 5, 6, 9]
# y = [1, 6, 3, 5]

# figure dimensions
plt.axis([0, width, 0, height])

# figure labels
plt.xlabel("in Km")
plt.ylabel("in Km")

# plotting triangles
plt.plot(x, y, 'k^')

# plotting hosts names
for i in range(hosts_quantity):
    plt.annotate(i, (x[i]+0.1, y[i]+0.1))

print("em x:",x ,"em y:" ,y) 

for j in range(hosts_quantity - 1):
    for k in range(hosts_quantity - 1):
        a = abs(x[j+1] - x[k])
        b = abs(y[j+1] - y[k])
        h = mt.sqrt(mt.pow(a,2) + mt.pow(b,2))
    
        if(h<=3.3 and h != 0):
            print(x[j+1],y[j+1]," Está no alcance de ", x[k],y[k])
        #else:
           # print(x[j],y[j]," Não está no alcance de ", x[k+1],y[k+1])

#plot the circles with a fixed area of 25000, what results in a Radius of 3.2 aprox.
r = mt.sqrt((25000/np.pi))
print(r)
area = np.pi * (r*r)
print(area)

# plotting estimated area coverage
plt.scatter(x, y, s=area, alpha=0.11)

# plt.arrow(x[1], y[1], x[2]-x[1], y[2]-y[1])

plt.show()