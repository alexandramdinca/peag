import numpy as np

# FUNCTIONS FOR PARENT SELECTION
# INPUT/SELECTED POPULATION - SPECIFIED BY A MATRIX AND A QUALITY VECTOR - for general representation scenarios


# TOURNAMENT SELECTION for k individuals
# tournament selection - selects dim individuals
# I: pop, qual, dim, n, k - population matrix, quality vector, pop - dim x n, qual - dim, number of individuals entering the competition
# O: spop, squal - selected population along with the quality values of its members
def tournament(pop,qual,dim,n,k):
    spop=pop.copy()
    squal=np.zeros(dim)
    for it in range(dim):
        # selection of one individual at iteration it
        # generate k random indices in poz
        poz=np.random.randint(0,dim,k)
        # quality values entering the competition
        v=[qual[poz[i]] for i in range(k)]
        M=max(v)
        p=np.where(v==M)
        # imax = first position in v where the maximum value is reached
        imax=p[0][0]
        # isel = the corresponding index in the population for imax
        isel=poz[imax]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal

# TOURNAMENT SELECTION for k individuals
# tournament selection - selects dimc<dim individuals
# I: pop, qual, dim, n, k - population matrix, quality vector, pop - dim x n, qual - dim, number of individuals entering the competition
# O: spop, squal - selected population along with the quality values of its members
def tournament_2(pop,qual,dim,dimc,n,k):
    spop=np.zeros([dimc,n])
    squal=np.zeros(dimc)
    for it in range(dimc):
        # selection of one individual at iteration it
        # generate k random indices in poz
        poz=np.random.randint(0,dim,k)
        # quality values entering the competition
        v=[qual[poz[i]] for i in range(k)]
        M=max(v)
        p=np.where(v==M)
        # imax = first position in v where the maximum value is reached
        imax=p[0][0]
        # isel = the corresponding index in the population for imax
        isel=poz[imax]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal


# ROULETTE AND SUS SELECTIONS

# compute the FPS probability distribution for a quality vector
# I: qual, dim - quality vector of size dim
# O: cumulative distribution qfps
def fps(qual,dim):
    fps=np.zeros(dim)
    # sum of all values in the qual vector
    sum=np.sum(qual)
    for i in range (dim):
        fps[i] = qual[i]/sum
    qfps=fps.copy()
    for i in range(1, dim):
        qfps[i]=qfps[i-1]+fps[i]
    return qfps

# FPS with sigma scaling
# I: qual, dim - quality vector of size dim
# O: cumulative distribution qfps
# if all elements in qual are equal, returns the standard FPS
def sigmafps(qual, dim):
    # mean of the qual vector
    med=np.mean(qual)
    # standard deviation of qual
    var=np.std(qual)
    # compute the sigma-scaled values: newq[i] = max(qual[i] - (med - 2*var)), i = 1...dim
    newq=[max(0,qual[i]-(med-2*var)) for i in range(dim)]
    # compute the distribution on the new vector
    if np.sum(newq)==0:
        qfps=fps(qual,dim)
    else:
        qfps=fps(newq,dim)
    return qfps


# compute the linear rank probability distribution for a quality vector
# I: dim - population size
#    s - selection pressure
# O: cumulative distribution qlr
def linear_rank(dim,s):
    # compute linear rank probabilities
    lr=[(2-s)/dim+2*(i+1)*(s-1)/(dim*(dim+1)) for i in range(dim)]
    # compute cumulative probabilities
    qlr=lr.copy()
    for i in range(1, dim):
        qlr[i]=qlr[i-1]+qlr[i]
    return np.array(qlr)

# roulette selection using the FPS distribution with sigma-scaling
# I: pop, qual, dim, n - population matrix, quality vector, pop - dim x n, qual - dim
# O: spop, squal - selected population along with the quality values of its members
def roulette(pop,qual,dim,n):
    spop=pop.copy()
    squal=np.zeros(dim)
    # uses FPS with sigma-scaling
    qfps=sigmafps(qual,dim)
    for it in range(dim):
        # selection of one individual at iteration it
        r=np.random.uniform(0,1)
        poz=np.where(qfps>=r)
        # isel = first position in qfps where the cumulative sum of the first isel elements exceeds r
        isel=poz[0][0]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal

# sort the population pop with quality vector qual in ascending order by quality
# I: pop, qual, dim - as above
# O: pops, quals - versions sorted by quality
def sort_pop(pop,qual):
    indici=np.argsort(qual)
    pops=pop[indici]
    quals=qual[indici]
    return pops,quals

