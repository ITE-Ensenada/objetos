class Dog:
	especie = "perros"
	def __init__(self,name,age):
		self.nombre = name
		self.edad = age
	def ladra(self):
		print("gua gua")

perrito = Dog("Laika", 12)
print(perrito)
print(perrito.nombre)
perrito.ladra()