# afisare
print('A inceput scoala! (iar)')

# citire de la tastatura
# implicit tipul transferat este clasa str (sir de caractere

n = input('n=')
print('Tipul datei n este', type(n))

# pentru a lucra cu n ca data int - schimbare de tip
n = int(n)      # n este o alta variabila! cea veche nu mai exista!
print('Tipul datei n este', type(n))

# atribuire
m = n + 7
print('m=', m)

# atribuire multipla
a, b, c = 1.2, -5, 'Limonada'
print(a, '\n', b, '\n', c)
x = y = z = 2 * a + b
print(x, '\n', y, '\n', z)

import numpy

# citire vector dintr-un fisier text
v = numpy.genfromtxt('fis1.txt', int)
print(v)

# scriere vector in fisier text
numpy.savetxt('fis2.txt', v, '%i')

##STRUCTURA IF
# if-else
# verificarea paritatii lui n
if n % 2 == 0:
    print(n, 'este par')
else:
    print(n, 'este impar')

# if-elif-else
# verificarea proprietatii de divizibilitate cu 3 a lui n
if n % 3 == 0:
    print(n, ' divizibil cu 3')
elif n % 3 == 1:
    print(n, 'nedivizibil cu 3, rest 1')
else:
    print(n, 'nedivizibi cu 3, rest 2')

# structura while
# produsul elementelor pozitive ale vectorului v
p, exista = 1, False
i = 0
dim = len(v)
while (i < dim):
    if v[i] > 0:
        p *= v[i]
        exista = True
    i = i + 1
if exista:
    print('Produsul este ', p)
else:
    print('Nu exista elemente pozitive')

# structura for
# parcurgere "standard", cu indice in 0,1,...,dim-1
p, exista = 1, False
for i in range(dim):
    if v[i] > 0:
        p *= v[i]
        exista = True
if exista:
    print('Produsul este ', p)
else:
    print('Nu exista elemente pozitive')

# parcurgerea elementelor unei multimi
p, exista = 1, False
for element in v:
    if element > 0:
        p *= element
        exista = True
if exista:
    print('Produsul este ', p)
else:
    print('Nu exista elemente pozitive')

# citire si prelucrare matrice
a = numpy.genfromtxt('fis3.txt', int)
# calculul elementelor minim si maxim
# dimensiunile matricei
lin, col = a.shape
minim = maxim = a[0, 0]
for i in range(lin):
    for j in range(col):
        if minim > a[i, j]:
            minim = a[i, j]
        elif maxim < a[i, j]:
            maxim = a[i, j]
print('Minimul este', minim, ' si maximul este ', maxim)

# echivalent
minim,maxim=a.min(),a.max()
print('Minimul este', minim, ' si maximul este ', maxim)

#copierea unei matrice in fisier text - similar vectorilor
numpy.savetxt('matrice.txt',a,'%i')
numpy.savetxt('matrice1.txt',a,'%.2f')