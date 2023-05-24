"main menu"
from buscar import localizar
from eliminar import verificar
from agregar import agregar_elementos
from burbuja import verificador
#from extras import eliminar_espacios
class principal:
    '''clase principal'''
    elementos = [1,2,8,4,7,6,3]
    def __init__(self):
        '''operaciones que se pueden realizar con el arreglo'''
        self.opciones = {
            "buscar": self.buscar_numero,
            "eliminar": self.eliminar_numero,
            "agregar": self.agregar_numero,
            "ordenar": self.ordenar_arreglo,
            "salir": self.salir_menu
        }

    def inicio(self):
        '''despliega el menu de opciones'''
        elementos = principal.elementos
        while True:
            print("Lista de Elementos:\n",elementos,"\nQue operacion desea realizar??:\n")
            print("-Buscar\n-Eliminar\n-Agregar\n-Ordenar\n-Salir\n")
            respuesta = input("Respuesta:   ")
            if respuesta in self.opciones:
                self.opciones[respuesta]()
            else:
                print("escoge una opcion valida")
                input("precione enter para continuar...")


    def buscar_numero(self):
        '''busca la direccion de un elemento del arreglo'''
        elementos = principal.elementos
        print("lista de elementos:\n",elementos)
        buscar = float(input(" ingrese el numero que desea buscar: "))
        resultado = localizar(elementos,buscar)
        if not resultado:
            print("el numero no se encuentra dentro del arreglo")
            input("precione enter para continuar...")
        else:
            print("El numero se encuentra en las posiciones: \n",resultado)
            input("precione enter para continuar...")

    
        
    def eliminar_numero(self):
        '''elimina un numero del arreglo'''
        elementos = principal.elementos
        numero_eliminar = float(input("ingrese el numero que desee eliminar: "))
        elementos = verificar(elementos,numero_eliminar)
        if elementos:
            print("El elemento se ha eliminado\n",elementos)
            input("precione enter para continuar...")
        else:
            print("El elemento no se encuentra en el arreglo\n")
            input("precione enter para continuar...")

    def agregar_numero(self):
        '''agrega elementos al arreglo'''
        elementos = principal.elementos
        numero_acomodar =float(input(" introduce un numero: "))
        elementos = agregar_elementos(numero_acomodar,elementos)
        print(elementos)
        input("precione enter para continuar...")

    def ordenar_arreglo(self):
        '''ordena el arreglo'''
        elementos = principal.elementos
        verifica = verificador(elementos)
        if verifica:
            print("Numeros ordenados: ",elementos)
        else:
            print(" los numeros ya estan ordenados ")

            input("precione enter para continuar...")

    def salir_menu(self):
        '''cierra el programa'''
        print(" Salir ")
        exit()


menu = principal()
menu.inicio()
