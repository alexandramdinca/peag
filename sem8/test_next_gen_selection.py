# script for the test of next generation selection - elitist
import numpy as np
from selection_mechanisms_EN import elitism
import init_generation as gi
import matplotlib.pyplot as graph


#random generation of two populations
dim=12
c=np.genfromtxt("costuri.txt")
p1,v1=gi.gen(c,dim)
p2,v2=gi.gen(c,dim)
generation,values=elitism(p1,v1,p2,v2,dim)
print('Population 1 with its qualities')
print(v1)
print('Population 2 with its qualities')
print(v2)
print('Selected:')
print(values)

# print(p1)
# print(p2)
# print(generation)

graph.plot(v1,"go",markersize=18,label='Current population')
graph.plot(v2,"bo",markersize=14,label='Descendants population')
graph.plot(values,"ro",markersize=10,label='Next generation')
graph.legend()
graph.show()

