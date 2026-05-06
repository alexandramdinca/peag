import numpy as np
import matplotlib.pyplot as grafic


#fitness function
def foNR(x):
    #objective function / fitness function for n queens problem

    # I: x - the evaluated individual (the permutation), n - the dimension of the problem
    # E: c - quality (the number of pairs of queens that do not attack each other)

    n=x.size
    c=len([(i,j) for i in range(n-1) for j in range(i+1,n) if abs(i-j)!=abs(x[i]-x[j])])

    return c

#generate the initial population
#I:
# n - the dimension of the problem
# dim - the number of individuals from the problem
#E: pop - the initial population
def gen(n,dim):
    #define an ndarray variable with all values being null
    pop=np.zeros((dim,n+1),dtype=int)
    for i in range(dim):
        #generate the candidate as a permutation with n elements
        pop[i,:n]=np.random.permutation(n)
        pop[i,n]=foNR(pop[i,:n])
    grafic.plot(pop[:,n], "go", markersize=11, label="Initial")
    return pop


#mutation by insertion inside a permutation
def mutation_insertion(p):
    n=p.size
    print(f"\n\n\nMutation in {p} with quality {foNR(p)}")
    p1=np.random.randint(0,n-1)
    p2=np.random.randint(p1+1,n)
    print(f"\nPositions are {p1+1} and {p2+1}")
    rez=p.copy()
    if p1+1<p2:
        inserted_element=p[p2]
        x=np.delete(p,p2)
        rez=np.insert(x,p1+1,inserted_element)
    print(f"\nResulted into individual {rez} with quality {foNR(rez)}")
    return rez



#mutation takes place on the children population
# I:pop,dim,n - population of dimension dim of x with (n+1) elements
#   pm - mutation probability
#E: - mpop - mutated population
def mutate_population(pop,dim,n,pm):
    mpop=pop.copy()
    for i in range(dim):
        #randomly generate r as the chance of mutation taking place
        r=np.random.uniform(0,1)
        if r<=pm:
            #mutation in individual i - by insertion
            x=mutation_insertion(mpop[i,:n],n)
            mpop[i,:n]=x.copy()
            mpop[i,n]=foNR(x)
    grafic.plot(mpop[:,n], "ro", markersize=7,label="After mutation")
    return mpop

if __name__=="__main__":
    p=gen(12,18)
    o=mutate_population(p,18,12,0.2)
    grafic.legend()
    grafic.show()


