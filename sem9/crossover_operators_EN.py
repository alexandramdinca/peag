import numpy as np



# CROSSOVER FOR BINARY OR INTEGER VECTORS

# single-point crossover between x and y, vectors with n components
# I: x, y, n as above
# E: c1, c2 - the two offspring - with n components
def single_point_crossover(x,y,n):
    # randomly generate the crossover point, between 1 and n-1 to have an effect
    # position n holds the fitness
    i = np.random.randint(1,n-1)
    c1=x.copy()
    c2=y.copy()
    # selecting the segments that make up the first child
    c1[0:i] = x[0:i]
    c1[i:n] = y[i:n]
    # selecting the segments that make up the second child
    c2[0:i] = y[0:i]
    c2[i:n] = x[i:n]
    return c1,c2


# uniform crossover between x and y, vectors with n components
# I: x, y, n as above
# E: c1, c2 - the two offspring
def uniform_crossover(x,y,n):
    # initialize children with parent values
    c1=x.copy()
    c2=y.copy()
    # constructing the children
    for i in range(n):
        r = np.random.randint(0,2)
        # if r==1, swap alleles at position i
        if r == 1:
            c1[i] = y[i]
            c2[i] = x[i]
    return c1,c2



# CROSSOVER FOR PERMUTATIONS - a permutation of size n has elements 0, 1, ..., n-1
# PMX operator
# I: permutations x, y of size n
# E: resulting offspring c1, c2
def PMX_crossover(x,y,n):
    # generating the crossover segment
    pos=np.random.randint(0,n,2)
    while pos[0]==pos[1]:
        pos=np.random.randint(0,n,2)
    p1=np.min(pos)
    p2=np.max(pos)
    c1=PMX(x,y,n,p1,p2)
    c2=PMX(y,x,n,p1,p2)
    return c1,c2

# applies PMX on x, y of size n, with recombination segment (p1, p2)
def PMX(x,y,n,p1,p2):
    # initialize child - a vector with all elements -1 - values that are not in 0, ..., n-1
    c=-np.ones(n,dtype=int)
    # copy the common segment into child c
    c[p1:p2+1]=x[p1:p2+1]
    # analysis of the common segment - in permutation y
    for i in range(p1,p2+1):
        # placing allele a
        a=y[i]
        if a not in c:
            curent=i
            placed=False
            while not placed :
                b=x[curent]
                # poz = the position where b is found in y
                [poz]=[j for j in range(n) if y[j]==b]
                if c[poz]==-1 :
                    c[poz]=a
                    placed=True
                else:
                    curent=poz
    # z = the vector of alleles from y not yet copied into c
    z=[y[i] for i in range(n) if y[i] not in c]
    # poz - the vector of free positions in c - those with value -1
    poz=[i for i in range(n) if c[i]==-1]
    # copying the alleles not yet copied from y into c
    m=len(poz)
    for i in range(m):
        c[poz[i]]=z[i]
    return c


# OCX operator
# I: permutations x, y of size n
# E: resulting offspring c1, c2
def OCX_crossover(x,y,n):
    # generating the crossover segment
    pos=np.random.randint(0,n,2)
    while pos[0]==pos[1]:
        pos=np.random.randint(0,n,2)
    p1=np.min(pos)
    p2=np.max(pos)
    c1=OCX(x,y,n,p1,p2)
    c2=OCX(y,x,n,p1,p2)
    return c1,c2

# applies OCX on x, y of size n, with recombination segment (p1, p2)
def OCX(x,y,n,p1,p2):
    # copy the common segment into c2
    c2=[x[i] for i in range(p1,p2+1)]
    # compute z based on y: components starting from p2 to n and then from 0 to p2-1, excluding elements already copied
    z1=[y[i] for i in range(p2,n) if y[i] not in c2]
    z2=[y[i] for i in range(p2) if y[i] not in c2]
    z=np.append(z1,z2)
    # compute the final segment of the resulting individual - from z, indices 0 to n-p2
    c3=[z[i] for i in range(n-p2-1)]
    # compute the starting segment of the resulting individual - from z, indices n-p2 to len(z)
    c1=[z[i] for i in range(n-p2-1,len(z))]
    # compute child c
    c=np.append(c1,c2)
    c=np.append(c,c3)
    return c

# CX operator
# I: permutations x, y of size n - completed with fitness
# E: resulting offspring c1, c2
def crossover_CX(x,y,n):
    cycle=cycles(x,y,n)
    c1=x.copy()
    c2=y.copy()
    for i in range(n):
        cat, rest = np.divmod(cycle[i], 2)
        # alleles from even-numbered cycles are swapped
        # the first cycle is labeled 1
        if not rest:
            c1[i]=y[i]
            c2[i]=x[i]
    return c1,c2

# computation of cycles from
# I: x, y of size n
# in
# E: the cycle vector, where cycle[i] = the number of the cycle to which x[i] and y[i] belong
def cycles(x,y,n):
    # cycle number
    index=1
    cycle=np.zeros(n)
    ready=0
    while not ready:
        p=np.where(cycle==0)
        # if there is a gene not yet assigned to a cycle
        if np.size(p):
            i=p[0][0]
            a=x[i]
            cycle[i]=index
            b=y[i]
            while b!=a:
                r=np.where(x==b)
                j=r[0][0]
                cycle[j]=index
                b=y[j]
            index+=1
        else:
            ready=1
    return cycle


#EDGE CROSSOVER

