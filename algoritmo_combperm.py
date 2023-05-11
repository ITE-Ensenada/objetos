'''
El siguiente modulo contiene 4 clases:

1. Clase -> Algoritmo
2. Metodos -> Combinaciones, permutaciones, permutaciones con repeticion

El programa lee un archivo de texto que contiene una serie de numeros
y lo convierte en un array de numeros enteros. Una vez se forme el array
el programa lo que hace es analizar las posibles combinaciones y permutaciones
del arreglo.

'''
import math
import itertools
from itertools import product


with open('numeros.txt', 'r', encoding='utf-8') as archivo:
    lines = archivo.readlines()
    file_int = [] # lista vacia para que tome los valores del archivo
    for line in lines:
        numeros = line.split(",")
        for numero in numeros:
            file_int.append(int(numero))  #Agrega los numeros

print("Arreglo: ", file_int)


class Algoritmo:
    '''
        Esta clase provee a los
        3 metodos principales un solo
        parametro: el arreglo, este arreglo
        esta directamente relacionado 
    '''
    def __init__(self, array):
        self.array = array

    def combinacion(self):
        '''
            Este metodo toma a "combs"
            como un arreglo vacio, el cual
            ira aumentando su tamaño conforme
            a n combinaciones posibles
        '''
        # Obtencion del numero total de combinaciones:
        # Formula: C(n,k) = n! / k(! * (n-k)!)

        n_length = len(self.array)
        combinaciones = 0

        for k in range(1, n_length + 1):
            combinaciones += len(list(itertools.combinations(self.array, k)))

        print(combinaciones)

        # Combinaciones posibles:
        combs = []
        for i in range(1, len(self.array) + 1):
            combs.extend(list(itertools.combinations(self.array, i)))

        print("\nCombinacions posibles: \n", combs)

    def permutacion(self):
        '''
            Este metodo muestra todas las formas en que
            nuestro archivo con numeros puede ser ordenado
            sin que se repitan sus elementos
        '''

        # Obtencion del numero total de permutaciones:
        # Formula: n! = n * (n-1) * (n-2) * ... * 2 * 1

        permutaciones = math.factorial(len(self.array))
        print(permutaciones)

		# Muestra distintas formas de orden del arreglo
        for permuta in itertools.permutations(self.array):
            print(permuta)


    def permutacion_repetcion1(self):
        '''
            Este metodo muestra todas las formas en que
            nuestro archivo con numeros puede ser ordenado
            con la excepcion de que los elementos puedan
            aparecer mas de una vez
        '''
        # muestra el numero total de permutaciones
        repeticiones_permitidas = len(self.array)
        permutaciones_repeticion = len(self.array) ** repeticiones_permitidas
        print(permutaciones_repeticion)

        # muestra las formas de ordenar el arreglo
        length = len(self.array)
        permuta_repeat = list(product(self.array, repeat=length))
        print(permuta_repeat)

algoritmo = Algoritmo(file_int)
algoritmo.combinacion()
algoritmo.permutacion()
algoritmo.permutacion_repetcion1()
