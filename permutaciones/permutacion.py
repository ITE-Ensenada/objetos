'''programa permutaciones, combinaciones'''
'''def obtener_combinaciones(arr, k):
    if k == 0:
        yield []
    elif len(arr) < k:
        return
    else:
        for i in range(len(arr)):
            elemento = arr[i]
            for combo in obtener_combinaciones(arr[i+1:], k-1):
                yield [elemento] + combo

arr = [1, 2, 3, 4]
k = int(input("Ingrese el numero de elementos por combinacion: "))

for combo in obtener_combinaciones(arr, k):
    print(combo)'''

def permutaciones(arr):
    if len(arr) <= 1:
        yield arr
    else:
        for i in range(len(arr)):
            resto = arr[:i] + arr[i+1:]
            for p in permutaciones(resto):
                yield [arr[i]] + p

arr = [1,2,3]
for perm in permutaciones(arr):
    print(perm)



