# Prima incercare in Python

# import SciPy
# import OpenCV

print('Prima incercare in Python')


def fib(n):
    # construieste si scrie sirul lui fibonacci pina la n si intoarce lista ca rezultat

    # I: n - limita superioara
    # E: lista termenilor calculati

    result = []
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        result.append(a)
        a, b = b, a + b
    print("<== gata")
    return result

print('Al doilea text')

if __name__=='__main__':
    a=fib(50)
    print('Lista generata:')
    print(a)
