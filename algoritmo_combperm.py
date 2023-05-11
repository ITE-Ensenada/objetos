# pylint: disable = C0103
# pylint: disable = W0621

'''
El siguiente modulo contiene 4 clases:

1. Clase -> Algoritmo
2. Metodos -> Combinaciones, permutaciones, permutaciones con repeticion

El programa lee un archivo de texto que contiene una serie de numeros
y lo convierte en un array de numeros enteros. Una vez se forme el array
el programa lo que hace es analizar las posibles combinaciones y permutaciones
del arreglo.

'''


with open('numeros.txt', 'r', encoding='utf-8') as archivo:
    lines = archivo.readlines()
    file_int = [] # lista vacia para que tome los valores del archivo
    for line in lines:
        numeros = line.split(",")
        for numero in numeros:
            file_int.append(int(numero))  #Agrega los numeros

print("Arreglo: ", file_int)

def factorial(n):
    '''
    La siguiente funcion es totalmente
    obligatoria para el uso correcto
    de las demas funciones
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combinaciones(array, r):
    '''
    La funcion almacena dentro una segunda funcion
    la cual nos mostrara tanto el total de combinaciones
    es decir, el numero de combinaciones, y las combinaciones 
    mismas
    '''
    def muestra_combinaciones(array, r, index, temp, resultado_combinaciones):
        if len(temp) == r:
            resultado_combinaciones.append(temp[:]) # creamos una copia
            return

        for i in range(index, len(array)):
            temp.append(array[i])
            muestra_combinaciones(array, r, i+1, temp, resultado_combinaciones)
            temp.pop()

    resultado_combinaciones = []
    muestra_combinaciones(array, r, 0, [], resultado_combinaciones)
    return resultado_combinaciones

def permutaciones(array):
    '''
    Esta funcion calcula todas las permutaciones posibles
    de un arreglo SIN que se REPITAN elementos
    '''
    def muestra_permutaciones(array, index, temp, muestra_resultado):
        if index == len(array):
            muestra_resultado.append(temp[:]) # creamos una copia
            return

        for i in range(index, len(array)):
            array[index], array[i] = array[i], array[index]
            temp.append(array[index])
            muestra_permutaciones(array, index+1, temp, muestra_resultado)
            temp.pop()
            array[index], array[i] = array[i], array[index]

    muestra_resultado = []
    muestra_permutaciones(array, 0, [], muestra_resultado)
    return muestra_resultado

def permutaciones_repeticion(array, r):
    '''
    *Referencia*:

    Formula: P(n,r = n**r)

    Esta funcion se encarga de calcular todas las permutaciones posibles
    PERMITIENDO repetir elementos
    '''
    def muestra_permurepeticion(array, r, temp, muestra_resultados):
        if r == 0:
            muestra_resultados.append(temp[:])
            return

        for elemento in array:
            temp.append(elemento)
            muestra_permurepeticion(array, r-1, temp, muestra_resultados)
            temp.pop()

    muestra_resultados = []
    muestra_permurepeticion(array, r, [], muestra_resultados)
    return muestra_resultados

# Asignamos valor para "n" y "r"
r = len(file_int) - 1
n = len(file_int)

# Uso de la formula
total_combinaciones = factorial(n) // (factorial(r) * factorial(n - r))
print(f"\nEste es el total de combinaciones del arreglo: {total_combinaciones}")

mostrar_combinaciones = combinaciones(file_int, r)
print("\nEstas son todas las combinaciones posibles: ")
for c in mostrar_combinaciones:
    print(c)

total_permutaciones = factorial(len(file_int))
print(f"Este es el total de permutaciones del arreglo: {total_permutaciones}")


'''
muestreo_permutaciones = permutaciones(file_int)
print("Todas las permutaciones son: ")
for p in muestreo_permutaciones:
    print(p)

'''
total_permutaciones_repeticion = len(file_int)**r
print(f"Total permutaciones en repeticion: ,{total_permutaciones_repeticion}")

'''
muestra_permurepeticion = permutaciones_con_repeticion(arr, r)
print("El total de permutaciones en repeticion posibles son:")
for p in todas_permutaciones:
    print(p)
'''
