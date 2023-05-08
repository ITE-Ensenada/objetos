"""Programa el cual ordena con el metodo de la burbuja"""
import time
start_time = time.time()

def burbuja(arreglo):
    """Metodo de la burbuja para ordenar un arreglo"""
    cont = len(arreglo)

    for i in range(cont):
        for j in range(0, cont-i-1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo

mi_arreglo = [1,4,3,5,6,7,4,2,234,5,26,2,6,6,7,62,63,6241,5231,5,235,63,25,73,5,836,14,4,6,15,7,8,5]
print("Aqui se muestra el arreglo original: ", mi_arreglo)
randomizador = burbuja(mi_arreglo)
print("Aqui se muestra ordenado", randomizador)


end_time = time.time()
total_time = end_time - start_time
print("\nEsta ejecucion duro: ", total_time, "segundos")
