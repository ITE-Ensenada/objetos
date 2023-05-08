'''Algoritmo de ordenamiento de numeros'''
def ordenamiento_burbuja(lista):
    '''Este es un verificador que hace un ordenamiento de los numeros de menor a mayor.'''
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
numeros = [10, 5, 8, 3, 2, 6, 14, 141, 145, 123, 9, 11, 13]
numeros_ordenados = ordenamiento_burbuja(numeros)
print(numeros_ordenados) # [2, 3, 5, 6, 8, 10]

