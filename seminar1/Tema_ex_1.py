import numpy as np

def numara(a):
    m,n=a.shape #dimensiuni matrice primita
    nr=0        #contor linii cu elementele în ordine crescătoare
    for i in range(m):
        #sort=True
        #j=0
        # while sort and (j<n-1):
        #     if a[i,j]>a[i,j+1]:
        #         sort=False
        #     else:
        #         j+=1
        sortata = all(a[i, j] <= a[i, j + 1] for j in range(n - 1))
        # returneaza True daca toate elementele din lista sunt True, adica daca linia i este sortata crescator
        if sortata:
            nr+=1
    return nr

if __name__=="__main__":
    a=np.genfromtxt("matrice.txt")
    print(numara(a))