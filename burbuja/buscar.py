'''este codigo localiza un elemento dentro de un arreglo y te da su ubicacion'''
elementos = [1,2,3,4,5,6,2,8,2]

def localizar(arreglo,numero):
    '''busca el numero dentro de un arreglo y te devuelve un arreglo con las posiciones'''
    espacios = len(arreglo)
    contador = 0
    localizador = []
    for i in range(espacios):
        if arreglo[i] == numero:
            localizador.append(i)
            contador += 1
    return localizador
buscar = float(input(" ingrese el numero que desea buscar: "))
resultado = localizar(elementos,buscar)
if not resultado:
    print("el numero no se encuentra dentro del arreglo")
else:
    print("El numero se encuentra en las posiciones: \n",resultado)
