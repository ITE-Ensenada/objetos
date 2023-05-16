def arreglo(archivo):
    with open( archivo, "a") as f:
        texto = input("datos a agregar: ")
        print(f"nuevos datos: ", texto)
        datos = f.write(texto)
        f.close()
        with open(archivo,'r') as f:
            leer = f.read()
        print("nuevo contenido: \n", leer)
        f.close()
        #n = len(arreglo)
        #print(n)

archivo = input("nombre del archivo: ")
arreglo(archivo)