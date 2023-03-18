class personaje:
    especie = "dragon"
    def __init__(self ,name):
        self.nombre = name
        self.edad = 100
        self.traje = "capa sanadora"
        self.fuerza = 7
        self.tipo = "cambiaformas"
        self.magia = "fuego"
        self.ataque = 6
        self.caminar = 2
        self.poder = 6

    def __str__(self):
        return f"{self.nombre} eres un {self.especie}"

    def saludo(self):
        print("Quiero ir a casa...")
    
if __name__ == '__main__':  
	nombre = input('Dime tu nombre: ')
	jugador = personaje(nombre)
	print(jugador)
	commando = ""
	while (commando!="exit"):
		commando = input('-->')
		if commando == "hola":
			jugador.saludo()
		print(commando)



    


