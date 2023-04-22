class Character:
	def __init__(self, name, age, speed, dodge, damage, stamina, strength, height, skinColor):
		self.name = name
		self.age = age
		self.speed = speed
		self.dodge = dodge
		self.damage = damage
		self.health = 13
		self.stamina = stamina
		self.strength = strength
		self.height = height
		self.skinColor = skinColor

# ****** METHODS ******

	# Presentation

	def showCharacter(self):
		print("Presentando a: \n" "Nombre: " + self.name, "\nEdad: " + self.age, "\n")
		print("Caracteristicas: \n" "Velocidad: " + self.speed, "\nSalud: ", self.health, "\nAltura: " + self.height, 
			"\nColor de piel: " + self.skinColor)
		print("Habilidades: \n" "Esquiva: " + self.dodge, "\nDaño: " + self.damage,
		 "\nEstamina: " + self.stamina, "\nFuerza: " + self.strength)

	def checkHealth(self):

		if (self.health < 15) and (self.health > 10): print("Salud baja")
		elif self.health <= 7: print("Tienes", + self.health, "de vida \nTe estas desangrando, CURATE!!")



		

# *********************