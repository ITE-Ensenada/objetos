"de primera estancia este archivo debe leer un txt y convertirlo a un arreglo "
import numpy as np
from algoritmo import Algoritmo

with open("desorden.txt", "r", encoding="utf-8") as archivo:
    elementos = archivo.read()

#ahora para separar los numeros y asi almacenarlos en una lista
numeros = elementos.split(",")

#aqui con la ayuda de numpy almacenamos en un arreglo pero antes
# con el init convertimos a enteros los numeros
arreglo = np.array([int(num) for num in numeros])
algoritmo = Algoritmo()

# # Llamar al metodo combinaciones
combinaciones = algoritmo.combinaciones(arreglo)
print(combinaciones)

# # Llamar al método permutaciones
# permutaciones = algoritmo.permutaciones(arreglo)
# print(permutaciones)

# # Llamar al método permutacionesRepeat
# permutacionesRepeat = algoritmo.permutacionesrepeat(arreglo)
# print(permutacionesRepeat)
