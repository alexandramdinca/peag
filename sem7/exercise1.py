import numpy as np

# representation of n on m bits as a binary string stored as a vector of 0-1
def dec_to_bin(n,m):
    # standard representation, but as a string of characters
    repr = bin(n)[2:]
    # transformation into a string of m characters
    repr_f = repr.zfill(m)
    # transformation into a binary string (list of bits)
    x=[int(repr_f[i]) for i in range(m)]
    return x

# inverse conversion
def bin_to_dec(x,m):
    # conversion from list of integers to list of characters
    y=''
    for i in range(m):
        y+=str(x[i])
    # base-10 representation
    n=int(y,2)
    return n

# fitness function

def fitness(sir):
    x=bin_to_dec(sir[0:11],11)
    y=bin_to_dec(sir[11:23],12)
    return (y-1)*(np.sin(x-2)**2)

# an individual has 23 bits - the binary representation of numbers from {1,...,1500} concatenated with
# the binary representation of numbers from {0,...,2501}
def cerinta_a(dim):
    populatie=[]
    print("INITIAL POPULATION")
    for i in range(dim):
        x=np.random.randint(0,1501)
        y=np.random.randint(0,2502)
        print("Components in base 10 (phenotype):",x,y)
        individ=dec_to_bin(x,11)+dec_to_bin(y+1,12)
        print("Genotype representation",individ)
        calitate=fitness(individ)
        print(f"Fitness: {calitate:.4f}")
        individ=individ+[calitate]
        populatie=populatie+[individ]
    return populatie


def recombinare_3puncte(sir1,sir2):
    n=23
    i=np.random.randint(0,n-2)
    j=np.random.randint(i+1,n-1)
    k=np.random.randint(j+1,n)
    # or, equivalently
    #[i,j,k] = sorted(np.random.choice(range(10), 3, replace=False))
    print("Positions ",i,j,k)
    copil1=sir1.copy()
    copil2=sir2.copy()
    copil1[i:j]=sir2[i:j]
    copil2[i:j]=sir1[i:j]
    copil1[k:]=sir2[k:]
    copil2[k:]=sir1[k:]
    return copil1, copil2


def cerinta_b(populatie,pc):
    dim=len(populatie)
    copii=populatie.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        if r<=pc:
            # selecting individuals, without their fitness values
            p1=populatie[i][:23].copy()
            p2=populatie[i+1][:23].copy()
            print(f"\n\nParent1 {populatie[i][:-1]} fitness {populatie[i][-1]:.4f}")
            print(f"Parent2 {populatie[i + 1][:-1]} fitness {populatie[i + 1][-1]:.4f}")
            c1,c2=recombinare_3puncte(p1,p2)
            copii[i][:23]=c1
            copii[i][23]=fitness(c1)
            copii[i+1][:23] = c2
            copii[i+1][23] = fitness(c2)
            print(f"Individual {copii[i][:-1]} fitness {copii[i][-1]:.4f}")
            print(f"Individual {copii[i+1][:-1]} fitness {copii[i+1][-1]:.4f}")
    return copii

if __name__=="__main__":
    p=cerinta_a(10)
    c=cerinta_b(p,0.8)
    print("\n\nOFFSPRING POPULATION")
    for individ in c:
        print(f"Individual {individ[:-1]} fitness {individ[-1]:.4f}")