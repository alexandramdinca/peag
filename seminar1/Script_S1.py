import numpy as np

m=np.zeros([4,5])
print('Matrice: ')
print(m)

m[:4,:4]=np.genfromtxt('matrice.txt')
print('Matrice dupa citire: ')
print(m)

for i in range(4):
    m[i,4]=np.sum(m[i,:4])
print('Matrice dupa calcule: ')
print(m)

m_a=np.random.uniform(0,1,[5,3])
print("Matrice cu valori aleatoare uniform intre 0 si 1:")
print(m_a)

p=np.matmul(m,m_a)      # inmultire matrice
print('Produsul intre matricele m si m_a:')
print(p)