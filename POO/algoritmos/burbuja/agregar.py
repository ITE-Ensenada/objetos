def Add(array, num):
    n = len(array) #tamaño total deln arreglo
    mitad = n//2 #punto medio en el arreglo
    half1 = array[ :mitad] #new array of 0-mitad = half1
    half2 = array[mitad: ] #new array of mitad-n = half1
   
    if num<=array[mitad]: #juega con half1 
        half1 = where(num, half1)
        array=half1+half2 #Rearmar el array partido con el nuevo elemento
        return array
    else :#juega con half2 
        half2 = where(num, half2)
        array=half1+half2 #Rearmar el array partido con el nuevo elemento
        return array

def where(num, mitad):
    if num>=mitad[-1]:#agrega al ultimo
        mitad.append(num)
    elif num<=mitad[0]:#agrega al principio
        mitad=[num, *mitad]
    else: 
        mitad=Add(mitad, num) #Recursividad para volver a partirlo y encontrar el lugar exacto
    return mitad
