import numpy as np
import matplotlib.pyplot as graph
import random
import copy
from crossover_operators_EN import singular_crossover, simple_crossover
from mutation_operators_EN import non_uniform_mutation
from selection_mechanisms_EN import elitism, roulette


# checks the feasibility of choice x and also computes the objective function
def ok(x,c,v,max):
    val=np.dot(x,v)
    cost=np.dot(x,c)
    return cost<=max,val


# generates the initial population
# I:
#  c, v - the cost and value vectors
#  max - the maximum capacity
#  dim - the number of individuals in the population
# E:
# pop - the population accompanied by fitness values

def gen(c,v,max,dim):
    # n = problem size
    n=v.size
    # work with the population as a list of dim elements - lists with n+1 individuals each
    pop=[]
    for i in range(dim):
        ready=False
        while ready == False:
            # generate the candidate x with elements 0, 1
            x=[random.uniform(0,1) for _ in range(n)]
            ready,val=ok(x,c,v,max)
        # found a feasible candidate solution, in list data type x
        # append the value
        x.append(val)
        # add the new individual with its objective function value to the population - add another list with n+1 elements as an element of the pop list
        pop.append(x)
    return pop




# crossover on the parent population pop
# I: pop - the parents accompanied by fitness values
#    c, v, max - problem data
#    pc - crossover probability
# E: po - the offspring population accompanied by fitness values
# asexual crossover is implemented
def crossover_population(pop,c,v,max,pc,alpha):
    dim=len(pop)
    n=c.size
    po=copy.deepcopy(pop)
    # the population is traversed so that individuals 0,1 then 2,3 and so on are selected
    for i in range(0,dim-1,2):
        # select parents
        x = copy.deepcopy(pop[i][:-1])
        y = copy.deepcopy(pop[i+1][:-1])
        r = np.random.uniform(0,1)
        if r<=pc:
            # crossover x with y - singular or simple: more suitable here
            c1,c2= crossover_singular(x ,y ,n,alpha)
            #c1, c2 = crossover_simplu(x, y, n, alpha)
            fez, val = ok(c1, c, v, max)
            if fez:
                po[i][:-1]=copy.deepcopy(c1)
                po[i][-1]=val
            fez, val = ok(c2, c, v, max)
            if fez:
               po[i+1][:-1]=copy.deepcopy(c2)
               po[i+1][-1]=val
    return po


# mutation on the offspring population
# I: pop - the offspring population accompanied by fitness values
#    pm - mutation probability
# E: mpop - the mutated population, fitness values included
def mutation_population(pop,c,v,max,pm,sigma):
    # copy the population into the result
    dim = len(pop)
    n = c.size
    mpop=copy.deepcopy(pop)
    for i in range(dim):
        # copy individual i from the input population into x
        x=copy.deepcopy(pop[i][:-1])
        for j in range(n):
            # randomly determine whether mutation occurs on individual i, gene j
            r=np.random.uniform(0,1)
            if r<=pm:
                # mutation
                x[j]=m_neuniforma(x[j],sigma,0,1)
        # the resulting individual possibly undergoes multiple mutations
        # if it is feasible, it is kept
        fez, val = ok(x, c, v, max)
        if fez:
            mpop[i][:-1]=copy.deepcopy(x)
            mpop[i][-1]=val
    return mpop


def show(sol,v):
    # continuous Knapsack results visualization
    n=len(sol)
    t=len(v)
    val=max(v)
    print("Best computed value: ",val)
    sol1=[float(f"{sol[i]:.3f}") for i in range(len(sol))]
    print("The corresponding choice is: ",sol1)
    fig=graph.figure()
    x=[i for i in range(t)]
    y=[v[i] for i in range(t)]
    graph.plot(x,y,'ro-')
    graph.ylabel("Value")
    graph.xlabel("Generation")
    graph.title("Fitness evolution of the best individual from each generation")
    graph.show()



## GENETIC ALGORITHM FOR SOLVING THE CONTINUOUS KNAPSACK PROBLEM
# I: fc, fv - the cost/value files
#    dim - the size of a population
#    NMAX - the maximum number of evolution simulations
#    pc - crossover probability
#    pm - mutation probability
#
# E: sol - the solution computed by the GA
#    val - the maximum of the fitness function

def GA(fc,fv,cmax,dim,NMAX,pc,pm,alpha, sigma):
    # generating the population at the initial time step
    c=np.genfromtxt(fc)
    v=np.genfromtxt(fv)
    pop=gen(c, v, cmax, dim)
    n = c.size
    # initializations for the GA
    it=0
    ready=False
    nrm=1
    # in istoric_v we store the best cost from the current population, at each step of the evolution
    istoric_v=[max([pop[i][-1] for i in range(dim)])]
    # evolution - while
    #                - NMAX has not been exceeded  and
    #                - the population has at least 2 individuals with different fitness values  and
    #                - in the last NMAX/3 iterations the best fitness has changed at least once
    while it<NMAX and not ready:
        # PARENT SELECTION
        # the roulette function is implemented on ndarray
        individuals = np.array([pop[i][:-1] for i in range(dim)])
        qual = np.array([pop[i][-1] for i in range(dim)])
        spop, sval = roulette(individuals, qual, dim, n)
        spop = spop.tolist()
        # CROSSOVER
        for i in range(dim):
            spop[i].append(sval[i])
        pop_o= crossover_populatie(spop,c, v, cmax, pc, alpha)
        # MUTATION
        pop_mo= mutatie_populatie(pop_o,c,v,cmax,pm, sigma)
        # NEXT GENERATION SELECTION
        # the elitism function is implemented on ndarray
        individuals = np.array([pop[i][:-1] for i in range(dim)])
        qual = np.array([pop[i][-1] for i in range(dim)])
        individuals_new = np.array([pop_mo[i][:-1] for i in range(dim)])
        qual_new = np.array([pop_mo[i][-1] for i in range(dim)])
        newpop, newval = elitism(individuals, qual, individuals_new, qual_new, dim)
        minimum=min(newval)
        maximum=max(newval)
        if maximum==istoric_v[it]:
            nrm=nrm+1
        else:
            nrm=1
        if maximum==minimum or nrm==int(NMAX/3):
            ready=True
        else:
            it=it+1
        istoric_v.append(max(newval))
        pop = copy.deepcopy(newpop.tolist())
        for i in range(dim):
            pop[i].append(newval[i])
    # the solution = the best individual from the last generation
    qual = [pop[i][-1] for i in range(dim)]
    best=max(qual)
    i_sol = np.argmax(qual)
    sol=pop[i_sol][:-1]
    show(sol,istoric_v)
    return sol,best


if __name__=="__main__":
    sol,val=GA("cost1.txt","valoare1.txt",50,500,800,0.8,0.1,0.3, 0.05)