import numpy as np

def fitness(x):
    return 1+2*np.sin(x[0]-x[2])+np.cos(x[1])

def cerinta_a(dim,a,b):
    populatie=np.zeros([dim,4])
    for i in range(dim):
        populatie[i, :3]=np.random.uniform(a,b,3)
        populatie[i,3]=fitness(populatie[i,:3])
    return populatie

def aritmetica_t(x,y,alpha):
    r1=alpha*x+(1-alpha)*y
    r2=alpha*y+(1-alpha)*x
    return r1,r2

def cerinta_b(populatie,pc,alpha):
    dim=populatie.shape[0]
    populatie_c=populatie.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        if r<=pc:
            print('\nCrossover in \n',populatie[i,:-1], ' calitatea ',populatie[i,-1],'\n',populatie[i+1,:-1], ' calitatea ',populatie[i+1,-1])
            populatie_c[i,:-1],populatie_c[i+1,:-1]=aritmetica_t(populatie[i,:-1],populatie[i+1,:-1],alpha)
            populatie_c[i,-1]=fitness(populatie_c[i,:-1])
            populatie_c[i+1,-1]=fitness(populatie_c[i+1,:-1])
            print('Rezulta\n',populatie_c[i,:-1], ' calitatea ',populatie_c[i,-1],'\n',populatie_c[i+1,:-1], ' calitatea ',populatie_c[i+1,-1])
    return populatie_c

if __name__=="__main__":
    dim=10
    pc=0.7
    alpha=0.25
    a=[-1,0,-2]
    b=[1,1,1]
    populatie=cerinta_a(dim,a,b)
    print(populatie)
    populatie_c=cerinta_b(populatie,pc,alpha)
