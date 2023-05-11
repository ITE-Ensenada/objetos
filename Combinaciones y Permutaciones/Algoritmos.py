with open("Elementos.txt", "r") as archivo:
    elementos = archivo.read()

elementos = elementos.split(",")
elementos = [int(elemento) for elemento in elementos]

def burbuja(elementos):
	for i in range(len(elementos)-1):
		for j in range(len(elementos)-1):
			if elementos[j] > elementos[j+1]:
				elementos[j],elementos[j+1]=elementos[j+1],elementos[j]

def permutacion(elementos):
	y=0
	for i in list(elementos):
		for j in list(elementos):
			for m in list(elementos):
				print(i,j,m)
				y+=1
	print("Permutaciones totales: ",y)	

def permutacionRep(elementos):
	y=0
	for i in list(elementos):
		for j in list(elementos):
			for m in list(elementos):
				if j or m == i:
					print(i,j,m)
					y+=1
	print("Permutaciones con repeticion totales: ",y)			

def combinaciones(elementos):
	y=0
	for i in list(elementos):
		for j in list(elementos):
			for m in list(elementos):
				print(i,j,m)
				print(j,i,m)
				print(m,j,i)
				print(j,m,i)
				y+=4
	print("Combinaciones totales: ",y)			

print("1. Ordenarlos")
print("2. Permutacion")
print("3. Permutacion con repeticion")
print("4. Conbinarlos")
accion = int(input("Que le quieres hacer a los numeros?: "))

if accion == 1:
	burbuja(elementos)
	print(elementos)
if accion == 2:
	permutacion(elementos)
if accion == 3:
	permutacionRep(elementos)
if accion == 4:
	combinaciones(elementos)

#burbuja(elementos)
#print(elementos)

#permutacion(elementos)

#permutacionRep(elementos)

#combinaciones(elementos)