"""Este programa es una modificacion al visto en clase para determinar si se necesita, o no, ordenar una lista"""
def verificador(arreglo):
    """Este verificador lo que hace es ir avanzando de 1 en 1 en los elementos del arreglo y comparalo con el siguiente """
    orden=0
    n = len(arreglo)
    for i in range(n-1):
        if arreglo[i]>arreglo[i+1]:
            orden=1
            break
    if orden == 0:
        print("la lista esta ordenada")
        print(elementos)

    else:
        print("la lista sera ordenada")
        burbuja(arreglo)

def burbuja(arreglo):
    n = len(arreglo)
    for i in range(n-1):       # <-- bucle padre
        #j = i + 1
        for j in range(i+1,n): # <-- bucle hijo
            #print(f" i {i} , j {j}")
            if arreglo[i] > arreglo[j]:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
                #arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    print("Ya ordenados => ",elementos)
#elementos = [0,1,2,3,4,5,6,7,8,9]
#elementos = [3,2,1,6,0,8,-3]
elementos = [3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,78,90,-0,-21,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62]
"""
i=0 - > n-1
j = i + 1 - > n
[4,2,1,0]
2,4,1,0
1,4,2,0
0,4,2,1
i = 1
0,2,4,1
0,1,4,2
i=2
0,1,2,4
"""
verificador(elementos)