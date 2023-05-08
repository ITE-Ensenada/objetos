import time
start_time = time.time()

def burbuja(arreglo):
    """ordena un arreglo utilizando una burbuja"""
    contador = len(arreglo)

    for i in range(contador):
        for j in range(0, contador-i-1):
            if arreglo[j] > arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo

lista = [1,4,36,32,3,4,5,6,7,53,0,5,3]
print("Aqui se muestra el arreglo original: ", lista)
random = burbuja(lista)
print("Aqui se muestra ordenado", random)

"""muestra en pantalla el tiempo en verificar"""
end_time = time.time()
total_time = end_time - start_time
print("\nSe demoró", total_time, "segundos")