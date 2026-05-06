import random
import copy

def fitness(x):
    return sum(x)


def cerinta_a(dim):
    populatie=[]
    for i in range(dim):
        individ=random.choices([0,1],k=7)
        individ.append(fitness(individ))
        populatie.append(individ)
    return populatie

def cerinta_b(parinti,pc):
    copii=copy.deepcopy(parinti)
    dim=len(parinti)
    for i in range(0,dim-1,2):
        raspuns=random.uniform(0,1)
        if raspuns<pc:
            parinte1=parinti[i][:-1]
            parinte2 = parinti[i+1][:-1]
            copil1, copil2 = recombinare_2(parinte1, parinte2)
            copil1.append(fitness(copil1))
            copil2.append(fitness(copil2))
            copii[i] = copil1.copy()
            copii[i + 1] = copil2.copy()
    return copii

def recombinare_2(x,y):
    print("\nRecombinare in ",x,y)
    copil1,copil2=x.copy(),y.copy()
    i, j = sorted(random.sample(range(1,6), 2))
    print('Punctele ',i,j)
    copil1[i:j]=y[i:j]
    copil2[i:j]=x[i:j]
    print("Rezulta ",copil1,copil2)
    return copil1,copil2

if __name__=="__main__":
    populatie=cerinta_a(10)
    copii=cerinta_b(populatie,pc=0.8)
    print("\n\n Populatia de parinti")
    for individ in populatie:
        print(individ)
    print("\nPopulatia de copii")
    for individ in copii:
        print(individ)



