# script for the test of parents selection - SUS selection with FPS with sigma scaling
import numpy as np
from selection_mechanisms_EN import *

import init_generation as gi
import matplotlib.pyplot as graph


# random generation of a population
dim=12
c=np.genfromtxt("costuri.txt")

p,v=gi.gen(c,dim)
# the calculation of parents and their qualities using SUS with FPS with sigma scaling
parents,values=SUS(p,v,dim,c.shape[0])


x=range(dim)
graph.plot(x,v,"go",markersize=16,label='Qualities of current population')
graph.plot(x,values,"ro",markersize=10,label='Qualities of the parents')
graph.legend()
graph.show()