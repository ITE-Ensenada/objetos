def leer_archivo(numeros):
    with open(numeros, 'r') as archivo:
        numeros_str = archivo.read().strip().split(',')
        numeros = [int(num) for num in numeros_str]
    return numeros

arreglo = leer_archivo('numeros.txt')
print(arreglo)

def obtener_combinaciones(arreglo, r):
    n = len(arreglo)
    resultado = []
    def generar_combinaciones(indices, combinacion):
        if len(combinacion) == r:
            resultado.append(combinacion)
            return
        for i in range(len(indices)):
            generar_combinaciones(indices[i+1:], combinacion + [arreglo[indices[i]]])
    generar_combinaciones(list(range(n)), [])
    return resultado

def obtener_permutaciones(arreglo):
    n = len(arreglo)
    resultado = []
    
    def generar_permutaciones(indices, permutacion):
        if len(permutacion) == n:
            resultado.append(permutacion)
            return
        
        for i in range(len(indices)):
            generar_permutaciones(indices[:i] + indices[i+1:], permutacion + [arreglo[indices[i]]])
    
    generar_permutaciones(list(range(n)), [])
    return resultado

def obtener_permutaciones_repetidas(arreglo, r):
    n = len(arreglo)
    resultado = []
    
    def generar_permutaciones_repetidas(permutacion):
        if len(permutacion) == r:
            resultado.append(permutacion)
            return
        
        for i in range(n):
            generar_permutaciones_repetidas(permutacion + [arreglo[i]])
    
    generar_permutaciones_repetidas([])
    return resultado

print("permutaciones con repeticion tomando con 2 elementos del arreglo")
permutaciones_repetidas = obtener_permutaciones_repetidas(arreglo, 2)
print("Permutaciones repetidas:", permutaciones_repetidas)
print("permutaciones tomando del arreglo")
permutaciones = obtener_permutaciones(arreglo)
print("Permutaciones:", permutaciones)
print("combinaciones de 5 elementos del arreglo")
combinaciones = obtener_combinaciones(arreglo, 5)
print("Combinaciones:", combinaciones)