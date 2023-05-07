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

def burbuja(elementos):
	for i in range(len(elementos)-1):
		for j in range(len(elementos)-1):
			if elementos[j] > elementos[j+1]:
				elementos[j],elementos[j+1]=elementos[j+1],elementos[j]

def verificador1(elementos):
	Orden = True
	n = len(elementos)
	for i in range(n-1):
		for j in range(i+1,n):
			if elementos[i] > elementos[j]:
				Orden = False
	if Orden == True:
		print("Verficador1: Los elementos estan orden")
	else:
		print("Verficador1: Los elementos estan desorden")

def verificador2(elementos):
	i=1
	Orden = True
	while i < len(elementos):
		if elementos[i-1] > elementos[i]:
			Orden=False
		i+=1
	if Orden == True:
		print("Verficador2: Los elementos estan orden")
	else:
		print("Verficador2: Los elementos estan desorden")

#burbuja(elementos)
verificador1(elementos)
verificador2(elementos)








