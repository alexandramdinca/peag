# script for testing next-generation selection - elitist selection
import numpy as np
#from selection_mechanisms_EN import elitism
import init_generation as gi
import matplotlib.pyplot as graph
import copy

def elitism(current_p,current_p_d,descendants,quals_descendants,dim):
    next_gen=copy.deepcopy(descendants)
    next_gen_quals=copy.deepcopy(quals_descendants)
    if max(current_p_d)>max(quals_descendants):
        max_index=np.argmax(current_p_d)
        replaced=np.random.randint(dim)
        next_gen[replaced]=copy.deepcopy(current_p[max_index])
        next_gen_quals[replaced]=current_p_d[max_index]
    return next_gen, next_gen_quals


# random generation of two populations
dim=12
cmax=30
c=np.genfromtxt("cost.txt")
v=np.genfromtxt("valoare.txt")

L1=gi.gen(c,v,cmax,dim)
L2=gi.gen(c,v,cmax,dim)
pop1=[L1[i][:-1] for i in range(len(L1))]
cal1=[L1[i][-1] for i in range(len(L1))]
pop2=[L2[i][:-1] for i in range(len(L2))]
cal2=[L2[i][-1] for i in range(len(L2))]
generation,valori=elitism(pop1,cal1,pop2,cal2,dim)


# print(pop1)
# print(pop2)
# print(generation)

graph.plot(cal1,"go",markersize=18,label="Current Population")
graph.plot(cal2,"bo",markersize=14,label="Mutated offspring population")
graph.plot(valori,"ro",markersize=11,label="Next generation")

graph.legend()
graph.show()

