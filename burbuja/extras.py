'''funciones para corregir cosas que no pude corregir en el main'''
def eliminar_espacios(arreglo):
    if arreglo[-1] == '' :
        arreglo = arreglo[:len(arreglo)-1]
    return arreglo
