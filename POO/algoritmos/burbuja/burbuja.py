def Burbuja(array):
    '''ordena el arreglo'''
    n = len(array)
    for i in range(n-1):       # bucle 1
        for j in range(i+1,n): # bucle 2
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array