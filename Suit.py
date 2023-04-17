
# Clase Padre
class Clothes:
	def __init__(self, color, texture, style):
		self.color = color
		self.texture = texture
		self.style = style

# ********* METHODS **************




# ********************************		

class Suit(Clothes):

	def __init__(self, color, texture, style, ab, botones, corbata): 
		super().__init__(color, texture, style)

		self.ab = ab # ab = anti-balas
		self.botones = botones
		self.corbata = corbata

# ********* METHODS **************

	def MostrarSuit(self):
		print("\nColor de traje:", self.color, "\nTextura: ",self.texture, "\nEstilo del traje: ",self.style, "\nAnti-Balas:", + self.ab, 
			"\nNumero de botones:", + self.botones, "\nCorbata:", self.corbata)






# ********************************	

traje1 = Suit("Rojo", "Kevlar", "Corte Ingles", True, 2, "Negra") # True = 1, False = 0 (Estos valores se imprimen)
traje1.MostrarSuit() 


class Shoes(Clothes):
	def __init__(self, color, texture, style):
		super().__init__(color, texture, style)

# ********* METHODS **************







# ********************************	

class GLoves(Clothes):
	def __init__(self, color, texture, style):
		super().__init__(color, texture, style)

 
# ********* METHODS **************







# ********************************	


class Accesories(Clothes):
	def __init__(self, color, texture, style):
		super().__init__(color, texture, style)