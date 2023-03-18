class Personaje: 
    especie: "jugador_1"
    def __init__(self, name, age, sex, hp, stamina, classes, race, height, complex, color_hair):
        self.nombre = name
        self.edad = age
        self.vida = 200
        self.estamina = 20
        self.clase = classes
        self.raza = race
        self.altura = 150
        self.complexion = complex
        self.cabello = color_hair 
        self.genero = sex
        
class Armas: 
    tipo: "alabarda"
    def __init__(self, dimensions, damage, material, weight):
        self.dimensiones=dimensions
        self.danio=damage
        self.material= material
        self.peso=weight

    tipo: "espadon"
    def __init__(self, dimensions, damage, material, weigth):
        self.dimensiones= 80
        self.danio=50
        self.material= "acero"
        self.peso=90

    tipo: "mangual"
    def __init__(self, dimensions, damage, material, weigth):
        self.dimensiones= 90 
        self.danio=30
        self.material= "acero oxidado"
        self.peso=60
