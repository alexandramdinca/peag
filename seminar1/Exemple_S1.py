# exemple de apel
# import Exemple_S1 as S1
# a=S1.fib_1(10)
# b=S1.fib_2(10)
# c=S1.fib_r(10)

import numpy as np

def fib_1(n):
    # calcularea primilor n (+1) termeni ai sirului Fibonacci, intr-un vector

    # I: n - indicele ultimului termen calculat
    # E: r - vectorul termenilor calculati

    r=np.zeros(n+1, dtype=int)
    r[0]=0
    r[1]=1
    for i in range(2,n+1):
        r[i]=r[i-1]+r[i-2]
    return r

def fib_2(n):
    # calcularea primilor n (+1) termeni ai sirului Fibonacci, intr-o lista

    # I: n - indicele ultimului termen calculat
    # E: r - lista termenilor calculati

    r=[0,1]
    for i in range(2,n+1):
        #t = r[i-1] + r[i-2]
        #r = r + [t]
        r = r + [r[i-1] + r[i-2]]
    return r

def fib_r(n):
    # calcularea termenului n din sirul Fibonacci, recursiv

    # I: n - indicele termenului de calculat
    # E: r - valoarea termenului calculat

    if n==0:
        r=0
    elif n==1:
        r=1
    else:
        r = fib_r(n-1) + fib_r(n-2)
    return r

