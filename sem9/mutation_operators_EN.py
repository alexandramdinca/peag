import numpy as np

## MUTATION FUNCTIONS LIBRARY

# NOTE! ALL EVALUATIONS OF RESULTING INDIVIDUALS WILL BE PERFORMED BY THE CALLER

# BINARY VECTORS
# bitflip mutation

# I: x - the value to be modified
# E: y - the result of the mutation
def bitflip_mutation(x):
    y=not x
    return int(y)


# INTEGER VECTORS
# random reset

# I: a, b - the reset is performed on the set a, a+1, ..., b-1
# E: y - the new value
def random_reset(a,b):
    y=np.random.randint(a,b)
    return y

# creep mutation

# I: x - the value to be modified
#    a, b - the bounds within which the output y must fall, a variant of x modified by one unit
# E: y - as above
def creep_mutation(x,a,b):
    # generate +1 or -1
    p=np.random.randint(0,2)
    if p==0:
        sign=-1
    else:
        sign=1
    y=x+sign
    if y>b:
        y=b
    if y<a:
        y=a
    return y

# REAL-VALUED VECTORS
# uniform mutation

# I: a, b - the interval in which the reset is performed
# E: y - the new value
def uniform_mutation(a,b):
    y=np.random.uniform(a,b)
    return y

# non-uniform mutation

# I: x - the value to be modified
#    sigma - the creep step
#    a, b - the bounds within which the output y must fall
# E: y - as above
def non_uniform_mutation(x,sigma,a,b):
    # generate noise
    p=np.random.normal(0,sigma)
    y=x+p
    if y>b:
        y=b
    if y<a:
        y=a
    return y


# PERMUTATIONS
# inversion mutation of permutation x with n components

# I: x, n
# E: y - the resulting permutation
def inversion_mutation(x,n):
    # generating positions for inversion
    pos = np.random.randint(0, n, 2)
    while pos[0] == pos[1]:
        pos = np.random.randint(0, n, 2)
    p1 = np.min(pos)
    p2 = np.max(pos)
    y=x.copy()
    y[p1:p2+1]=[x[i] for i in range(p2,p1-1,-1)]
    return y


# swap mutation of permutation x with n components

# I: x, n
# E: y - the resulting permutation
def swap_mutation(x,n):
    # generating positions for swap
    pos = np.random.randint(0, n, 2)
    while pos[0] == pos[1]:
        pos = np.random.randint(0, n, 2)
    p1 = np.min(pos)
    p2 = np.max(pos)
    y=x.copy()
    y[p1]=x[p2]
    y[p2]=x[p1]
    return y


# insertion mutation of permutation x with n components
# I: x, n
# E: y - the resulting permutation
def insertion_mutation(x,n):
    # generating positions for insertion
    pos = np.random.randint(0, n, 2)
    while pos[0] == pos[1]:
        pos = np.random.randint(0, n, 2)
    p1 = np.min(pos)
    p2 = np.max(pos)
    y=x.copy()
    y[p1+1]=x[p2]
    if p1<n-2:
        y[p1+2:n]=np.array([x[i] for i in range(p1+1,n) if i != p2])
    return y

def shuffle_mutation(x,n):
    #generation of the positions for the shuffle
    pos = np.random.randint(0, n, 2)
    while pos[0] == pos[1]:
        pos = np.random.randint(0, n, 2)
    p1 = np.min(pos)
    p2 = np.max(pos)
    y=x.copy()
    y[p1:p2+1] = np.random.permutation(x[p1:p2+1])
    #np.random.shuffle(y[p1:p2+1])
    return y