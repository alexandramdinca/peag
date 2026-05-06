# Rezolvarea problemei celor n regine

import matplotlib.pyplot as grafic

def regine(n):
    # cautare in spatiul solutiilor

    x=[0]*n     # lista de lucru, valori irelevante
    nr=0        # numar solutii gasite
    i=0         # indicele primei componente a solutiei
    x[i]=-1     # prima valoare posibila minus ratia x[i] apartine 0..n-1
    while i>-1:     # nu s-a atins configuratia finala
        gasit=0     # nu am gasit o valoare acceptabila pentru componenta i
        while x[i]<n-1 and  not gasit:
            x[i]=x[i]+1         # adauga ratia la valoarea curenta
            gasit=posibil(x,i)  # e valoare acceptabila?
        if not gasit:
            i=i-1       # impas, revenire
        else:
            if i==n-1:  # configuratie solutie
                nr=nr+1
                retine_solutia(nr,x)
            else:
                i=i+1       # avans
                x[i]=-1     # prima valoare minus ratia
    return nr

def posibil(x,i):
    p=1             # presupunem ca solutia partiala e acceptabila
    for j in range(i):
        if (x[i]==x[j]) or (abs(i-j)==abs(x[i]-x[j])):
            p=0     # presupunerea a fost gresita
    return p

def retine_solutia(nr, sol):
    # vizualizare asezare regine pe tabla de sah

    # I: sol - permutarea care defineste asezarea
    # E: -

    print('Solutia numarul ', nr, " : ", sol)
    n = len(sol)
    fig = grafic.figure(1)
    ax = fig.gca()
    x = [i + 0.5 for i in range(n)]
    y = [sol[i] + 0.5 for i in range(n)]
    grafic.plot(x, y, 'r*', markersize=10)
    grafic.xticks(range(n + 1))
    grafic.yticks(range(n + 1))
    grafic.grid(True, which='both', color='k', linestyle='-', linewidth=1)
    ax.set_aspect('equal')
    grafic.title('Solutia nr. '+str(nr))
    grafic.ion()
    grafic.pause(0.0000001)

    input('Apasa <Enter> pentru a continua')
    fig.clear()

def regine_2(n):
    # varianta recursiva

    # pregatiri
    x = [0] * n  # lista de lucru, valori irelevante
    nr = 0  # numar solutii gasite
    i = 0
    # apel functie recursiva
    nr=regine_r(n,x,i,nr)
    print('Am gasit ', nr,' solutii')

def regine_r(n,x,i,nr):
    if i==n:
        nr=nr+1
        retine_solutia(nr,x)
    else:
        for j in range(n):
            x[i]=j
            if posibil(x,i):
                nr=regine_r(n,x,i+1,nr)
    return nr

n=int(input('Nr. regine='))
regine(n)
