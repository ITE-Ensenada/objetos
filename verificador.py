"""Verificador de orden de un arreglo"""
import time
start_time = time.time()

"""Aqui se da nuestro arreglo y se acomoda"""
lista = [1, 4, 3, 5, 6, 7, 4, 2, 234, 5, 26, 2, 6, 6, 7, 62, 63, 6241, 5231, 5, 235, 63, 25, 73, 5]
print ("tu arreglo original es:", lista)
lista.sort()
print("Tu arreglo omdificado es: ", lista)

end_time = time.time()
total_time = end_time - start_time
print("\nEsta ejecucion duro: ", total_time, "segundos")
