# Script_tema_1.py
# Tema de studiu individual
# copiati si rulati comenzile in consola, cite una pentru a vedea rezultatul fiecareia

import numpy as np

#generare aleatoare vector - 25 intregi intre -3 si 10
v=np.random.randint(-3,11,25)

#generare aleatore matrice - 3x4, elemente generate uniform pe [-2,7]
a=np.random.uniform(-2,7,[3,5])

#calcul element maxim
maxim_v=v.max()
maxim_a=a.max()

#cautare valoarea 5 in vector
poz1=np.argwhere(v==5) # poz1 e o matrice cu "numar aparitii" linii si 1 coloana
print(poz1)

for x in poz1:
    print(x[0])

#cautarea valorii a[0,0] in matrice

poz2=np.argwhere(a==a[0,0]) # poz2 e o matrice cu "numar aparitii" linii si doua coloane
for x in poz2:
    print(x[0],x[1])

#sortare vector
v_sort=np.sort(v)


#sortare matrice dupa ultima coloana
indici=a[:,-1].argsort()
b=a[indici]

#valoare medie vector
val_medie=np.mean(v)

#deviatie standard vector
dev_std=np.std(v)

#vectorul valorilor medii pe fiecare din cele 3 linii ale lui a
med_linii=np.zeros(3)
for i in range(3):
    med_linii[i]=np.mean(a[i])


