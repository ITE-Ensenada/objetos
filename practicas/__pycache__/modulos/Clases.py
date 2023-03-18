class Personaje:
	especie = "humanoide"
	def __init__(self, nombre, edad):
		self.name = nombre
		self.age = edad
		self.fuerza = 10
		self.nivel = 1
		self.magia = 0
		self.velocidad = 5
		self.armadura = 10
		self.resistencia_magica = 10
		self.mana = 80
		self.vida = 120
		self.posicionX = 10
		self.posicionY = 10
		self.height = 50
		self.width= 50

	def __str__(self):
		return f"hola {self.name}, el {self.especie}"

	def sonido(self):
		print("*corrido tumbado*")

class equipamiento:
	tipo = "mochila"
	def __init__(self):
		self.espacio = 60
		self.tiposdeobjeto = 0

class objetos:
	tipo = "pocion de vida"
	def __init__(self):
		self.potencia = 30
		