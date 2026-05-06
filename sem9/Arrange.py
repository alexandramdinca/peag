import numpy as np
import matplotlib.pyplot as graph
from crossover_operators_EN import uniform_crossover, single_point_crossover
from mutation_operators_EN import bitflip_mutation
from selection_mechanisms_EN import elitism, SUS


# fitness function
def fitness(x,n,m):
    # objective function for the queens problem

    # I: x - the individual - binary string, m+n
    # E: c - fitness = 1/(1+cost), where cost accounts for incorrect arrangements

    cost=0
    if x[n+m-1]==0 and x[0]==1 and x[1]==0:
        cost+=1
    if x[n+m-2]==0 and x[n+m-1]==1 and x[0]==0:
        cost+=1
    for i in range(n+m-2):
        if x[i]==0 and x[i+1]==1 and x[i+2]==0:
            cost+=1
    cost+=abs(sum(x)-m)
    return 1/(1+cost)


# generates the initial population
# I:
#  n, m - number of dogs, number of cats
#  dim - the number of individuals in the population
# E: pop, cal - the initial population, the fitness vector
def gen(n,m,dim):
    # define an ndarray variable with all elements zero
    pop=np.zeros((dim,n+m),dtype=int)
    cal=np.zeros(dim)
    for i in range(dim):
        # generate the candidate permutation with n elements
        pop[i]=np.random.randint(0,2,n+m)
        cal[i]=fitness(pop[i],n,m)
    return pop, cal

# crossover on the parent population pop, of size dim x (n+m+1)
# I: pop, cal, n, m - as above
#    pc - crossover probability
# E: po, co - the offspring population, co the fitness vector
# asexual recombination is implemented
def crossover_population(pop,cal,n,m,pc):
    # initialize the offspring population, po, with the parent population
    po=pop.copy()
    co=cal.copy()
    dim,_=pop.shape
    # the population is traversed so that individuals 0,1 then 2,3 and so on are selected
    for i in range(0,dim-1,2):
        # select parents
        x = pop[i]
        y = pop[i+1]
        r = np.random.uniform(0,1)
        if r<=pc:
            #c1,c2 = uniform_crossover(x,y,n+m)
            c1, c2 = single_point_crossover(x, y, n+m)
            val1=fitness(c1, n, m)
            val2= fitness(c2, n, m)
            po[i]=c1.copy()
            co[i]=val1
            po[i+1]=c2.copy()
            co[i+1]=val2
    return po, co



# mutation on the offspring population
# I: pop, cal, n, m - as above
#    pm - mutation probability
# E: mpop, mcal - the mutated population, the fitness vector
def mutation_population(pop,cal,n,m,pm):
    mpop=pop.copy()
    mcal=cal.copy()
    dim, _ = pop.shape
    for i in range(dim):
        for k in range(m+n):
            # randomly determine whether mutation occurs
            if np.random.uniform(0,1) <= pm:
                # mutation
                mpop[i,k]=bitflip_mutation(mpop[i,k])
        mcal[i]=fitness(mpop[i],n, m)
    return mpop, mcal

# graph display
def show(sol,v):
    n=len(sol)
    t=len(v)

    x=[i for i in range(t)]
    graph.plot(x,v,'ro-')
    graph.ylabel("Quality")
    graph.xlabel("Generation")
    graph.title("Evolution of the best individual over time")
    graph.show()



## GENETIC ALGORITHM
# I: n, m - problem size
#    dim - the size of a population
#    NMAX - the maximum number of evolution simulations
#    pc - crossover probability
#    pm - mutation probability
#
# E: sol - the solution computed by the GA
#    val - how good the solution is (val=1, val>.999999999)
def GA(n,m, dim,NMAX,pc,pm):
    # generating the population at the initial time step
    pop,cal=gen(n,m, dim)
    # initializations for the GA
    it=0
    ready=False
    maximum=np.max(cal)
    minimum=np.min(cal)
    if maximum==minimum:
        ready=True
    istoric_v=[maximum]
    # termination condition:
        # the maximum number of iterations, NMAX, has been exceeded OR
        # the population contains individuals with the same fitness OR
        # the maximum of the objective function, 1, has not been reached
    while it<NMAX and not ready and maximum<0.99999999 :
        # parent selection
        spop,sval=SUS(pop,cal,dim,n+m)
        # crossover
        pop_o,cal_o=crossover_population(spop,sval,n,m,pc)
        # mutation
        pop_mo, cal_mo=mutatie_population(pop_o,cal_o,n,m,pm)
        # next generation selection
        newpop,newval=elitism(pop,cal,pop_mo,cal_mo,dim)
        # updating the current population
        pop= newpop.copy()
        cal = newval.copy()
        minimum=np.min(newval)
        maximum=np.max(newval)
        # stop the evolution when all individuals in the population have the same fitness
        if maximum==minimum:
            ready=True
        else:
            it+=1
        istoric_v.append(maximum)

    i_sol=np.argmax(cal)
    sol=pop[i_sol]
    val=cal[i_sol]
    print(f"the computed solution {sol} has fitness {val}")
    show(sol,istoric_v)
    return sol, val

if __name__=="__main__":
    number_of_dogs=38
    number_of_cats=17
    sol,val=GA(number_of_dogs,number_of_cats,300,350,0.85,0.15)
    print(f"verification: {sum(sol)} vs {number_of_cats}")
    if fitness(sol,number_of_dogs,number_of_cats)<0.99999999:
        print("A correct arrangement was not obtained")
    else:
        print("Correct arrangement")
