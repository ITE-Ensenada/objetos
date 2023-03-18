class Personaje:
	especie = "Puca"
	def __init__(self,name,age,piel,vida,pelota,fuerza,nivel,caminar):
		self.nombre = name
		self.edad = age
		self.piel = rojo
		self.vida = 10
		self.pelota = ball
		self.fuerza = 10
		self.nivel = 0
		self.caminar = 3

	def __str__(self):
		return f"{self.nombre} Hola {self.especie}"

	def camina(self):
		print("camina " + str(self.caminar))

	def ataca(self):
		return self.ataque

if __name__ == '__main__':  
	nombre = input('Puca dice que ingreses tu nombre: ')
	edad = input('A Puca le interesa tu edad: ')
	jugador1 = Personaje(nombre, edad)
	print(jugador1)
	commando = ""
	while (commando!="exit"):
		commando = input('-->')
		if commando == "camina":
			jugador1.camina()
		print(commando) 
