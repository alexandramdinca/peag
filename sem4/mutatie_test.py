import numpy as np
from Mutation_functions import m_permutation_inversion
import matplotlib.pyplot as grafic

#fitness function
def foTSP(p,c):
    n=p.size
    cost=c[p[0]][p[-1]]+sum([c[p[i]][p[i+1]] for i in range(n-1)])
    return 100/cost

#initial population generation function
def gen(c,dim):
    n=c.shape[0]
    population=np.zeros([dim,n],dtype="int")
    values=np.zeros(dim)
    for i in range(dim):
       population[i]=np.random.permutation(n)
       values[i] = foTSP(populatie[i],c)
    grafic.plot(values,"gs",markersize=11,label="Initial")
    return population, values


#MUTATION
#mutation operation of the children resulting from crossover operation

    # I: po,vo - population of children and their qualities array (list)
    #   dim,n - dimension of population / size of an individual
    #    pm - mutation probability
    #    c - the costs matrix
    # E: descm - [mpo,mvo] - the resulting individuals
def mutate_population(pchildren,vchildren,c,pm):
    mpo=pchildren.copy()
    mvo=vchildren.copy()
    dim=mpo.shape[0]
    n=mpo.shape[1]
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            x=mpo[i]
            y=m_permutation_inversion(x,n)
            mpo[i]=y
            mvo[i]=foTSP(y,c)
    grafic.plot(mvo, "rs", markersize=9,label="After mutation")
    return mpo,mvo

if __name__=="__main__":
    c=np.genfromtxt("costuri.txt")
    p,v=gen(c,14)
    o,vo=mutate_population(p,v,c,0.2)
    grafic.legend()
    grafic.show()