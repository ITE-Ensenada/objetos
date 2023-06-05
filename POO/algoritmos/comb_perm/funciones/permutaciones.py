from funciones.fun_factorial import factorial
import copy
#total = factorial(n) #Nos dice el total de las permutaciones

def permutaciones(elementos):
    if len(elementos) == 0:
        return [[]]
    resultados = []
    for i in range(len(elementos)):
        restantes = elementos[:i] + elementos[i+1:]
        for p in permutaciones(restantes):
            resultados.append([elementos[i]] + p)
    return resultados