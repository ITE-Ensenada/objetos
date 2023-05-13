"""este programa puede agregar, eliminar y verificar la posicion de un elemento de una lista"""
def pregunta(nombre):
    """esta funcion es para preguntar si se desea hacer una operacion"""
    print("Quieres",nombre,"un elemento")
    print("1) Si")
    print("2) No")
    respuesta = input()
    return int(respuesta)

def burbuja(arreglo):
    """esta funcion ordena el arreglo"""
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
    return arreglo

def agregar(arreglo):
    """esta funcion agrega un elemento a un arreglo y luego ordena dicho arreglo"""
    print("Que numero desea agregar a la lista")
    arreglo.append(int(input()))
    arreglo = burbuja(arreglo)
    return arreglo

def eliminar(arreglo):
    """esta funcion elimina un elemento de un arreglo"""
    print("Que numero desea eliminar de la lista")
    arreglo.remove(int(input()))
    return arreglo

def posiciones(arreglo):
    """esta funcion es para conocer la posicion de un numero en un arreglo"""
    print("Que numero desea buscar")
    busca=int(input())
    localizado=""
    for i in range(len(arreglo)):
        if arreglo[i]==busca:
            localizado=localizado+str(i)+", "
    if localizado == "":
        localizado = "No se encontro dicho elemento"
    else:
        localizado = "las posiciones son "+localizado
    return localizado

lista=[2,4,6,8,10,12,14,16]

print("la lista es la siguiente",lista)
respuesta = pregunta("agregar")
if respuesta == 1:
    lista = agregar(lista)
    print("La nueva lista es",lista)
respuesta = pregunta("eliminar")
if respuesta == 1:
    lista = eliminar(lista)
    print("La nueva lista es",lista)
respuesta = pregunta("conocer la posicion de")
if respuesta == 1:
    posicion=posiciones(lista)
    print(posicion)