class Personaje:
	especie = "humanoide"
	def __init__(self,nombre,edad,traje,habilidad,mochila):
		self.nombre = nombre
		self.edad = edad
		self.traje = traje
		self.mochila = mochila
		self.corazones = 7
		self.habilidad = habilidad
		self.dinero= 10
		self.resistencia = 5
		self.nivel = 0
		self.camina = 3
		self.ataque = 2
		
class mochila:
	def __init__(self, color):
		self.tamano = 7
		self.color = color

class herramientas: 
	def __init__(self,tipo):
		self.tipo = tipo
		self.poder = 0
		self.cansancio = 0 

class traje:
	def __init__(self):
		self.proteccion  = 2



if __name__ == '__main__':  
	nombre = input('Ingresa tu nombre tio: ')
	edad = input('Dame tu edad : ')
	habilidades = input('Que habilidad deseas tener?: ')
	jugador1 = Personaje(nombre, edad, habilidades, traje, mochila)

	print(jugador1)


