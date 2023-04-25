import random, math

tipos = ["Acero","Agua","Bicho","Dragon","Electrico","Fantasma","Fuego","Hada","Hielo","Lucha","Normal","Planta","Psiquico","Roca","Siniestro","Tierra","Veneno","Volador"]

#vertical↓ = tipo del atacante, horizontal→ = tipo del receptor
tabla = [[0.5,0.5,1,1,0.5,1,0.5,2,2,1,1,1,1,2,1,1,1,1],
		[1,0.5,1,0.5,1,1,2,1,1,1,1,0.5,1,2,1,2,1,1],
		[0.5,1,1,1,1,0.5,0.5,0.5,1,0.5,1,2,2,1,2,1,0.5,0.5],
		[0.5,1,1,2,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
		[1,2,1,0.5,0.5,1,1,1,1,1,1,0.5,1,1,1,0,1,2],
		[1,1,1,1,1,2,1,1,1,1,0,1,2,1,0.5,1,1,1],
		[2,0.5,2,0.5,1,1,0.5,1,2,1,1,2,1,0.5,1,1,1,1],
		[0.5,1,1,2,1,1,0.5,1,1,2,1,1,1,1,2,1,0.5,1],
		[0.5,0.5,1,2,1,1,0.5,1,0.5,1,1,2,1,1,1,2,1,2],
		[2,1,0.5,1,1,0,1,0.5,2,1,2,1,0.5,2,2,1,0.5,0.5],
		[0.5,1,1,1,1,0,1,1,1,1,1,1,1,0.5,1,1,1,1],
		[0.5,2,0.5,0.5,1,1,0.5,1,1,1,1,0.5,1,2,1,2,0.5,0.5],
		[0.5,1,1,1,1,1,1,1,1,2,1,1,0.5,1,0,1,2,1],
		[0.5,1,2,1,1,1,2,1,2,0.5,1,1,1,1,1,0.5,1,2],
		[1,1,1,1,1,2,1,0.5,1,0.5,1,1,2,1,0.5,1,1,1],
		[2,1,0.5,1,2,1,2,1,1,1,1,0.5,1,0.5,1,1,0.5,0],
		[0,1,1,1,1,0.5,1,2,1,1,1,2,1,0.5,1,0.5,0.5,1],
		[0.5,1,2,1,0.5,1,1,1,1,2,1,2,1,0.5,1,1,1,1]]

movimientosdisponibles = [["Terremoto",15,100,"Fisico"],
						["Cascada",1,80,"Fisico"],
						["Puño Hielo",8,75,"Fisico"],
						["Demolicion",15,75,"Fisico"],
						["Patada Ignea",6,85,"Fisico"],
						["Lanzallamas",6,90,"Especial"],
						["Avanlancha",13,75,"Fisico"],
						["Energibola",11,90,"Especial"],
						["Hoja Aguda",11,90,"Fisico"],
						["Puntada Sombria",5,80,"Fisico"],
						["Tajo Aereo",17,75,"Especial"],
						["Golpe Cuerpo",10,75,"Fisico"],
						["Bomba Germen",11,75,"Fisico"]]
class Pokemon:
	def __init__(self):
		self.nivel = 50

	def stats(self):
		print("Pokemon:",self.nombre)
		print("Tipo 1:",tipos[self.tipo1])
		if self.tipo2 != 18:
			print("Tipo 2:",tipos[self.tipo2])
		print("Nivel:",self.nivel)
		print("Vida:",self.vida)
		print("Defensa:",self.defensa)
		print("Velocidad:",self.velocidad)
		print("Ataque Especial:",self.atespecial)
		print("Defensa Especial:",self.dfespecial)
		print("movimiento 1:",movimientosdisponibles[self.movimientos[0]][0],"Tipo",tipos[movimientosdisponibles[self.movimientos[0]][1]],"Potencia",movimientosdisponibles[self.movimientos[0]][2],"Categoria",movimientosdisponibles[self.movimientos[0]][3])
		print("movimiento 2:",movimientosdisponibles[self.movimientos[1]][0],"Tipo",tipos[movimientosdisponibles[self.movimientos[1]][1]],"Potencia",movimientosdisponibles[self.movimientos[1]][2],"Categoria",movimientosdisponibles[self.movimientos[1]][3])
		print("movimiento 3:",movimientosdisponibles[self.movimientos[2]][0],"Tipo",tipos[movimientosdisponibles[self.movimientos[2]][1]],"Potencia",movimientosdisponibles[self.movimientos[2]][2],"Categoria",movimientosdisponibles[self.movimientos[2]][3])
		print("movimiento 4:",movimientosdisponibles[self.movimientos[3]][0],"Tipo",tipos[movimientosdisponibles[self.movimientos[3]][1]],"Potencia",movimientosdisponibles[self.movimientos[3]][2],"Categoria",movimientosdisponibles[self.movimientos[3]][3])

	def pelea(self,movimientoausar,agresor,victima):
		print(self.nombre, "a usado", movimientosdisponibles[movimientoausar][0])
		multiplicador = tabla[movimientosdisponibles[movimientoausar][1]][victima.tipo1]
		if victima.tipo2 != 18:
			multiplicador = multiplicador*tabla[movimientosdisponibles[movimientoausar][1]][victima.tipo2]
		if multiplicador >= 2:
			print("Es supereficaz")
		elif multiplicador <= 0.5:
			print("Es poco eficaz")
		if movimientosdisponibles[movimientoausar][1] == agresor.tipo1 | movimientosdisponibles[movimientoausar][1] == agresor.tipo2:
			multiplicador = multiplicador*1.5
		if movimientosdisponibles[movimientoausar][3] == "Fisico":
			dano = ((((2*agresor.nivel/5+2)*agresor.ataque*movimientosdisponibles[movimientoausar][2]/victima.defensa)/50)+2)*multiplicador*random.randrange(85,100,1)/100
		critico = random.randrange(0,80,1)
		if critico >= 76:
			dano = dano*2
			print("Golpe critico")
		victima.vida = victima.vida-math.floor(dano)
		print(victima.vida)

class Swampert(Pokemon):
	def __init__(self):
		super().__init__()
		self.nombre = "Swampert"
		self.tipo1 = 1
		self.tipo2 = 15
		self.vida = 175
		self.ataque = 130
		self.defensa = 110
		self.velocidad = 80
		self.atespecial = 105
		self.dfespecial = 110
		self.movimientos = [0,1,2,3]


class Blaziken(Pokemon):
	def __init__(self):
		super().__init__()
		self.nombre = "Blaziken"
		self.tipo1 = 6
		self.tipo2 = 9
		self.vida = 155
		self.ataque = 140
		self.defensa = 90
		self.velocidad = 100
		self.atespecial = 130
		self.dfespecial = 90
		self.movimientos = [4,5,6,3]

class Decidueye(Pokemon):
	def __init__(self):
		super().__init__()
		self.nombre = "Decidueye"
		self.tipo1 = 11
		self.tipo2 = 5
		self.vida = 153
		self.ataque = 127
		self.defensa = 95
		self.velocidad = 90
		self.atespecial = 120
		self.dfespecial = 120
		self.movimientos = [7,8,9,10]

class Snorlax(Pokemon):
	def __init__(self):
		super().__init__()
		self.nombre = "Snorlax"
		self.vida = 235
		self.tipo1 = 10
		self.tipo2 = 18
		self.ataque = 130
		self.defensa = 85
		self.velocidad = 50
		self.atespecial = 85
		self.dfespecial = 130
		self.movimientos = [0,6,11,12]