'''Algoritmo para ordenar de menor a mayor'''
def ordenamiento_seleccion(lista):
    '''Algoritmo simple que recorre una lista varias veces buscando el elemento más pequeño y colocándolo en su posición correcta.'''
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
numeros = [10, 5, 8, 3, 2, 6]
numeros_ordenados = ordenamiento_seleccion(numeros)
print(numeros_ordenados) # [2, 3, 5, 6, 8, 10]
