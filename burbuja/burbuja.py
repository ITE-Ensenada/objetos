"""verificador y metodo burbuja"""
def verificador(arreglo):
    '''verifica que el arreglo este ordenado de menor a mayor'''
    n = len(arreglo)
    for i in range(n-1):
        for j in range(i+1,n):
            if arreglo[j] < arreglo[i]:
                burbuja(arreglo)
                return True
def burbuja(arreglo):
    '''ordena los numeros del arreglo'''
    n = len(arreglo)
    for i in range(n-1):       # <-- bucle padre
        for j in range(i+1,n): # <-- bucle hijo
            if arreglo[i] > arreglo[j]:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
