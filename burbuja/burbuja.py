"""verificador y metodo burbuja"""
def verificador(arreglo):
    '''verifica que el arreglo este ordenado de menor a mayor'''
    n = len(arreglo)
    for i in range(n-1):
        for j in range(i+1,n):
            if arreglo[j] < arreglo[i]:
                return False
def burbuja(arreglo):
    '''ordena los numeros del arreglo'''
    n = len(arreglo)
    for i in range(n-1):       # <-- bucle padre
        for j in range(i+1,n): # <-- bucle hijo
            if arreglo[i] > arreglo[j]:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
elementos = [5,3,5,1,0,5,7,87,-2]
verifica = verificador(elementos)
if verifica is False:
    print("numeros desordenados")
    burbuja(elementos)
    print(" ordenados: ",elementos)
else:
    print("los numeros estan ordenados")
