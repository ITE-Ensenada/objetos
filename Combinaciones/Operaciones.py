import itertools

class Combinaciones:
    def calcular(self, numeros, r):
        resultado = list(itertools.combinations(numeros, r))
        return resultado

class Permutaciones:
    def permutar(self, numeros):
        resultado = list(itertools.permutations(numeros))
        return resultado
    
class Permutacion_Repeat: 
    def repeat(self, numeros, r):
        resultado = list(itertools.product(numeros, repeat=r))
        return resultado
 