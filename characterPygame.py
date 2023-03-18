class Personaje:
    especie = "Gato"
    def __init__(self, name, age, piel, estatura, curacion):
        self.nombre = name
        self.edad = age
        self.color = piel
        self.height = estatura
        self.vida = 20
        self.curacion = curacion
        self.fuerza = 7
        self.armadura = 10
        self.velocidad = 1.5
        self.blockhit = False
        self.caminar = 3


class Weapons:
    tipo = "espada"
    def __init__(self, dimensiones, damage):
        self.dimensiones = dimensiones
        self.damage = damage
        self.mejora = False
        self.reach = 3
    tipo = "hacha"
    def __init__(self, dimensiones, damage):
        self.dimensiones = dimensiones
        self.damage = damage
        self.reach = 2

