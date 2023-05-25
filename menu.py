#ejemplo de invocacion de funciones
def menu():
    print("menu")
def opcion1():
    print("opcion 1")
def opcion2():
    print("opcion 2")
seleccion = [menu,opcion1,opcion2]
opc = seleccion[i]
opc()
eval("opcion2"+"()")

