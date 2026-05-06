import numpy as np

# numbers from 1 to 350 can be represented using 9 bits

# representation of the natural number x as a Gray binary string on m bits
def nat_Gray(x,m):
    # obtain the binary representation of x in the form '0b_bit_string' and extract bit_string
    t=bin(x)[2:]
    # pad with 0s for representation on m bits
    t=t.zfill(m)
    # t is a string of characters
    rezultat = t[0]
    for i in range(1,m):
        # perform XOR operation at bit level - works with integers
        bit= str(int(t[i]) ^ int(t[i-1]))
        # append the bit character to the string
        rezultat=rezultat+bit
    # the result is a string of bits - string containing elements '0' and '1'
    # return a list with elements 0 and 1
    return [int(rezultat[i]) for i in range(m)]

# inverse operation of the one presented above
def Gray_bin(bG):
    m = len(bG)
    # convert into a string of characters
    bG_s=''
    for i in range(m):
        bG_s+=str(bG[i])
    # obtain the standard binary representation, as a string of characters
    bS = bG_s[0]
    val=int(bG_s[0])
    for i in range(1,m):
        if bG_s[i]=='1':
            val=int(not(val))
        bS=bS+str(val)
    # obtain the base-10 representation of the binary string
    n = int(bS,2)
    return n

def fitness(sir):
    x=Gray_bin(sir)
    return x**2

def cerinta_a(dim):
    populatie=np.zeros([dim,9],dtype="int")
    calitati=np.zeros(dim,dtype="int")
    for i in range(dim):
        x=np.random.randint(1,351)
        populatie[i]=np.array([nat_Gray(x,9)])
        calitati[i]=fitness(populatie[i])
    return populatie,calitati


# I:
# parents, fitness_values - the parent population and the vector of fitness values
# pc - recombination probability
# O:
# offspring, offspring_fitness - resulting population and fitness values vector

def cerinta_b(parinti,calitati,pc):
    copii=parinti.copy()
    calitati_copii=calitati.copy()
    dimensiune=calitati.size
    for i in range(0,dimensiune-1,2):
        raspuns=np.random.uniform(0,1)
        if raspuns<pc:
            parinte1=parinti[i].copy()
            parinte2=parinti[i+1].copy()
            print('Selected parents:',parinte1, parinte2)
            copil1, copil2=recombinare_unipunct(parinte1,parinte2)
            val1, val2=fitness(copil1), fitness(copil2)
            copii[i]=copil1.copy()
            copii[i+1]=copil2.copy()
            calitati_copii[i], calitati_copii[i+1]=val1, val2
    return copii, calitati_copii

def recombinare_unipunct(x,y):
    copil1, copil2=x.copy(), y.copy()
    i=np.random.randint(1,x.size-1)
    copil1[i:]=y[i:]
    copil2[i:]=x[i:]
    print('Single-point recombination at position',i)
    print('Resulting offspring ',copil1,copil2)
    return copil1, copil2

if __name__=="__main__":
    dim_curent=10
    pop_curenta, qual_curenta=cerinta_a(dim_curent)
    print("CURRENT POPULATION AND FITNESS VALUES")
    print(pop_curenta)
    print(qual_curenta)
    pc=0.7
    copii,qual_copii=cerinta_b(pop_curenta,qual_curenta,pc)