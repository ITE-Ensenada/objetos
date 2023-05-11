from Operaciones import *

#Para leer el archivo .txt cambiar la direccion de memoria
arreglo = open (r'C:\Users\ramro\OneDrive\Documentos\Programacion\Lenguaje Python\Algoritmo_Prob\numeros.txt') 
contenido = (arreglo.read())
lista = contenido.strip().split(',')

#Convierte cada número de la lista en un entero
lista = [int(num) for num in lista]

#El num "2", son combinaciones de dos numeros, Se puede cambiar
combinaciones = Combinaciones()
resultado_c = combinaciones.calcular(lista, 2)
print('Combinaciones: ', resultado_c)

permutaciones = Permutaciones()
resultado_p = permutaciones.permutar(lista)
print('Permutaciones: ', resultado_p)

permutaciones_repeat = Permutacion_Repeat()
resultado_r = permutaciones_repeat.repeat(lista, 6)
print('Permutaciones repetidas: ', resultado_r)
