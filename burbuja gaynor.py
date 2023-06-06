def bubble_sort(arr):
    n = len(arr)
    cont = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            cont += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, cont

elementos = [4, 6, 1, 12, 9]

print("Números a ordenar:", elementos)
arreglo, cont = bubble_sort(elementos)
print(f"Números ordenados en {cont} ciclos:", arreglo)