def verificador1(arreglo):
    n = len(arreglo)
    for i in range(n-1):
        for j in range(i+1,n):
            # si encuentra un error
            if arreglo[i] > arreglo[j]:
                return False
    return True
elementos = [2,3,4,65,3,21,4,45,76,89,8,98,9]
verifica = verificador1(elementos)

if verifica:
    print("Ordenado")
else: 
    print("No ordenado")