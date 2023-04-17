class Character:
	def __init__(self, name, age, speed, dodge, damage, health, stamina, strength, height, skinColor):
		self.name = name
		self.age = age
		self.speed = speed
		self.dodge = dodge
		self.damage = damage
		self.health = health
		self.stamina = stamina
		self.strength = strength
		self.height = height
		self.skinColor = skinColor

# ****** METHODS ******

	# Presentation

	def showCharacter(self):
		print("Presentando a: \n" "Nombre: " + self.name, "\nEdad: " + self.age, "\n")
		print("Caracteristicas: \n" "Velocidad: " + self.speed, "\nSalud: " + self.health, "\nAltura: " + self.height, 
			"\nColor de piel: " + self.skinColor)
		print("Habilidades: \n" "Esquiva: " + self.dodge, "\nDaño: " + self.damage,
		 "\nEstamina: " + self.stamina, "\nFuerza: " + self.strength)

# *********************