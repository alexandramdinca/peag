import numpy as np
import matplotlib.pyplot as graph
from crossover_operators_EN import OCX_crossover, CX_crossover
from mutation_operators_EN import insertion_mutation, swap_mutation
from selection_mechanisms_EN import elitism, roulette


# objective function for the N-Queens problem

# I: x - the individual (permutation) being evaluated, n - problem size
# E: c - fitness (number of pairs of queens that do not attack each other)
def foNR(x):
    n=x.size
    c=len([(i,j) for i in range(n-1) for j in range(i+1,n) if abs(i-j)!=abs(x[i]-x[j])])

    return c


# generates the initial population
# I:
#  n - the problem size
#  dim - the number of individuals in the population
# E: pop - the initial population
def gen(n,dim):
    # define an ndarray variable with all elements zero
    pop=np.zeros((dim,n+1),dtype=int)
    for i in range(dim):
        # generate the candidate permutation with n elements
        pop[i,:n]=np.random.permutation(n)
        pop[i,n]=foNR(pop[i,:n])
    return pop

# crossover on the parent population pop, of size dim x (n+1)
# I: pop, dim, n - as above
#    pc - crossover probability
# E: po - the offspring population
# asexual crossover is implemented
def crossover_population(pop,pc):
    # initialize the offspring population, po, with the parent population
    po=pop.copy()
    dim,n=pop.shape
    n-=1
    # the population is traversed so that individuals 0,1 then 2,3 and so on are selected
    for i in range(0,dim-1,2):
        # select parents
        x = pop[i,:-1]
        y = pop[i+1,:-1]
        r = np.random.uniform(0,1)
        if r<=pc:
            # crossover x with y - CX or OCX - suitable for N-Queens
            c1,c2 = OCX_crossover(x,y,n)
            val1=foNR(c1)
            val2= foNR(c2)
            po[i][:n]=c1.copy()
            po[i][n]=val1
            po[i+1][:n]=c2.copy()
            po[i+1][n]=val2
    return po



# mutation on the offspring population
# I: pop, dim, n - the population of dimensions dim x (n+1)
#    pm - mutation probability
# E: mpop - the mutated population
def mutation_population(pop,pm):
    mpop=pop.copy()
    dim, n = pop.shape
    n-=1
    for i in range(dim):
        # randomly determine whether mutation occurs
        r=np.random.uniform(0,1)
        if r<=pm:
            # mutation on individual i - by swap
            x=swap_mutation(mpop[i,:n],n)
            mpop[i,:n]=x.copy()
            mpop[i,n]=foNR(x)
    return mpop

## MUTATION


def show(sol,v):
    # visualization of queen placement on the chessboard

    # I: sol - the permutation that defines the placement
    #    v - the vector with the best fitness from each generation
    # E: -

    n=len(sol)
    t=len(v)
    minimum=min(v)
    t1="Fitness evolution (best individual from each generation).\nThe result "
    t2="Best queen placement found.\nThe result "
    t4="is optimal (" + str(minimum) + " vs 0" + ")"
    if minimum>0:
        t3="is not "
    else:
        t3=""
    titlu1 =t1+t3+t4
    titlu2=t2+t3+t4

    x=[i for i in range(t)]
    graph.plot(x,v,'ro-')
    graph.ylabel("Quality")
    graph.xlabel("Generation")
    graph.title(titlu1)

    fig=graph.figure()
    ax=fig.gca()
    y=[n-1-i+0.5 for i in range(n)]
    x=[sol[i]+0.5 for i in range(n)]
    graph.plot(x,y,'r*',markersize=10)
    graph.xticks(range(n+1))
    graph.yticks(range(n+1))
    graph.grid(True,which='both',color='k', linestyle='-', linewidth=1)
    ax.set_aspect('equal')
    graph.title(titlu2)
    graph.show()



## GENETIC ALGORITHM FOR SOLVING THE N-QUEENS PROBLEM
# I: n - the problem size
#    dim - the size of a population
#    NMAX - the maximum number of evolution simulations
#    pc - crossover probability
#    pm - mutation probability
#
# E: sol - the solution computed by the GA
#    val - the maximum of the fitness function - n*(n-1)/2 - number of pairs of queens in attacking positions
def GA(n,dim,NMAX,pc,pm):
    # generating the population at the initial time step
    pop=gen(n,dim)
    # initializations for the GA
    it=0
    ready=False
    maximum=np.max(pop[:,n])
    istoric_v=[n*(n-1)//2-maximum]
    # termination condition:
        # the maximum number of iterations, NMAX, has been exceeded OR
        # the population contains individuals with the same fitness OR
        # the maximum of the objective function, n*(n-1)/2, has not been reached
    while it<NMAX and not ready and maximum<n*(n-1)//2 :
        # parent selection
        spop,sval=roulette(pop[:,:n],pop[:,n],dim,n)
        # appending sval as the last column of spop
        pop_s=np.hstack((spop,sval.reshape(-1,1)))
        # crossover
        pop_o=crossover_population(pop_s,pc)
        # mutation
        pop_mo=mutation_population(pop_o,pm)
        # next generation selection
        newpop,newval=elitism(pop[:,:n],pop[:,n],pop_mo[:,:n],pop_mo[:,n],dim)
        # updating the current population
        pop[:, :n] = newpop.copy()
        pop[:, n] = newval.copy()
        minimum=np.min(newval)
        maximum=np.max(newval)
        # stop the evolution when all individuals in the population have the same fitness
        if maximum==minimum:
            ready=True
        else:
            it+=1
        istoric_v.append(n*(n-1)//2-int(maximum))

    i_sol=np.argmax(pop[:,n])
    sol=pop[i_sol,:n]
    val=n*(n-1)//2-pop[i_sol,n]
    print(f"the computed solution {sol} has {val} placement errors")
    show(sol,istoric_v)
    return sol, val

if __name__=="__main__":
    sol,val=GA(14,120,500,0.85,0.15)
