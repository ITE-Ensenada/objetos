# pylint: disable=C0103

'''
    Metodo ordenar un arreglo
    con n elementos
'''
from funciones_burbuja import *

# -----------------------

class Producto:
    '''
    La clase almacena propiedades
    tipicas de un producto

    '''
    def __init__(self, nombre, peso = 1, precio = 1, tamanio = 1, fragil = 1):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.tamanio = tamanio
        self.fragil = fragil

lista = []
with open('basedatos.txt', 'r', encoding='utf-8') as file:
    leng = len(lista)
    print(leng)
    h = 0
    for line in file:
        values = line.strip().split(',')
        lista[h].append(Producto(values[0:4]))
        h = h + 1

print(lista)

def burbuja(arreglo):
    '''
    Esta funcion intercambia numeros
    de menor a mayor

    '''
    n = len(arreglo)
    for i in range(n-1):       # <-- bucle padre
        #j = i + 1
        for j in range(i+1,n): # <-- bucle hijo
            #print(f" i {i} , j {j}")
            if arreglo[i] > arreglo[j]:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
                #arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
#elementos = [0,1,2,3,4,5,6,7,8,9]
#elementos = [3,2,1,6,0,8,-3]
elementos = [3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,78,90,-0,-21,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62]

print("Numero a ordenar => ", elementos)
burbuja(elementos)
print("\nYa ordenados => ",elementos)

add_numb(elementos)
delete_numb(elementos)
encontrar_numero(elementos)
