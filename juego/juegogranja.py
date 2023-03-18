class Personaje:
	especie = "humanoide"
	def __init__(self,name,age,traj,alm,habil,ar,cab):
		self.nombre = name
		self.edad = age
		self.traje = traj
		self.mochila = alm
		self.herramientas= ar
		self.corazones = 7
		self.habilidades = habil
		self.cabello= cab
		self.dinero= 10
		self.resistencia = 5
		self.nivel = 0
		self.camina = 3
		self.ataque = 2
class mochila:
	def __init__(self, colores):
		self.tamano = 7
		self.color = colores

class herramientas:
	tipo = "regadera"
	def __init__(self, mat):
		self.capacidad = 5
		self.material = mat
		self.cansancio = 0

class traje:
	def __init__(self,c,protec):
		self.color = c
		self.proteccion  = protec


	 

	def __str__(self):
		return f"{self.nombre} HOLA {self.especie}"

	def camina(self):
		print("camina " + str(self.caminar))

	def ataca(self):
		return self.ataque

if __name__ == '__main__':  
	nombre = input('Ingresa tu nombre tio: ')
	edad = input('Dame tu edad : ')
	cabello = input('de que color es tu cabello')
	habilidades = input('Que habilidad deseas tener?')
	jugador1 = Personaje(nombre, edad, cabello,habilidades, traje, mochila, herramientas,)

	print(jugador1)
	commando = ""
	while (commando!="exit"):
		commando = input('-->')
		if commando == "camina":
			jugador1.camina()
		print(commando)

