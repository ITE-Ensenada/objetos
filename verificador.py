"""Aqui se integra una funcion la cual indica si el arreglo esta ordenado o no"""
def verificador(array):
    """Bloque el cual verifica si los numeros estan ordenados"""
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    return True
datos = [1,31,31,3,123,23,4,5,6,5,4,4,6,7,8,7,5,43,2,4,6,7,876,543,2
         ,23,4,6,7,8,6,4,3,2,2,2,222,33,542,14,3263472,46,26,16,145,
         151,235,124,315,15,35,134,1325,1325132,52,5123,5123,51325,1324,
         61,51,343]

COMPRUEBA = verificador(datos)
if COMPRUEBA:
    print("Completaste el ciclo de tu arreglo")
    print(datos)
else:
    print("Algo salio mal en el orden")
    print(datos)
