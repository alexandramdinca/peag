import numpy as np

## Library for mutation functions

#Notice! All the evaluations of the resulting individuals will be made by the calling function

#BINARY ARRAYS
#bitflip mutation

#I: x - the value that gets changed
#E: y - the resulting value of the mutation
def m_binary(x):
    y=not x
    return int(y)


#INTEGER ARRAYS
#random reset

#I:a,b - the reset takes place with values from the set a, a+1,...,b-1
#E: y - the new value
def m_rr(a,b):
    y=np.random.randint(a,b)
    return y

#creep mutation

#I: x - the value to be changed
#   a,b - the limits within which the new value must be included in
#E:y - the new value
def m_creep(x,a,b):
    #generate +1 or -1
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

#REAL NUMBERS ARRAYS
#uniform mutation

#I:a,b - the interval on which the reset is being made
#E: y - the new value
def m_uniform(a,b):
    y=np.random.uniform(a,b)
    return y

#non-uniform mutation

#I: x - the value to change
#   sigma - the step size of the increase
#   a,b - the limits within which the new resulting value must be included in
#E:y - the new value
def m_non-uniform(x,sigma,a,b):
    #noise generation
    p=np.random.normal(0,sigma)
    y=x+p
    if y>b:
        y=b
    if y<a:
        y=a
    return y


#PERMUTATIONS
#mutation by inversion of the permutation x with n components

# I:x - the individual to be mutated
#   n - the maximum index of the permutation
# E:y - the resulting permutation
def m_permutation_inversion(x,n):
    #generation of the positions for inversion
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1:p2+1]=[x[i] for i in range(p2,p1-1,-1)]
    return y


#swap mutation of permutation x with n components  mutatia prin interschimbare a permutarii x cu n componete

# I:x - the individual to be mutated
#   n - the maximum index of the permutation
# E:y - the resulting permutation
def m_permutation_swap(x,n):
    #generation of the positions for the swap
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1]=x[p2]
    y[p2]=x[p1]
    return y


#mutation by insertion of permutation x with n components

# I:x - the individual to be mutated
#   n - the maximum index of the permutation
# E:y - the resulting permutation
def m_permutation_insertion(x,n):
    #generation of the positions for the insertion
    poz = np.random.randint(0, n, 2)
    while poz[0] == poz[1]:
        poz = np.random.randint(0, n, 2)
    p1 = np.min(poz)
    p2 = np.max(poz)
    y=x.copy()
    y[p1+1]=x[p2]
    if p1<n-2:
        y[p1+2:n]=np.array([x[i] for i in range(p1+1,n) if i != p2])
    return y