def verificador2(arreglo):
    if arreglo == sorted(arreglo):
        print("Ordenado")
    else:
        print("No ordenado")

elementos = [2,3,4,65,3,21,4,45,76,89,8,98,9]
verificador2(elementos)