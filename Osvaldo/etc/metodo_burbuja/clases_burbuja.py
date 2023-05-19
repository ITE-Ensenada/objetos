class Producto:


    def __init__(self, arreglo):
        self.arreglo = arreglo


    def burbuja(self):
        '''Ordena un arreglo de menor a mayor'''

        longitud = len(self.arreglo)

        for i in range( longitud - 1 ):
            for j in range( i+1, longitud ):

                if self.arreglo[i] > self.arreglo[j]:

                    temp = self.arreglo[i]

                    self.arreglo[i] = self.arreglo[j]

                    self.arreglo[j] = temp


    def verificador0(self):
        '''Verifica si el arreglo esta ordenado de menor a mayor, si no lo esta, manda a llamar al metodo burbuja'''

        for i in range( len(self.arreglo) - 1):

            if self.arreglo[i] > self.arreglo[(i+1)]:

                self.burbuja()
                break


    def add_int_number3(self, value):
        '''Agrega un numero al arreglo'''

        arreglo_nuevo = [None] * (len(self.arreglo) + 1)
        inserted = False
        index_nuevo = 0

        for num in self.arreglo:
            
            if not inserted and num > value:
                arreglo_nuevo[index_nuevo] = value
                inserted = True
                index_nuevo += 1
            
            arreglo_nuevo[index_nuevo] = num
            index_nuevo += 1

        if not inserted:
            arreglo_nuevo[index_nuevo] = value

        self.arreglo = arreglo_nuevo


    def delete_int_number0(self, value):
        '''Elimina un numero del arreglo'''

        arreglo_nuevo = [None] * ( len(self.arreglo) - 1 ) # Se inicializa un arreglo vacio con 1 valor menos del arreglo original
        longitud = len( self.arreglo ) - 1
        jndex = 0
        deleted = False

        for index in range(longitud):
            if self.arreglo[index] == value:
                jndex += 1
                deleted = True
            arreglo_nuevo[index] = self.arreglo[jndex]
            jndex += 1

        if not deleted:
            if self.arreglo[longitud] == value:
                arreglo_nuevo[longitud - 1] = self.arreglo[longitud]
            else:
                print('El numero no se encuentra en el arreglo')


    def run(self):

        print(self.arreglo)
        self.verificador0()
        print(self.arreglo)

        self.add_int_number3(14)
        print(self.arreglo)

        self.delete_int_number0(14)
        print(self.arreglo)





array = [1,3,2,4,5,6,7,0]

objeto = Producto(array)

objeto.run()