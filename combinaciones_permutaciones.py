def generar_combinaciones(arr):
    combinaciones = []

    def generar_combinaciones_util(temp, start):
        if len(temp) > 0:
            combinaciones.append(temp)

        for i in range(start, len(arr)):
            generar_combinaciones_util(temp + [arr[i]], i + 1)

    generar_combinaciones_util([], 0)
    return combinaciones


def generar_permutaciones(arr):
    permutaciones = []

    def generar_permutaciones_util(temp, disponibles):
        if len(temp) == len(arr):
            permutaciones.append(temp)
        else:
            for i in range(len(disponibles)):
                generar_permutaciones_util(temp + [disponibles[i]], disponibles[:i] + disponibles[i + 1:])

    generar_permutaciones_util([], arr)
    return permutaciones

# Ejemplo de uso
arreglo = [2, 3, 4, 65, 3, 21, 4, 45, 76, 89, 8, 98, 9]
print("Combinaciones:")
print(generar_combinaciones(arreglo))
print("Permutaciones:")
print(generar_permutaciones(arreglo))