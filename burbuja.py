import pygame

def agregar_numero(arreglo, numero):
    n = len(arreglo)
    indice = 0
    while indice < n and arreglo[indice] < numero:
        indice += 1
    arreglo.insert(indice, numero)
    return arreglo

def eliminar_numero(arreglo, numero):
    if numero in arreglo:
        arreglo.remove(numero)
    return arreglo
def encontrar_posicion(arreglo, numero):
    if numero in arreglo:
        posicion = arreglo.index(numero)
        return posicion
    else:
        return None

arreglo = [0, 5, 9, 13, 45, 69, 90]

while True:
    print("Elije el numero de la accion que deseas realizar en el arreglo:")
    print(arreglo)
    print("1- Agregar numero")
    print("2- Borrar numero")
    print("3- Localizar numero")

    opcion = input("Opcion: ")

    if opcion == 1:
        numero = input(int("Ingresa el numero que deseas ingresar en el arreglo: "))
        arreglo = agregar_numero(arreglo, numero)
        print("Nuevo arreglo:", arreglo)

    elif opcion == 2:
        numero = input(int("Ingresa el numero que deseas eliminar del arreglo: "))
        arreglo = eliminar_numero_arreglo(arreglo, numero)
        print("Arreglo actualizado:", arreglo)

    elif opcion == 3:
        numero = int(input("Ingrese el número a buscar: "))
        posicion = encontrar_posicion(arreglo, numero)
        if posicion is not None:
            print("El número", numero, "se encuentra en la posición", posicion)
        else:
            print("El número", numero, "no se encuentra en el arreglo.")
    elif opcion == "exit":
        False