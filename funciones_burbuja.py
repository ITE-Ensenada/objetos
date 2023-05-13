
'''
Este modulo se encarga de actualizar un arreglo
algoritmo de ejemplo: 

Si i = 0, tal indice no se vera afectado, ejemplo:

[0, 25, 20, 21, 7]
    	
input: 4

output: [0, 4, 25, 20, 21, 7]

'''

def add_numb(farray):
    '''
    La siguiente funcion se encarga
    de agregar un numero (el que
    desee el usuario) y ordenarlo
    segun el arreglo:

    Si tenemos [0, 1, 5, 3]
    y el usuario ingresa: 2
    el arreglo quedara:

    [0,1,2,5,3]
    '''
    numero = int(input("Ingresa un numero: "))

    array.append(numero)
    i = len(farray) - 1
    while i > 0 and farray[i-1] > numero:
        farray[i] = farray[i-1]
        i -= 1
    # Agrega el numero
    farray[i] = numero

    return farray

def delete_numb(farray):
    '''
    Esta funcion se encarga
    de eliminar el numero
    que el usuario ingrese
    '''
    print(farray)
    delete = int(input("Ingresa el numero que quieres eliminar: "))
    array_actualizado = []
    for i in farray:
        if i != delete:
            array_actualizado.append(i)
    farray = array_actualizado
    print(farray)

array = [1, 2, 3, 4, 5]

delete_numb(array)

def encontrar_numero(arreglo):
    '''
    Esta funcion se encarga
    de imprimir la posicion
    del numero que el usuario
    ingreso
    '''
    print(arreglo)
    numero = int(input("Ingresa el numero que quieres localizar: "))
    localizar = []
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            localizar.append(i)
    print("La posicion es: ")
    return localizar

array = [1, 2, 3, 4, 5]
mostrar_array = encontrar_numero(array)
print(mostrar_array)
