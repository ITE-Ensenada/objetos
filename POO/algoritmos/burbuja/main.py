from burbuja import Burbuja
from agregar import Add
from buscar import Search, Find
from eliminar import Delete
loop=1
#Se declara arreglo
arreglo=[1, 32, 33, 4, 54, 11, 23, 41, 21, 21, 3, 32, 222, 49, 82]
#Se imprime
print("Este es el arreglo original: ", arreglo)
#Lo quiere ordenar??
print("Deseas ordenarlo? \n 1=Si	0=No")
ordena = int(input())
#Si lo quiso ordenar? :)
if ordena:
	Burbuja(arreglo)
	print("Tu arreglo ya esta ordenado \n",arreglo)
while(loop):
	#opciones que hacer
	print("Que quieres hacer? \n 1=Agregar un numero \n 2=Eliminar un numero \n 3=Buscar un numero \n 4=Salir \n (ingresa la opcion deseada) \n")
	do = int(input())
	if (do==1):
		print("Ingresa un numero a agregar")
		num = float(input())
		arreglo = Add(arreglo, num)
		print(arreglo)
	elif do==2:
		print("Ingresa el numero a eliminar")
		num = float(input())
		if not Find(arreglo,num):
			print("No existe ese numero")		
		arreglo=Delete(arreglo, num)
		print(arreglo)
	elif do==3:
		print("Ingresa el numero a buscar")
		num = float(input())
		Search(arreglo, num)
	elif do==4:
		print("No vuelvas pronto, gracias :) <3")
		loop=0
	else: 
		print("No existe la eleccion, vuelve en una semana a ver si el David ya hace la tarea")

