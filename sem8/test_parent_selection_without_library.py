# script for testing parent selection - tournament selection
import numpy as np
import init_generation as gi
import matplotlib.pyplot as graph
# for legend - adjusted display
# random generation of a population
def tournament(pop,cal,dim,k):
    parents=[]
    qualities=[]
    for i in range(dim):
        positions=np.random.randint(0,dim,k)
        multime_cal=[cal[positions[t]] for t in range(k)]
        index_individual=np.argmax(multime_cal)
        parents.append(pop[positions[index_individual]])
        qualities.append(cal[positions[index_individual]])
    return parents, qualities


dim=10
cmax=30
k=2
c=np.genfromtxt("cost.txt")
v=np.genfromtxt("valoare.txt")

L=gi.gen(c,v,cmax,dim)
pop=[L[i][:-1] for i in range(len(L))]
cal=[L[i][-1] for i in range(len(L))]

parents,values=tournament(pop,cal,dim,k)

# print(pop)
# print(parents)
graph.plot(cal,"go",markersize=16,label="Current population")
graph.plot(values,"ro",markersize=10,label="Parent population")
graph.legend()
graph.show()

