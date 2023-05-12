"Programa que busca, ordena y borra posiciones en un arreglo"
arreglo = [1,3,3,4,5,6,7,8]
seleccion = int(input("Que es lo que desea hacer? "))
if seleccion > 4:
    print("Ingrese un numero valido")
else:
    if seleccion == 1:
        print("Decidiste dejar el arreglo igual")
        print(arreglo)
    elif seleccion == 2:
        print("Arreglo original: ")
        print(arreglo)
        lugar = int(input("A que lugar desea agregar un nuevo numero? "))
        nuevo_numero = int(input("Que numero deseas agregar? "))
        if lugar <= len(arreglo):
            arreglo.insert(lugar, nuevo_numero)
        else:
            arreglo.append(nuevo_numero)
        print(arreglo)
    elif seleccion == 3:
        print("Arreglo original: ")
        print(arreglo)
        borrar = int(input("Que posicion desea borrar? "))
        if borrar >= len(arreglo):
            print("Ingrese un valor valido, ya que este no existe")
        else:
            arreglo.pop(borrar)
            print("Su nuevo arreglo es: ", arreglo)
    elif seleccion == 4:
        posiciones = []
        print("Arreglo original: ")
        print(arreglo)
        localizador = int(input("Qué número desea ubicar? "))
        if localizador in arreglo:
            for i, posicion in enumerate(arreglo):
                if posicion == localizador:
                    posiciones.append(i)
            print("Número:", localizador, "se ubica en las siguientes posiciones:")
            for posicion in posiciones:
                print(posicion)
        else:
            print("El número no se encuentra en el arreglo")
            
