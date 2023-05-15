
def factorial(valor):

    for num in range(1, valor):
        valor *= num

    return valor



def convertor_txt_py():
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()

    numeros_str = contenido.split(',')

    arreglo = [int(numero) for numero in numeros_str]

    return arreglo


def combinaciones(arreglo):
    
    longitud = len(arreglo) # Longitud del arreglo
    print( range(longitud) )


def permutaciones(arreglo):
    pass


def permutaciones_con_repeticion(arreglo):
    pass




if __name__ == '__main__':
    combinaciones(arreglo = convertor_txt_py())