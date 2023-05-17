'''permutaciones con repeticion'''
def permutaciones_con_repeticion(arr, r):
    if r == 0:
        yield []
    else:
        for i in range(len(arr)):
            for p in permutaciones_con_repeticion(arr, r-1):
                yield [arr[i]] + p

arr = [1, 2, 3]
r = 3
for perm in permutaciones_con_repeticion(arr, r):
    print(perm)