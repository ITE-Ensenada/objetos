# pylint: disable=W0105
'''
    Este modulo contiene
    una funcion que nos
    indicara si un arreglo
    esta ordenado o 
    desordenado
'''

import time
start_time = time.time()

def verificador_burbuja(arreglo):
    '''
        La funcion lo que hace es verificar
        si los elementos cumplen el siguiente
        requisito:

        que al hacer un recorrido, el primer
        elemento sea menor al que le sigue
    '''
    ordenado = True
    n_arreglo = len(arreglo)

    for i in range(n_arreglo-1):
	    #j = i + 1
        for j in range(i+1,n_arreglo):
            # Imprimimos para saber las posiciones en las que nos encontramos
            """
            print("Index I: ",i, "\t\t\t\tIndex J: ",j)
            print("value I: ", arreglo[i], "\t\t\t\tvalue J: ", arreglo[j])
            """
            # validacion de orden
            if arreglo[i] > arreglo[j]:
                ordenado = False
    if ordenado is True:
        print("Tu arreglo esta ORDENADO")
    else:
        print("Tu arreglo esta DESORDENADO")

elementos = [3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,78,90,-0,-21,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62]

verificador_burbuja(elementos)

# Medir tiempo
end_time = time.time()
total_time = end_time - start_time
print("\nEl tiempo de ejecucion de este verificador fue de: ", total_time, "segundos")
