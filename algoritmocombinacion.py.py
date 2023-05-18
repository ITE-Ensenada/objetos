def add_numb(arry):
    
    numero = int(input("Ingrese un numero: "))

    array.append(numero)
    i = len(arry) - 1
    while i > 0 and arry[i-1] > numero:
        arry[i] = arry[i-1]
        i -= 1
    # Agregue el numero
    arry[i] = numero

    return arry

def delete_numb(arry):
   
    print(arry)
    delete = int(input("Ingresa el numero que gustes eliminar: "))
    array_actualiz = []
    for i in arry:
        if i != delete:
            array_actualiz.append(i)
    arry = array_actualiz
    print(arry)

arry = [1, 4, 5, 16, 2]

delete_numb(arry)

def encontrar_numero(arreglo):
   
    print(arreglo)
    numero = int(input("Ingresa el numero que quieres encontrar: "))
    Encuentro = [0]
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            Encuentro.append(i)
    print("Su lugar es: ")
    return Encuentro

array = [1, 2, 3, 4, 5]
mostrar_array = encontrar_numero(array)
print(mostrar_array)