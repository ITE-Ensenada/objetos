'''Este programa agrega un elemento a el arreglo y acomoda los numero de menos a mayor'''
elementos = [1,2,3,4,5,7,8,10]
def agregar_elementos(numero,arreglo):
    '''si el ultimo elemento es menor al numero, agrega el numero al final'''
    posicion = arreglo[-1]
    if numero > posicion:
        j = arreglo.append(numero)
    else:
        j = 0
    return j

def ordenar(arreglo,numero_agregar):
    '''Ordena los numeros del arreglo'''
    numero = len(arreglo)
    j = 0
    for i in range(numero-1):
        if arreglo[i] >= numero_agregar:
            j = i
            break
    arreglo.insert(j,numero_agregar)
    return arreglo

def partir_arreglo(arreglo,numero):
    '''parte el elemento en 2'''
    elemento = len(arreglo)
    mitad = elemento//2
    mitad1 = arreglo[ :mitad]
    mitad2 = arreglo[mitad: ]
    posicion = mitad1[-1]
    if numero < posicion:
        ordenado = ordenar(mitad1,numero)
        arreglo = ordenado + mitad2
    else:
        ordenado = ordenar(mitad2,numero)
        arreglo = mitad1 + ordenado
    return arreglo

numero_acomodar =int(input(" introduce un numero: "))
agregar = agregar_elementos(numero_acomodar,elementos)
if agregar == 0:
    array = partir_arreglo(elementos,numero_acomodar)
    print(array)
else:
    print(elementos)
