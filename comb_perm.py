"""Parte del codigo el cual lee nuestro archivo .txt y lo convierte en arreglo"""

archivo = open('combinaciones.txt', 'r', encoding='utf-8')
contenido = archivo.read()
arreglo = contenido.split(",")

#Combinaciones
def combinaciones(array):
    """Genera nuestras combinaciones"""
    combina = []

    def generar_combinaciones(cont, ini):
        if len(cont) > 0:
            combina.append(cont)

        for i in range(ini, len(array)):
            generar_combinaciones(cont + [array[i]], i + 1)

    generar_combinaciones([], 0)
    return combina

#Permutaciones
def permutaciones(array2):
    """genera permutaciones"""
    cambio = []

    def generar_permutaciones(cont, libres):
        if len(cont) == len(array2):
            cambio.append(cont)
        else:
            for i, elemento in enumerate(libres):
                generar_permutaciones(cont + [elemento], libres[:i] + libres[i + 1:])

    generar_permutaciones([], array2)
    return cambio

print("Combinaciones: ")
print(combinaciones(arreglo))
lista = [1,2,3]
print("Permutaciones: ")
print(permutaciones(lista))

#Permutaciones repetitivas
def repetitivas(array, LONGITUD):
    "Da inicio a las permutaciones"
    permutaciones = []
    permutaciones_repetitivas(array, LONGITUD, [], permutaciones)
    return permutaciones

def permutaciones_repetitivas(array, LONGITUD, permutacion_actual, todas_permutaciones):
    "Genera todas las permutaciones"
    if LONGITUD == 0:
        todas_permutaciones.append(permutacion_actual)
        return

    for elemento in array:
        permutaciones_repetitivas(array, LONGITUD - 1, permutacion_actual + [elemento],
                                   todas_permutaciones)
print("Repetitivas: ")
LONGITUD = 2
permuta = repetitivas(arreglo, LONGITUD)
for permutacion in permuta:
    print(permutacion)
    
