"""
Flores Hernandez 10/05/2023
Abre un arreglo de un txt y realiza todas las combinaciones y permutaciones con dicho arreglo
Tambien permite al usuario ingresar un arreglo
"""
#arreglo = open("numeros.txt")
from funciones.permutaciones import *
arreglo=[1,2,3,4]
n = len(arreglo)
permutations(n)