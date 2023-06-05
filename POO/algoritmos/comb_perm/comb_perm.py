"""
Flores Hernandez 10/05/2023
utiliza un arreglo y realiza todas las combinaciones y permutaciones con dicho arreglo
"""
#arreglo = open("numeros.txt")
from funciones.permutaciones import *
from funciones.combinaciones import *
arreglo=[1,2,3,4]
n = len(arreglo)
resultado = permutaciones(arreglo)
for p in resultado:
    print(p)

r = 3
resultado = combinaciones(arreglo, r)
for c in resultado:
    print(c)
