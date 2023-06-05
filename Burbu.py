def pregunta(nombre):
    print(f"Quieres {nombre} un elemento")
    print("1) Si")
    print("2) No")
    respuesta = int(input())
    return respuesta

def burbuja(arreglo):
    n = len(arreglo)
    for i in range(n-1):
        for j in range(i+1, n):
            if arreglo[i] > arreglo[j]:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    return arreglo

def agregar(arreglo):
    print("Qué elemento desea agregar a la lista?")
    elemento = int(input())
    arreglo.append(elemento)
    arreglo = burbuja(arreglo)
    return arreglo

def eliminar(arreglo):
    print("Qué elemento desea eliminar de la lista?")
    elemento = int(input())
    arreglo.remove(elemento)
    return arreglo

def posiciones(arreglo):
    print("Qué elemento desea buscar?")
    busca = int(input())
    posiciones = [str(i) for i, num in enumerate(arreglo) if num == busca]
    if posiciones:
        return "Las posiciones son: " + ", ".join(posiciones)
    else:
        return "No se encontró dicho elemento"

lista = [24, 15, 7, 41, 2, 1, 9, 11]

print("La lista es la siguiente:", lista)
respuesta = pregunta("agregar")
if respuesta == 1:
    lista = agregar(lista)
    print("La nueva lista es:", lista)
respuesta = pregunta("eliminar")
if respuesta == 1:
    lista = eliminar(lista)
    print("La nueva lista es:", lista)
respuesta = pregunta("conocer la posición de")
if respuesta == 1:
    posicion = posiciones(lista)
    print(posicion)