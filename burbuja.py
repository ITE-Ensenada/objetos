def burbuja(lista):
    cuando = len(lista)
    for i in range(cuando):
        for actual in range(cuando - 1):
            siguiente_elemento = actual + 1
            if lista[actual] > lista[siguiente_elemento]:
                lista[siguiente_elemento], lista[actual] = lista[actual], lista[siguiente_elemento]
  


# Se usa de esta manera.
mi_lista = [16, 4, 29, 5, 9, 22, 23, 3, 7, 8]
print("Original: ")
print(mi_lista)
burbuja(mi_lista)
print("Ordenado: ")
print(mi_lista)