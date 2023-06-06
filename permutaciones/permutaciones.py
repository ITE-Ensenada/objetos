'''programa permutaciones, combinaciones'''
def combinaciones(array, numero):
    if numero == 0:
        yield []
    elif len(array) < numero:
        return
    else:
        for i in range(len(array)):
            elemento = array[i]
            for combo in combinaciones(array[i+1:], numero-1):
                yield [elemento] + combo

def permutaciones(arreglo):
    if len(arreglo) <= 1:
        yield arreglo
    else:
        for i in range(len(arreglo)):
            resto = arreglo[:i] + arreglo[i+1:]
            for p in permutaciones(resto):
                yield [arreglo[i]] + p
