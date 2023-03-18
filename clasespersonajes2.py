class personaje:
    def __init__(self,stamina,nombre,ataque):

        self.stamina = stamina
        self.nombre = nombre
        self.ataque = ataque

class power:
    def __init__(self,damg, type, cost, cd):

        self.damg = damg
        self.type = type
        self.cost = cost
        self.cd = cd 

class armor:
    def __init__(self,armor,type):

        self.armor = armor
        self.type = type