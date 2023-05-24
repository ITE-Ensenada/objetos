'''este codigo localiza un elemento dentro de un arreglo y te da su ubicacion'''
def localizar(arreglo,numero):
    '''busca el numero dentro de un arreglo y te devuelve un arreglo con las posiciones'''
    espacios = len(arreglo)
    localizador = []
    for i in range(espacios):
        if arreglo[i] == numero:
            localizador.append(i)
    return localizador
