'''Archivo main utilizado para ejecutar y testear las funciones del archivo funciones_burbuja.py'''''

from funciones_burbuja import *

if __name__ == '__main__':

    #cantidad = 100000 #random.randint(0,100000)

    #arreglo = generar_numeros( cantidad )
    index = 0

    arreglo = [1,2,3,4,5,6,7]

    numeros = [3,1,5]

    #print(arreglo)

    #verificador0(arreglo)

    #verificador1(arreglo)

    #arreglo = add_int_number1(arreglo, 4)

    #arreglo = add_int_number2(arreglo, 4)

    #arreglo = add_int_number3(arreglo, 4)

    print(find_all_int_number(arreglo, numeros))

    #print(arreglo)
