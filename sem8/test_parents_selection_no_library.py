# script for the test of parents selection - SUS selection with FPS with sigma scaling (no library)
import numpy as np
import init_generation as gi
import matplotlib.pyplot as graph

def sigma_scaling_prob_calculation(qualities):
    dimension=qualities.size
    prob=qualities/sum(qualities)
    average=np.mean(qualities)
    dev=np.std(qualities)
    qualities_sigma=np.array([max(qualities[i]-(average-2*dev),0) for i in range(dimension)])
    if sum(qualities_sigma)==0:
        p=prob.copy()
    else:
        sigma_prob = qualities_sigma / sum(qualities_sigma)
        p=sigma_prob.copy()
    cumulated=p.copy()
    for i in range(1,dimension):
        cumulated[i]=cumulated[i-1]+p[i]
    return cumulated

def SUS(pop,qual,dim):
    spop=pop.copy()
    squal=np.zeros(dim)
    qfps=sigma_scaling_prob_calculation(qual)
    r=np.random.uniform(0,1/dim)
    k,i=0,0
    while (k<dim):
        while (r<=qfps[i]):
            spop[k]=pop[i].copy()
            squal[k]=qual[i]
            r=r+1/dim
            k=k+1
        i=i+1
    return spop, squal


# random generation of a population
dim=12
c=np.genfromtxt("costuri.txt")

p,v=gi.gen(c,dim)
# the calculation of parents and their qualities using SUS with FPS with sigma scaling
parents,values=SUS(p,v,dim)

# print(p)
# print(parents)

print(f"Qualities of current population {v}")
print(f"Qualities of parent population {values}")

graph.plot(v,"go",markersize=16,label='Qualities of current population')
graph.plot(values,"ro",markersize=10,label='Qualities of parent population')
graph.legend()
graph.show()