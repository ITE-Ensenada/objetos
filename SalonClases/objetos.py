class Personaje:
	especie = "humanoide"
	def __init__(self,name,age):
		self.nombre = name
		self.edad = age
		self.fuerza = 10
		self.nivel = 0
		self.caminar = 3
		self.ataque = 2

	def __str__(self):
		return f"{self.nombre} HOLA {self.especie}"

	def camina(self):
		print("camina " + str(self.caminar))

	def ataca(self):
		return self.ataque

if __name__ == '__main__':  
	nombre = input('Ingresa tu nombre tio: ')
	edad = input('Dame tu edad : ')
	jugador1 = Personaje(nombre, edad)
	print(jugador1)
	commando = ""
	while (commando!="exit"):
		commando = input('-->')
		if commando == "camina":
			jugador1.camina()
		print(commando)
