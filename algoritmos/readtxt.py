def arreglo(archivo):
    global arreglo
    global f
    with open(archivo,'r') as f:
        contenido = f.read().split(',')
        #print('contenido: ', contenido)
        arreglo=[int(x) for x in contenido]
        print('arreglo resultante: ', arreglo)
        f.close()

        #n = len(arreglo)
        #print(n)

#contar los elementos de arreglo 
def contar_arreglo():
    global n 
    n = len(arreglo)
    #print(n)
def factorial_n():
    global factorial_n
    factorial_n = n 
    for i in range(1,n):
        factorial_n *= i
    #print(factorial_n) #factorial de n 
def elementos(): # elementos sera la cantidad de datos que trandra cada combinacion
    global r 
    r = int(input('Ingresa la cantidad de elementos por combinacion: '))
    global factorial_r
    factorial_r = r 
    for i in range(1,r):
        factorial_r *= i
    #print(factorial_r) #factorial de r
def factorial_m():
    global factorial_m
    global m 
    m = n - r
    if m==0 or m==1:
            factorial_m = 1
    elif m > 1:
        factorial_m = m 
        for i in range(1,m): 
            factorial_m *= i
    #print("factorial m", factorial_m) #factorial de m

def numero_combinaciones():
    com = (factorial_n/ (factorial_m * factorial_r))
    print('total de combinaciones: ', com)

def obtener_combinaciones(arr, r):
    if r == 0:
        yield []
    elif len(arr) < r:
        return
    else:
        for i in range(len(arr)):
            elemento = arr[i]
            for com in obtener_combinaciones(arr[i+1:], r-1):
                yield [elemento] + com

def numero_permutaciones():
    per = factorial_n/factorial_m
    print('total de permutaciones: ',per)

def permutaciones(arr):
    permutaciones = []

    def generar_permutaciones(temp, disponibles):
        if len(temp) == len(arr):
            permutaciones.append(temp)
        else:
            for i in range(len(disponibles)):
                generar_permutaciones(temp + [disponibles[i]], disponibles[:i] + disponibles[i + 1:])

    generar_permutaciones([], arr)
    return permutaciones



#def per_repeticiones(arreglo):
    #per_rep=

archivo = input("nombre del archivo: ")
arreglo(archivo)
contar_arreglo()
factorial_n()
elementos()
factorial_m()
numero_combinaciones()
for com in obtener_combinaciones(arreglo, r):
    print(com)
numero_permutaciones()
print("Permutaciones:")
print(permutaciones(arreglo))
f.close()


