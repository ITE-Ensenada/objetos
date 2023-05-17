"""Esta funcion se encarga se añadir un número al arreglo"""
def add_numb(garray):

  
    numero = int(input("Ingresa un numero: "))

    array.append(numero)
    i = len(garray) - 1
    while i > 0 and garray[i-1] > numero:
        garray[i] = garray[i-1]
        i -= 1
    # Agrega el numero
    garray[i] = numero

    return garray

def delete_numb(garray):
  """Esta función se encarga de eliminar el número que la persona elija"""
    print(garray)
    delete = int(input("Ingresa el numero a eliminar: "))
    array_actualizado = []
    for i in garray:
        if i != delete:
            array_actualizado.append(i)
    garray = array_actualizado
    print(garray)

array = [1, 2, 3, 4, 5]

delete_numb(array)

def encontrar_numero(arreglo):
    
    print(arreglo)
    numero = int(input("Ingresa el numero que busca: "))
    localizar = []
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            localizar.append(i)
    print("La posicion es: ")
    return localizar

array = [1, 2, 3, 4, 5]
mostrar_array = encontrar_numero(array)
print(mostrar_array)
