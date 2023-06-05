
def leer_archivo(numeros):
    with open(numeros, 'r') as archivo:
        numeros_str = archivo.read().strip().split(',')
        numeros = [int(num) for num in numeros_str]
    return numeros

arreglo = leer_archivo('numeros.txt')
print(arreglo)


def verificar_ordenamiento(arreglo):
    n = len(arreglo)
    ordenado = True
    for i in range(n - 1):
        if arreglo[i] > arreglo[i + 1]:
            ordenado = False
            break

    if not ordenado:
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
    return arreglo

def verificar_ordenamiento_segundo(arreglo):
    n = len(arreglo)
    # Verificación de ordenamiento ascendente
    ordenado_ascendente = all(arreglo[i] <= arreglo[i+1] for i in range(n-1))
    
    # Verificación de ordenamiento descendente
    ordenado_descendente = all(arreglo[i] >= arreglo[i+1] for i in range(n-1))
    
    if ordenado_ascendente:
        print("El arreglo está ordenado de menor a mayor.")
        

    elif ordenado_descendente:
        print("El arreglo está ordenado de mayor a menor.")
        
    else:
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        
    return arreglo

print(arreglo)    
print("Primer verificador: ")
arreglo = verificar_ordenamiento(arreglo)
print(arreglo)
print("Segundo verificador: ")
arreglo = verificar_ordenamiento_segundo(arreglo)
print(arreglo)