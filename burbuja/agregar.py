'''Este programa agrega un elemento a el arreglo y acomoda los numero de menos a mayor'''
from burbuja import verificador
def agregar_elementos(numero,arreglo):
    '''si el ultimo elemento es menor al numero, agrega el numero al final'''
    verificador(arreglo)
    posicion = arreglo[-1]
    if numero > posicion:
        arreglo.append(numero)
    else:
        temporal = partir_arreglo(arreglo,numero)
        arreglo = temporal
    return arreglo

def ordenar(arreglo,numero_agregar):
    '''Ordena los numeros del arreglo'''
    numero = len(arreglo)
    j = 0
    for i in range(numero):
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
    if numero <= posicion:
        ordenado = ordenar(mitad1,numero)
        arreglo = ordenado + mitad2
    else:
        ordenado = ordenar(mitad2,numero)
        arreglo = mitad1 + ordenado
    return arreglo
