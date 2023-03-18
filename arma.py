class arma:
    tipo: "espada magica"
    def __init__(self, name, poder):
        self.nombre = name
        self.magia = poder
        self.ataque = 5
        self.resistencia = 10/30
        self.rango = 2
        
    def __str__(self):
        print("Hola aventurero soy:")
        return f"{self.nombre} mi magia es {self. magia}!"
    def saludo(self):
        print("Hola aventurero! Juntos derrotaremos a los malos")

if __name__ == '__main__': 
 magia = "fuego de dragon" 
 nombre = input('Como quieres llamar a tu espada, recuerda que un arma digna debe tener un nombre digno!:')
 espada = arma(nombre, magia)
 print(espada)
 commando = ""
 while (commando!="exit"):
		commando = input('-->')
		if commando == "hola":
			 espada.saludo()
		print(commando)
