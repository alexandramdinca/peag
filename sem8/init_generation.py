import numpy as np

#fitness function
# I: x - the individual (permutation) being evaluated
#c - costs matrix
def foTSP(p,c):
    n=p.size
    cost=c[p[0]][p[-1]]+sum([c[p[i]][p[i+1]] for i in range(n-1)])
    return 100/cost

# generates the initial population
# I:
# c - costs matrix
# dim - number of individuals in the population
# O: pop - initial population and vector of qualities


def gen(c,dim):
    n=c.shape[0]
    population=np.zeros([dim,n],dtype="int")
    values=np.zeros(dim)
    for i in range(dim):
       population[i]=np.random.permutation(n)
       values[i] = foTSP(population[i],c)
    return population, values




