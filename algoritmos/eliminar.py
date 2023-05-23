
def arreglo(archivo):
    global arreglo
    global f
    with open(archivo,'r') as f:
        contenido = f.read().split(',')
        #print('contenido: ', contenido)
        arreglo=[int(x) for x in contenido]
        print('arreglo resultante: ', arreglo)
        f.close()
def delete(arreglo): 
    e = int(input("dato a eliminar: "))
    arreglo.remove(e)
    print("nuevo arreglo: ",arreglo)

archivo = input("nombre del archivo: ")
arreglo(archivo)
delete(arreglo)
