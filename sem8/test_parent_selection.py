# script for testing parent selection - roulette selection with FPS distribution and sigma-scaling
import numpy as np
from selection_mechanisms_EN import roulette
import init_generation as gi
import matplotlib.pyplot as grafic



# random generation of a population
dim=8
n=10
p=gi.gen(n,dim)
# population p is split into the individual matrix and the quality vector
# computing parents and their quality values using roulette selection with sigma-scaled FPS
parents,values=roulette(p[:,:n],p[:,n],dim,n)
# constructing the resulting population
rez=np.zeros([dim,n+1],dtype='int')
rez[:,:n]=parents.copy()
rez[:,n]=values.copy()
print("Current population")
print(p)
print("Parent population")
print(rez)


grafic.plot(p[:,n],"go",markersize=16,label='Qualities of current population')
grafic.plot(rez[:,n],"ro",markersize=10,label='Qualities of parents')
grafic.legend()
grafic.show()

