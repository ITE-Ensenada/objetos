def burbuja(arreglo):
        n = len(arreglo)
        for i in range(n-1):     
            for j in range(i+1,n): 
                if arreglo[i] > arreglo[j]:
                    temp = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = temp
                   
        return arreglo
def add():
    def agregar(archivo):
        with open( archivo, "a") as f:
            texto = input("datos a agregar: ")
            print(f"nuevos datos: ", texto)
            texto = ", " + texto
            datos = f.write(texto)
            f.close()
            with open(archivo,'r') as f:
                leer = f.read()
            print("nuevo contenido: \n", leer)
            f.close()
            #n = len(arreglo)
            #print(n)

    def arreglo(archivo):
        global arreglo
        global f
        with open(archivo,'r') as f:
            contenido = f.read().split(',')
            #print('contenido: ', contenido)
            arreglo=[int(x) for x in contenido]
            #print('arreglo resultante: ', arreglo)
            x = burbuja(arreglo)
            print("arreglo: ", x)
            f.close()

    

                

    archivo = input("nombre del archivo: ")
    agregar(archivo)
    arreglo(archivo)
    x = burbuja(arreglo)
    print(x)
add()
