class Weapon:
	def __init__(self, weaponType, damage, firemode, fireDistance, material):
		self.weaponType = weaponType 
		self.damage = damage
		self.firemode = firemode
		self.fireDistance = fireDistance

class Melee(Weapon):
	def __init__(self, weaponType, damage, firemode, fireDistance, material, width, height):
		super().__init__(weaponType, damage, firemode, fireDistance, material)


# *************** Melee Weapons (Cuerpo a cuerpo) ****************

class Axe(Melee):
	pass

class Sword(Melee):
	pass

class Knife(Melee):
	pass

class Boxers(Melee):
	pass

# *****************************************************************

class Pistol(Weapon):
	