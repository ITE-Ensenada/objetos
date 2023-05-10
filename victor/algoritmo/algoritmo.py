"aqui estara la clase algoritmo"
import itertools

class Algoritmo:
    "clase para poder brindar listas de combinaciones, permutaciones y permutaciones repetidas"
    def combinaciones(self, arreglo):
        "Devuelve una lista con todas las combinaciones posibles de los elementos del arreglo"
        return list(itertools.combinations(arreglo, 2))
    def permutaciones(self, arreglo):
        "Devuelve una lista con todas las permutaciones posibles de los elementos del arreglo"
        return list(itertools.permutations(arreglo))
    def permutacionesrepeat(self, arreglo):
        """(Devuelve una lista con todas las permutaciones posibles de los elementos del 
        arreglo permitiendo repetición"""
        return list(itertools.product(arreglo, repeat=2))
