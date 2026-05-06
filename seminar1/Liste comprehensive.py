# Exemple de utilizare a listelor comprehensive

# progresie aritmetica a..b cu ratia r
a,b,r=-12,21,3
pa=[i for i in range(a,b,r)]
a,b,r=21,-12,-3
pb=[i for i in range(a,b,r)]

# elemente divizibile cu k din lista
k=5
dpa=[x for x in pa if x%k==0]
dpa2=[x for x in range(a,b,r) if x%k==0]
dpb=[x for x in pb if x%k==0]

# maxim din lista si pozitia de aparitie
v_max=max(pa)
poz_max=pa.index(v_max)
print(pa)
print(dpa)
print("Maxim:",v_max,"   ","in pozitia:", poz_max)

# toate pozitiile de aparitie
t=[1,2,3,4,1,2,3,4,1,2,3,4,3,2,1]
toate_poz=[i for i, j in enumerate(t) if j == 3]


# diviziune
eps=0.1
d=[-1+i*eps for i in range(10000) if -1+i*eps<=1]
print("Diviziune, v1:", d)
# alternativ, folosind numpy
import numpy
d2=numpy.arange(-1,1+0.1,0.1)
print("Diviziune, v2:", d2)