# roulette selection using the rank distribution
# the input population is assumed to be sorted
# I: pop, qual, dim, n, s - population matrix, quality vector, pop - dim x n, qual - dim, selection pressure
# O: spop, squal - selected population along with the quality values of its members
def roulette_linear_rank(pop,qual,dim,n,s):
    spop=pop.copy()
    squal=np.zeros(dim)
    # uses rank selection
    qr=linear_rank(dim,s)
    for it in range(dim):
        # selection of one individual at iteration it
        r=np.random.uniform(0,1)
        poz=np.where(qr>=r)
        # isel = first position in qfps where the cumulative sum of the first isel elements exceeds r
        isel=poz[0][0]
        spop[it][:]=pop[isel][:]
        squal[it]=qual[isel]
    return spop, squal


# SUS selection using the linear rank distribution
# I: pop, qual, dim, n - population matrix, quality vector, pop - dim x n, qual - dim
# O: pop_s, qual_s - selected population along with the quality values of its members
def SUS_linear_rank(pop,qual,dim,n,s):
    pop,qual=sort_pop(pop, qual)
    spop=pop.copy()
    squal=np.zeros(dim)
    # uses FPS with sigma-scaling
    qfps=linear_rank(dim,s)
    r=np.random.uniform(0,1/dim)
    k,i=0,0
    while (k<dim):
        while (r<=qfps[i]):
            spop[k][:]=pop[i][:]
            squal[k]=qual[i]
            r=r+1/dim
            k=k+1
        i=i+1
    newp = np.random.permutation(dim)
    pop_r = spop[newp]
    qual_r = squal[newp]
    return pop_r, qual_r

# SUS selection using the FPS distribution with sigma scaling
# I: pop, qual, dim, n - population matrix, quality vector, pop - dim x n, qual - dim
# O: spop, squal - selected population along with the quality values of its members
def SUS(pop,qual,dim,n):
    spop=pop.copy()
    squal=np.zeros(dim)
    # uses FPS with sigma-scaling
    qfps=sigmafps(qual,dim)
    r=np.random.uniform(0,1/dim)
    k,i=0,0
    while (k<dim):
        while (r<=qfps[i]):
            spop[k][:]=pop[i][:]
            squal[k]=qual[i]
            r=r+1/dim
            k=k+1
        i=i+1
    return spop, squal

# ELITIST SELECTION

# elitist selection
# I: pop_c, qual_c, pop_mo, qual_mo - current population and mutated offspring population on which selection is based, each accompanied by its quality vector
# O: pop, qual - resulting population and quality vector
def elitism(pop_c,qual_c,pop_mo,qual_mo,dim):
    pop=np.copy(pop_mo)
    qual=np.copy(qual_mo)
    max_c=np.max(qual_c)
    max_mo=np.max(qual_mo)
    if max_c>max_mo:
        p1=np.where(qual_c==max_c)
        # imax = first position in qual_c where the maximum value is reached
        imax=p1[0][0]
        ir=np.random.randint(dim)
        # replacement
        pop[ir]=pop_c[imax].copy()
        qual[ir]=max_c
    return pop,qual



# GENITOR selection
# I:
# pop_c, qual_c, pop_mo, qual_mo - current population and mutated offspring population on which selection is based, each accompanied by its quality vector
# dim, dimc - dimensions
# O: pop_r, qual_r - resulting population and quality vector
def genitor(pop_c,qual_c,pop_mo,qual_mo,dim,dimc):
    pops,quals=sort_pop(pop_c,qual_c)
    pop=pops.copy()
    qual=quals.copy()
    for i in range(dimc):
        pop[i]=pop_mo[i].copy()
        qual[i]=qual_mo[i]
    # to obtain populations with individuals in arbitrary order, shuffle
    newp=np.random.permutation(dim)
    pop_r=pop[newp]
    qual_r=qual[newp]
    return pop_r,qual_r

# deterministic selection
# I: pop_c, qual_c, pop_mo, qual_mo - current population and mutated offspring population on which selection is based, each accompanied by its quality vector
# dim, L - dimensions
# O: pop_r, qual_r - resulting population and quality vector
def sel_det(pop_c,qual_c,pop_mo,qual_mo,dim,L):
    pop=np.append(pop_c,pop_mo)
    pop.resize(2*dim,L)
    qual=np.append(qual_c,qual_mo)
    p,q=sort_pop(pop, qual)
    pop_1=p[dim:2*dim].copy()
    qual_1=q[dim:2*dim].copy()
    newp = np.random.permutation(dim)
    pop_r = pop_1[newp]
    qual_r = qual_1[newp]
    return pop_r,qual_r
