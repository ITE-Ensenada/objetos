
def burbuja(lista):
    cuando = len(lista)
    for i in range(cuando):
        for actual in range(cuando - 1):
            siguiente_elemento = actual + 1
            if lista[actual] > lista[siguiente_elemento]:
                lista[siguiente_elemento], lista[actual] = lista[actual], lista[siguiente_elemento]
  


mi_lista = [7, 41, 16, 8, 10, 2, 29, 9, 33, 5]
print("Arreglo Original: ")
print(mi_lista)
burbuja(mi_lista)
print("Arreglo Ordenado: ")
print(mi_lista)