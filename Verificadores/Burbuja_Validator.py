elementos = [3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,78,90,-0,
-21,3, 1, 8,19,14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32
,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,
23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 
19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,
4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 
1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,
0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,
3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,
0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 
1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,
4,7,2,3,23,45,54,62,3, 1, 8, 19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62,3, 1, 8, 
19, 14,32,1,2,786,0,-1,4,7,2,3,23,45,54,62]

def burbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                

#burbuja(elementos)
def verificador1(arreglo):
    n = len(arreglo)
    for i in range(n-1):
        if arreglo[i] > arreglo[i+1]:
            return False
    return True

print("Verificador1: ¿El arreglo  está ordenado?", verificador1(elementos))


def verificador2(arreglo):
	i=1
	Orden = True
	while i < len(arreglo):
		if arreglo[i-1] > arreglo[i]:
			Orden=False
		i+=1
	if Orden == True:
		print("Verficador2: Los elementos estan orden")
	else:
		print("Verficador2: Los elementos estan desorden")

#burbuja(elementos)
verificador1(elementos)
verificador2(elementos)

#Quitando el simbolo '#' a burbuja(elementos) devuelve true