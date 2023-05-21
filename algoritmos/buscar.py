def posiciones(arreglo):
   #a es igual al elemento a buscar 
    a = float(input("Numero a buscar: "))
    search=""
    for i in range(len(arreglo)):
        if arreglo[i]==a:
            search=search+ str(i)
            #print("search ",search)
    if search == "":
        search = print("no esta tu elemento")
    else:
        search = print("se encontro en la posicion ", search)
    #return search


elementos = [1,2,3,4,16]
posicion=posiciones(elementos)

