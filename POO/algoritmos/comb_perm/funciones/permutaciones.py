from funciones.fun_factorial import factorial
import copy
#total = factorial(n) #Nos dice el total de las permutaciones

def permutacion(array, n):
	#array1=copy.deecopy(array)
	for i in range(n):
		array1=copy.deepcopy(array)
		temp1 = array1[0]
		array1[0] = array1[i]
		array1[i] = temp1
		if i==0: print(array1)
		k=2
		rep(array1, k, n)

def rep(array, k, n):
	for j in range(k, n-1):
		temp2 = array[j]
		array[j] = array[j+1]
		array[j+1] = temp2
		print(array)
		if k==1:
			return
		else:
			rep(array, k-1, n)


def recursive_permutations(p, i, n, res):
    if i == n:
        res.append(tuple(p))
    else:
        for x in range(1, n + 1):
            if x not in p:
                p[i] = x
                recursive_permutations(p, i + 1, n, res)
                p[i] = 0


def permutations(n):
    p = [0] * n
    res = []
    recursive_permutations(p, 0, n, res)
    print(res)
    return res