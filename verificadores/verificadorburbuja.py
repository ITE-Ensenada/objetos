'''Algoritmo de ordenamiento de numeros'''
def ordenamiento_burbuja_con_verificador(lista):
    '''encargado del ordenamiento de los numeros'''
    n = len(lista)
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenado = False
    return lista

def verificar_orden(lista):
    '''Se encarga de verificar si los numeros estan ordenados'''
    n = len(lista)
    for i in range(n-1):
        if lista[i] > lista[i+1]:
            return False
    return True
#numeros = [10, 5, 8, 3, 2, 6]
numeros = [1, 2, 3, 10, 30, 50, 11, 17, 20]

if verificar_orden(numeros):
    print("La lista ya está ordenada.")
else:
    numeros_ordenados = ordenamiento_burbuja_con_verificador(numeros)
    print("La lista ordenada:", numeros_ordenados)
