 #decorador que da la introducción a las caracteristicas del personaje
def introducciones(introduccion):
    def inicio():

        print("A continuacion se mostraran las caracteristicas del pesonaje:")

        introduccion()
            
    return inicio

#atributos base de cualquier personaje jugable o no jugable
class Personaje:
    especie = "jugador_1"
    
    def __init__(self, sex, hp, name):
        self.sexo = sex
        self.vida = hp
        self.nombre = name

#caracteristicas del enemigo
class Enemigo(Personaje):
    def __init__(self, sex, hp, name, weapon, classes, defect, loot):
        super().__init__(sex, hp, name)
        self.arma = weapon
        self.clase = classes
        self.defectos = defect
        self.botin = loot

    def mostrar_caracteristicas(self): #muestra las caracteristicas del enemigo
        print(f"ENEMIGO\nsexo = {self.sexo}\nVida = {self.vida}\nName = {self.nombre}\nArma = {self.arma}\nClase = {self.clase}\nDefectos = {self.defectos}\nBotín = {self.botin}\n")

#caracteristicas del jugador
class Jugador(Personaje):
    def __init__(self, sex, hp, name, stamina, race, weight, height, color_hair):
        super().__init__(sex, hp, name)
        self.estamina = stamina
        self.raza = race
        self.peso = weight
        self.altura = height
        self.pelo = color_hair

    def mostrar_caracteristicas(self): #muestra las caracteristicas del jugador
        print(f"JUGADOR\nsexo = {self.sexo}\nVida = {self.vida}\nNombre = {self.nombre}\nEstamina = {self.estamina}\nRaza = {self.raza}\nPeso = {self.peso}\nAltura = {self.altura}\nPelo = {self.pelo}")


class Armas:
    tipo = "alabarda"
    
    def __init__(self, dimensions, damage, material, weight):
        self.dimensiones = dimensions
        self.danio = damage
        self.material = material
        self.peso = weight


class Espadon(Armas):
    tipo = "espadon"
    
    def __init__(self, dimensions, damage, material, weight):
        super().__init__(dimensions, damage, material, weight)
        self.dimensiones = 80
        self.danio = 50
        self.material = "acero"
        self.peso = 90


class Mangual(Armas):
    tipo = "mangual"
    
    def __init__(self, dimensions, damage, material, weight):
        super().__init__(dimensions, damage, material, weight)
        self.dimensiones = 90
        self.danio = 30
        self.material = "acero oxidado"
        self.peso = 60