'''este programa elimina un elemento del arreglo'''
def recorrer(arreglo):
    '''recorre el arreglo y elimina los espacios vacios'''
    espacios = len(arreglo)
    vacios = espacios-1
    j=0
    for i in range(espacios-1):
        if arreglo[i] == '':
            j = i + 1
            arreglo[i] = arreglo[j]
            arreglo[j] = ''
        nuevoarreglo =  arreglo[:vacios]
    return nuevoarreglo

def eliminar(arreglo, numero):
    '''elimina el numero del arreglo'''
    espacio = len(arreglo)
    for i in range(espacio):
        if arreglo[i] == numero:
            arreglo[i] = ''

def verificar(arreglo,numero):
    '''verifica que el numero se encuentre en el arreglo'''
    espacio = len(arreglo)
    for i in range(espacio):
        if arreglo[i] == numero:
            eliminar(arreglo,numero)
            nuevoarreglo = recorrer(arreglo)
            arreglo = nuevoarreglo
            return arreglo
