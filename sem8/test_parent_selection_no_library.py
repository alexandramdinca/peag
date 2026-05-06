# script for testing parent selection - roulette selection with FPS distribution and sigma-scaling (no library)
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

def roulette(population,qualities,dim,n):
    parents=population.copy()
    parents_qualities=qualities.copy()
    cumulated=sigma_scaling_prob_calculation(qualities)
    for i in range(dim):
        r=np.random.uniform(0,1)
        poz=np.where(cumulated>=r)
        selected=poz[0][0]
        parents[i]=population[selected].copy()
        parents_qualities[i]=qualities[selected]
    return parents,parents_qualities


# random generation of a population
dim=8
n=10
p=gi.gen(n,dim)
# population p is split into the individual matrix and the quality vector
# computing parents and their quality values using roulette selection with sigma-scaled FPS
parents,values=roulette(p[:,:n],p[:,n],dim,n)
# constructing the resulting population
rez=np.zeros([dim,n+1],dtype='int')
rez[:,:n]=parents.copy()
rez[:,n]=values.copy()
print("Population considered to be current")
print(p)
print("Parent population")
print(rez)


x=[i for i in range(dim)]
graph.plot(x,p[:,n],"go",markersize=16,label='Qualities of current population')
graph.plot(x,rez[:,n],"ro",markersize=10,label='Qualities of parents')
graph.legend()
graph.show()

