'''menu'''
from permutaciones import combinaciones, permutaciones
numeros = []
with open('datos.txt', 'r') as archivo:
    linea = archivo.readline()
    elementos = linea.split(',')
    for elemento in elementos:
        numero = int(elemento.strip())
        numeros.append(numero)

def obtener_combinaciones(array):
    numero_combinaciones = 3
    for combo in combinaciones(array,numero_combinaciones):
        print(combo)

def obtener_permutaciones(arreglo):
    for permutacion in permutaciones(arreglo):
        print(permutacion)

opcion = " "
while opcion != "exit":
    print("opciones: [permutacion,combinacion, exit]")
    opcion = input("Que operacion desea realizar?").lower()
    opciones = {
        "permutacion": obtener_permutaciones,
        "combinacion": obtener_combinaciones,
    }
    if opcion in opciones:
        opciones[opcion](numeros)
    elif opcion == "exit":
        print("bye")
    else:
        print("Comando invalido")
