"""este programa lee datos de un archivo, y les realiza permutaciones y combinaciones
con una catidad de elementos elegida por el usuario"""
#pylint: disable=E1101
def factorial(x):
    """funcion que calcula factoriales"""
    resultado=1
    while(x > 1): 
        resultado*=x 
        x-=1
    return resultado 

class Arreglo(object):
    """clase para las combinaciones y permutaciones"""
    def numero_combinaciones(n,r):
        """metodo para calcular el numero de combinaciones"""
        factorialn=factorial(n)
        factorialr=factorial(r)
        factorialnr=factorial(n-r)
        resultado=factorialn/(factorialr*factorialnr)
        print("Combinaciones encontradas:",int(resultado))

    def combinaciones(lista,n,r,permutacion,posicion,empieza):
        """metodo para calcular las combinaciones"""
        if r>0:
            for i in range(empieza,n):
                permutacion[posicion]=lista[i]
                Arreglo.combinaciones(lista,n,r-1,permutacion,posicion+1,empieza+1)
                empieza+=1
        else:
            print(permutacion) 
		
    def numero_permutaciones(n,r):
        """metodo para calcular el numero de permutaciones"""
        factorialn=factorial(n)
        factorialnr=factorial(n-r)
        resultado=factorialn/factorialnr
        print("Permutaciones encontradas:",int(resultado))

    def permutaciones(lista,n,r,permutacion,posicion):
        """metodo para calcular las permutaciones"""
        if r>0:
            for i in range(n):
                bandera=1
                for j in range(len(permutacion)-1):
                    if permutacion[j]==lista[i]:
                        bandera=0
                if bandera==1:
                    permutacion[posicion]=lista[i]
                    Arreglo.permutaciones(lista,n,r-1,permutacion,posicion+1)
        else:
            print(permutacion) 
          
    def permutaciones_repe(lista,n,r,permutacion,posicion,contador):
        """metodo para calcular el numero de permutaciones con repeticiones y desplegarlas"""
        if r>0:
            for i in range(n):
                permutacion[posicion]=lista[i]
                contador=Arreglo.permutaciones_repe(lista,n,r-1,permutacion,posicion+1,contador)
        else:
            print(permutacion)
            contador=contador+1
        return contador  

archivo = open("texto.txt", "r")
lista = archivo.read().split(',')
tamaño = len(lista)
for i in range(tamaño):
    lista[i] = int(lista[i])
print("introduce un numero mayor a 0, y menor o igual que",tamaño)
eleccion=input()
lista2=[]
for i in range(eleccion):
    lista2.append("a")
contador=0
print("combinaciones")

Arreglo.combinaciones(lista,tamaño,eleccion,lista2,0,0)
Arreglo.numero_combinaciones(tamaño,eleccion)
print("Permutaciones")
Arreglo.permutaciones(lista,tamaño,eleccion,lista2,0)
Arreglo.numero_permutaciones(tamaño,eleccion)
print("Permutaciones con repeticion")
contador=Arreglo.permutaciones_repe(lista,tamaño,eleccion,lista2,0,contador)
print("Permutaciones con repeticion encontradas",contador)
archivo.close()
