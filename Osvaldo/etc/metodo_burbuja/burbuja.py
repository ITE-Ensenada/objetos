import random



def burbuja(arreglo):
    '''Ordena un arreglo de menor a mayor'''

    longitud = len(arreglo)

    for i in range( longitud - 1 ):
        for j in range( i+1, longitud ):

            if arreglo[i] > arreglo[j]:

                temp = arreglo[i]

                arreglo[i] = arreglo[j]

                arreglo[j] = temp


    print(arreglo)



def verificador1(arreglo):
    '''Verifica si el arreglo esta ordenado de menor a mayor, si no lo esta, manda a llamar al metodo burbuja'''

    print(arreglo)

    for i in range( len(arreglo) - 1):
        print('\nCiclo: ', (i+1))

        if arreglo[i] > arreglo[(i+1)]:

            burbuja(arreglo)
            break

        else:

            print('No se efectuo metodo de la burbuja.\nIndice i: ', arreglo[i],'Indice j: ', arreglo[(i+1)])

def verificador0(arreglo):
    '''Verifica si el arreglo esta ordenado de menor a mayor, si no lo esta, manda a llamar al metodo burbuja'''

    print(arreglo)

    for i in range( len(arreglo) - 1):

        if arreglo[i] > arreglo[(i+1)]:

            burbuja(arreglo)
            break


def add_int_number1(arreglo, numero):
    '''Agrega un numero al arreglo'''

    arreglo_nuevo = [None] * ( len(arreglo) + 1 ) # Se inicializa un arreglo vacio con 1 valor mas del arreglo original
    longitud = len( arreglo )

    for index in range( longitud ):
        '''Casos posibles
        1. El numero es menor o igual que el primer valor del arreglo
        2. El numero es mayor o igual que el ultimo valor del arreglo
        3. El numero esta entre el primer y ultimo valor del arreglo'''

        if numero < arreglo[0]:
            arreglo_nuevo[0] = numero
            arreglo_nuevo[index + 1] = arreglo[index]

        elif arreglo[ longitud - 1 ] < numero:
            arreglo_nuevo[ longitud ] = numero
            arreglo_nuevo[index] = arreglo[index]

        else:
            arreglo_nuevo[index] = arreglo[index]

            if arreglo[index] <= numero <= arreglo[index + 1]:

                arreglo_nuevo[index + 1] = numero

                for jndex in range( index + 1, longitud ):

                    arreglo_nuevo[jndex + 1] = arreglo[jndex]

                break

    print(arreglo_nuevo)

def add_int_number2(arreglo, numero):
    '''Agrega un numero al arreglo'''

    arreglo_nuevo = [None] * ( len(arreglo) + 1 ) # Se inicializa un arreglo vacio con 1 valor mas del arreglo original
    longitud = len( arreglo )
    verificador = False

    for index in range( longitud ): # Este metodo es lento
        '''Casos posibles
        1. El numero es menor que el primer valor del arreglo
        2. El numero es mayor que el ultimo valor del arreglo
        3. El numero esta entre el primer y ultimo valor del arreglo'''
        

        # Caso 1
        if numero < arreglo[0]:
            arreglo_nuevo[0] = numero
            arreglo_nuevo[index + 1] = arreglo[index]

        # Caso 2
        elif arreglo[ longitud - 1 ] < numero:
            arreglo_nuevo[ longitud ] = numero
            arreglo_nuevo[index] = arreglo[index]

        # Caso 3
        else:
            print(arreglo_nuevo, arreglo)

            if verificador == True:
                print("Entro al if verificador = true")
                arreglo_nuevo[index + 1] = arreglo[index]

            else:
                print("Entro al if verificador = false")
                arreglo_nuevo[index] = arreglo[index]


            if arreglo[index] <= numero <= arreglo[index + 1]:
                print("Entro al if")
                arreglo_nuevo[index + 1] = numero
                verificador = True
                print(verificador)



    print(arreglo_nuevo)


def generar_numeros(cantidad):
    '''Genera numeros pseudoaleatorios entre una cantidad dada, y los almacena en un arreglo'''

    arreglo = []

    for contador in range(cantidad):
        arreglo.append(random.randint(0,12))

    return arreglo



if __name__ == '__main__':

    #cantidad = random.randint(0,12)

    #arreglo = generar_numeros( cantidad )

    arreglo = [0,2,3,1,2,1,4]

    verificador0(arreglo)

    #verificador1(arreglo)
    
    #add_int_number1(arreglo, 4)
    
    #add_int_number2(arreglo, 4)