# builds the edge table for permutations x and y of size n
def build_table(x,y,n):
    # create a list with n elements, all 0
    edges=[0]*n
    # for convenience, border x with the last/first element
    x1=np.zeros(n+2, dtype='int')
    x1[1:n+1]=x[:]
    x1[0]=x[n-1]
    x1[n+1]=x[0]
    y1 = np.zeros(n + 2, dtype='int')
    y1[1:n + 1] = y[:]
    y1[0] = y[n - 1]
    y1[n + 1] = y[0]
    for i in range(1,n+1):
        a=x1[i]
        r=np.where(y==a)
        j=r[0][0]+1
        # find the neighbors of a in x and y using x1 and y1, and store as sets for difference and intersection
        vx={x1[i-1],x1[i+1]}
        vy={y1[j-1],y1[j+1]}
        dx=vx-vy
        dy=vy-vx
        cxy=vx & vy
        # convert from set to list
        lcxy=list(cxy)
        dx=list(dx)
        dy=list(dy)
        # work with str type
        for j in range(len(lcxy)):
            lcxy[j]=str(lcxy[j])+'+'
        for j in range(len(dx)):
            dx[j]=str(dx[j])
        for j in range(len(dy)):
            dy[j]=str(dy[j])
        edges[a]=lcxy+list(dx)+list(dy)
    return edges

# deletes an element from a list - with unique keys, if it appears in the list
# otherwise, leaves the list unchanged
def delete(x,a):
    # search for occurrence - there can be only one
    p=[i for i in range(len(x)) if x[i]==a]
    if len(p):
        del(x[p[0]])
    return x

# chooses the allele to place, if lp has more than one value
def choose(lp,edges,n):
    dim=len(lp)
    # search if 'lp[k]+' exists in the edge table
    # compute list lengths, in case 'lp[k]+' is not found
    lliste=np.zeros(dim)
    ready=0
    k=0
    while k<dim and not ready:
        a=str(lp[k])+'+'
        i=0
        while i<n and not gata :
            l=edges[i]
            p=[j for j in range(len(l)) if l[j]==a]
            if len(p):
                ready=1
                allele=lp[k]
            else:
                p=[j for j in range(len(l)) if l[j]==str(lp[k])]
                i=i+1
                lliste[k]=len(l)
        if not ready:
            k=k+1
    if not ready:
        # compute the minimum length and for which alleles it is achieved
        x=[j for j in range(dim) if lliste[j]==min(lliste)]
        # choose the first allele with minimum length
        # if there are multiple, choose the first one
        allele=lp[x[0]]
    return allele

# ECX operator - Edge crossover
def ECX(x,y,n):
    edges=build_table(x,y,n)
    # the resulting permutation
    z=np.zeros(n, dtype='int')
    # initially choose the first allele - variant: randomly select ap in 0...n-1
    # lp - list of possible alleles
    # chosen - flag vector of chosen alleles
    chosen=np.zeros(n)
    lp=[x[0]]
    for i in range(n):
        print(edges)
        if len(lp)==0:
            # randomly choose an allele
            a=np.random.randint(n)
            while chosen[a]:
                a = np.random.randint(n)
        else:
            if len(lp)>1:
                a=alege(lp,edges,n)
            else:
                a=lp[0]
        # assign the chosen allele
        z[i]=a
        chosen[a]=1
        print(a)
        # delete the allele from the edge table
        for k in range(n):
            sterge(edges[k],str(a))
            sterge(edges[k],str(a)+'+')
        # choose the list of possibilities at the next step
        lp=[int(edges[a][i][0]) for i in range(len(edges[a]))]
    return z

# ECX CALL
#import numpy as np
#import FunctiiCrossoverIndivizi as c
#n=10
#x=np.random.permutation(n)
#y=np.random.permutation(n)
#z=c.ECX(y,x,10)


# CROSSOVER FOR REAL-VALUES VECTORS

# single crossover between x and y, vectors with n components of type ndarray
# I: x, y, n as above
#    alpha - weight for averaging
# E: c1, c2 - the two offspring - without evaluation
def singular_crossover(x, y, n,alpha):
    # randomly generate the gene where recombination is performed
    i = np.random.randint(0,n)
    c1 = x.copy()
    c2 = y.copy()
    c1[i]=(alpha*x[i]+(1-alpha)*y[i])
    c2[i] = (alpha * y[i] + (1 - alpha) * x[i])
    return c1, c2


# simple crossover between x and y, vectors with n components - of type ndarray
# I: x, y, n as above
#    alpha - weight for averaging
# E: c1, c2 - the two offspring
def simple_crossover(x, y, n,alpha):
    # randomly generate the gene starting from which recombination is performed
    i = np.random.randint(0,n)
    c1 = x.copy()
    c2 = y.copy()
    for j in range(i,n):
        c1[j]=(alpha*x[j]+(1-alpha)*y[j])
        c2[j] = (alpha * y[j] + (1 - alpha) * x[j])
    return c1, c2

# total crossover between x and y, vectors with n components
# I: x, y, n as above
#    alpha - weight for averaging
# E: c1, c2 - the two offspring - without evaluation
def total_crossover(x, y, n,alpha):
    c1 = x.copy()
    c2 = y.copy()
    for j in range(n):
        c1[j]=(alpha*x[j]+(1-alpha)*y[j])
        c2[j] = (alpha * y[j] + (1 - alpha) * x[j])
    return c1, c2
