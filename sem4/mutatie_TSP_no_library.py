import numpy as np
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


def mutation_inversion(p,c):
    n=p.size
    print(f"The initial individual {p}")
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    print(f"The positions used for the mutation are: {i} , {j}")
    r=p.copy()
    r[i:j+1]=[p[k] for k in range(j,i-1,-1)]
    print(f"The individual after mutation {r}\n")
    return r


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
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            x=mpo[i]
            y=mutation_inversion(x,c)
            mpo[i]=y
            mvo[i]=foTSP(y,c)
    grafic.plot(mvo,"rs",markersize=8,label="After mutation")
    return mpo,mvo

if __name__=="__main__":
    c=np.genfromtxt("costuri.txt")
    p,v=gen(c,14)
    o,vo=mutate_population(p,v,c,0.2)
    grafic.legend()
    grafic.show()