from permutaciones import permutaciones
from combinaciones import combinaciones

arreglo = [5, 4, 3, 1]

# Obtener permutaciones
resultado_permutaciones = permutaciones(arreglo)
print("Permutaciones:")
for p in resultado_permutaciones:
    print(p)

r = 4

# Obtener combinaciones
resultado_combinaciones = combinaciones(arreglo, r)
print("Combinaciones:")
for c in resultado_combinaciones:
    print(c)