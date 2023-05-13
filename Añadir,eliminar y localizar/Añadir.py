with open("Elementos.txt", "r") as archivo:
    elementos = archivo.read()

elementos = elementos.split(",")
elementos = [int(elemento) for elemento in elementos]

print("Esta es la lista:",elementos)

def añadir(elementos):
    numero=int(input("Que numero quieres añadir? "))
    #numero=2
    elementos.append(numero)
    for i in range(len(elementos)-1):
        for j in range(len(elementos)-1):
            if elementos[j] > elementos[j+1]:
                elementos[j],elementos[j+1]=elementos[j+1],elementos[j]   

def borrar(elementos):
    localizacion=0
    numero=int(input("Que numero quieres eliminar? "))              
    elementos.remove(numero)
    print(elementos)

def localizar(elementos):
    n=len(elementos)
    localizacion=0
    contador=0
    #numero=5
    numero=int(input("Que numero quieres localizar? "))
    for i in list(elementos):
        localizacion+=1
        if i == numero:
            print("El numero esta en la posicion: ",localizacion)
        else:
            contador+=1
    if contador == n:
        print("No se encontro el numero que quieres localizar")

bucle = True
while bucle == True:
    print("1. Añadir un numero a la lista")
    print("2. Borrar un numero a la lista")
    print("3. Localizar un numero a la lista")
    hacer = int(input("Que le quieres hacer a la lista? "))
    if hacer == 1:
        añadir(elementos)
        print(elementos)
    if hacer ==2:
        borrar(elementos)
    if hacer ==3:
        localizar(elementos)
    if hacer >3: 
        print("No selecionaste una funcion")


