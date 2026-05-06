import numpy as np
import matplotlib.pyplot as graph
from crossover_operators_EN import PMX_crossover
from mutation_operators_EN import swap_mutation
from selection_mechanisms_EN import elitism, SUS, SUS_linear_rank

# objective function
def foTSP(p,c):
    n=p.size
    cost=c[p[0]][p[-1]]+sum([c[p[i]][p[i+1]] for i in range(n-1)])
    return 100/cost


# generates the initial population
# I:
#  fc - the name of the cost file
#  dim - the number of individuals in the population
# E: pop, val - the initial population and the fitness vector
def gen(c,dim):
    # n = problem size
    n = len(c)
    pop=np.zeros((dim,n),dtype=int)
    val=np.zeros(dim,dtype=float)
    for i in range(dim):
        # generate the candidate permutation with n elements
        pop[i] = np.random.permutation(n)
        # evaluate the candidate
        val[i] = foTSP(pop[i,:n],c)
    return pop, val



# crossover on the parent population pop, of size dim x n
# I: pop, valori, dim, n - as in the generation function
#    c - problem data
#    pc - crossover probability
# E: po, val - the offspring population, accompanied by fitness values
# asexual crossover is implemented
def crossover(pop,valori,c,pc):
    # initialize the offspring population, po, with a zero-element matrix
    dim,n=pop.shape
    po=np.zeros((dim,n),dtype=int)
    # initialize the fitness values of the offspring population, val, with a zero-element matrix
    val=np.zeros(dim,dtype=float)
    # the population is traversed so that 2 individuals are randomly selected - the matrix is accessed via a permutation of the row indices 0, 2, ..., dim-1
    pos=np.random.permutation(dim) # - linear rank
    # or the population is traversed so that 2 consecutive individuals are selected
    #pos=range(dim) # - to preserve order, FPS
    for i in range(0,dim-1,2):
        # select parents
        x = pop[pos[i]]
        y = pop[pos[i+1]]
        r = np.random.uniform(0,1)
        if r<=pc:
            # crossover x with y - PMX - suitable for adjacency-dependent problems
            c1,c2 = PMX_crossover(x,y,n)
            v1=foTSP(c1,c)
            v2=foTSP(c2,c)
        else:
            # asexual crossover
            c1 = x.copy()
            c2 = y.copy()
            v1=valori[pos[i]]
            v2=valori[pos[i+1]]
        # copy the result into the offspring population
        po[i] = np.copy(c1)
        po[i+1] = np.copy(c2)
        val[i]=v1
        val[i+1]=v2
    return po, val

# MUTATION
 # mutation operation on the offspring obtained from recombination
    # I: po, vo - the offspring population accompanied by the fitness vector
    #    dim, n - the dimensions
    #    pm - mutation probability
    #    c - the cost matrix
    # E: mpo, mvo - the resulting individuals, accompanied by fitness values
def mutation(po,vo,c,pm):
    mpo=po.copy()
    mvo=vo.copy()
    dim, n = po.shape
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            x=mpo[i]
            y=swap_mutation(x,n)
            mpo[i]=y
            mvo[i]=foTSP(y,c)
    return mpo,mvo


def show(sol,v):
    # TSP results visualization
    # I: x - the permutation that defines the arrangement
    # E: -
    n=len(sol)
    t=len(v)
    cost=min(v)
    print("Shortest computed distance: ",cost)
    print("A tour with cost ",cost," is: ",sol)
    x=[i for i in range(t)]
    y=[v[i] for i in range(t)]
    graph.plot(x,y,'ro-')
    graph.ylabel("Cost")
    graph.xlabel("Generation")
    graph.title("Fitness evolution of the best individual from each generation")
    graph.show()



## GENETIC ALGORITHM FOR SOLVING TSP
# I: fc - the file with the cost (distance) matrix
#    dim - the size of a population
#    NMAX - the maximum number of evolution simulations
#    pc - crossover probability
#    pm - mutation probability
#
# E: sol - the solution computed by the GA
#    val - 100 / maximum of the fitness function - minimum cost

def GA(fc,dim,NMAX,pc,pm):
    # read data from the n x n cost file
    c = np.genfromtxt(fc)
    # generating the population at the initial time step
    pop,qual=gen(c,dim)
    n=len(c)
    # initializations for the GA
    it=0
    ready=False
    # in istoric_v we store the best cost from the current population, at each step of the evolution
    istoric_v=[100/np.max(qual)]
    # evolution - while
    #                - NMAX has not been exceeded  and
    #                - the population has at least 2 individuals with different fitness values  and
    #                - in the last NMAX/3 iterations the best fitness has changed at least once
    nrm=1
    while it<NMAX and not ready:
        # PARENT SELECTION
        #1.
        spop, sval = SUS(pop, qual, dim, n)
        #2.
        #spop,sval=SUS_linear_rang(pop,qual,dim,n,1.5)
        # CROSSOVER
        kids,val_kids=crossover(spop,sval,c,pc)
        # MUTATION
        kidsm,val_kidsm=mutation(kids,val_kids,c,pm)
        # NEXT GENERATION SELECTION
        newpop,newval=elitism(pop,qual,kidsm,val_kidsm,dim)
        minimum=np.min(newval)
        maximum=np.max(newval)
        if maximum==100/istoric_v[it]:
            nrm=nrm+1
        else:
            nrm=0
        if maximum==minimum or nrm==int(NMAX/3):
            ready=True
        else:
            it=it+1
        istoric_v.append(100/np.max(newval))
        pop=newpop.copy()
        qual=newval.copy()
    i_sol = np.argmax(qual)
    sol=pop[i_sol]
    val=maxim
    show(sol,istoric_v)
    return sol,100/val

if __name__=="__main__":
    sol,val=GA("distante3.txt",200,300,0.8,0.2) # - minimum cost 29, values close to it are obtained
    sol,val=GA("costuri.txt",200,300,0.8,0.2) # - minimum cost 15, values close to it are obtained