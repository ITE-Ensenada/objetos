'''este programa elimina un elemento del arreglo'''
elementos = [1,2,3,4,5,7,8,10]
def recorrer(arreglo):
    '''recorre el arreglo y elimina los espacios vacios'''
    espacios = len(arreglo)
    vacios = espacios-1
    j=0
    for i in range(espacios-1):
        if arreglo[i] == '':
            j = i + 1
            arreglo[i] = arreglo[j]
            arreglo[j] = ''
    nuevoarreglo =  arreglo[:vacios]
    return nuevoarreglo

def eliminar(arreglo, numero):
    '''elimina el numero del arreglo'''
    espacio = len(arreglo)
    for i in range(espacio-1):
        if arreglo[i] == numero:
            arreglo[i] = ''

def verificar(arreglo,numero):
    '''verifica que el numero se encuentre en el arreglo'''
    espacio = len(arreglo)
    j = 0
    for i in range(espacio):
        if arreglo[i] == numero:
            j = 1
    return j

print(elementos)
numero_eliminar = float(input("ingrese el numero que desee eliminar: "))
revisar = verificar(elementos,numero_eliminar)
if revisar == 1:
    eliminar(elementos,numero_eliminar)
    nuevo_arreglo = recorrer(elementos)
    print(nuevo_arreglo)
else:
    print("el numero ingresado no se encuentra en el arreglo")
