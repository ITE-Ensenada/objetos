"""
verificador de orden del vector:
ejemplo mejor de los casos:
    [0,1,2,3,4,5]
REPEAT
    i = 0
    j = i +1
    if [i] < [j]
        i++
        j = i + 1

if j == n TRUE

ejemplo peor de los casos:
    [0,1,
    3,2,
    4,61]
    2,3,4,61
    0,1,2,3,4,61
i =0 
j = i +1
REPEAT
    if [i] < [j]
        
O(log n ^ 2 )
-PERMUTACION
    [n][n][n] = > n * n * n
    [1][2][3]

    [1][1][1]
-COMBINACIONES
    [n][n][n]

"""
def verificador(arreglo):
    """verificador 1"""
    ncant = len(arreglo)
    for i in range(ncant-1):
        if arreglo[i] > arreglo[i+1]:
            burbuja(arreglo)
            break
        else:
            print("no se necesito burbuja estaba en orden", arreglo[i])

#def intercambia(index_a, index_b, arreglo):

def burbuja(arreglo):
    """el mero mero de la burbuja para acomodar el desorden este si esta a la orden pal desorden"""
    ncant = len(arreglo)
    for i in range(ncant-1):       # <-- bucle padre
        #j = i + 1
        for j in range(i+1,ncant): # <-- bucle hijo
            #print(f" i {i} , j {j}")
            if arreglo[i] > arreglo[j]:
                temp = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = temp
                #arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
elementos = [0,1,2,3,4,5,6,7,8,9]
#elementos = [3,2,1,6,0,8,-3]

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
print("Numero a ordenar => ", elementos)
burbuja(elementos)
print("Ya ordenados => ",elementos)
