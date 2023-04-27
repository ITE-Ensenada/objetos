"""este archivo contiene clases y arreglos que hacen que funcione el sistema de batallas"""
import random
import math
#          0        1      2       3          4           5        6       7      8       9       10       11        12       13        14        15       16       17
tipos = ["Acero","Agua","Bicho","Dragon","Electrico","Fantasma","Fuego","Hada","Hielo","Lucha","Normal","Planta","Psiquico","Roca","Siniestro","Tierra","Veneno","Volador"]

#vertical↓ = tipo del atacante, horizontal→ = tipo del receptor
#         0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17
tabla =[[0.5,0.5, 1 , 1 ,0.5, 1 ,0.5, 2 , 2 , 1 , 1 , 1 , 1 , 2 , 1 , 1 , 1 , 1 ],#0
        [ 1 ,0.5, 1 ,0.5, 1 , 1 , 2 , 1 , 1 , 1 , 1 ,0.5, 1 , 2 , 1 , 2 , 1 , 1 ],#1
        [0.5, 1 , 1 , 1 , 1 ,0.5,0.5,0.5, 1 ,0.5, 1 , 2 , 2 , 1 , 2 , 1 ,0.5,0.5],#2
        [0.5, 1 , 1 , 2 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],#3
        [ 1 , 2 , 1 ,0.5,0.5, 1 , 1 , 1 , 1 , 1 , 1 ,0.5, 1 , 1 , 1 , 0 , 1 , 2 ],#4
        [ 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 , 1 , 1 , 0 , 1 , 2 , 1 ,0.5, 1 , 1 , 1 ],#5
        [ 2 ,0.5, 2 ,0.5, 1 , 1 ,0.5, 1 , 2 , 1 , 1 , 2 , 1 ,0.5, 1 , 1 , 1 , 1 ],#6
        [0.5, 1 , 1 , 2 , 1 , 1 ,0.5, 1 , 1 , 2 , 1 , 1 , 1 , 1 , 2 , 1 ,0.5, 1 ],#7
        [0.5,0.5, 1 , 2 , 1 , 1 ,0.5, 1 ,0.5, 1 , 1 , 2 , 1 , 1 , 1 , 2 , 1 , 2 ],#8
        [ 2 , 1 ,0.5, 1 , 1 , 0 , 1 ,0.5, 2 , 1 , 2 , 1 ,0.5, 2 , 2 , 1 ,0.5,0.5],#9
        [0.5, 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ,0.5, 1 , 1 , 1 , 1 ],#10
        [0.5, 2 ,0.5,0.5, 1 , 1 ,0.5, 1 , 1 , 1 , 1 ,0.5, 1 , 2 , 1 , 2 ,0.5,0.5],#11
        [0.5, 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 1 ,0.5, 1 , 0 , 1 , 2 , 1 ],#12
        [0.5, 1 , 2 , 1 , 1 , 1 , 2 , 1 , 2 ,0.5, 1 , 1 , 1 , 1 , 1 ,0.5, 1 , 2 ],#13
        [ 1 , 1 , 1 , 1 , 1 , 2 , 1 ,0.5, 1 ,0.5, 1 , 1 , 2 , 1 ,0.5, 1 , 1 , 1 ],#14
        [ 2 , 1 ,0.5, 1 , 2 , 1 , 2 , 1 , 1 , 1 , 1 ,0.5, 1 ,0.5, 1 , 1 ,0.5, 0 ],#15
        [ 0 , 1 , 1 , 1 , 1 ,0.5, 1 , 2 , 1 , 1 , 1 , 2 , 1 ,0.5, 1 ,0.5,0.5, 1 ],#16
        [0.5, 1 , 2 , 1 ,0.5, 1 , 1 , 1 , 1 , 2 , 1 , 2 , 1 ,0.5, 1 , 1 , 1 , 1 ]]#17

movimientosarre = [["Terremoto",15,100,"Fisico"],#0
                    ["Cascada",1,80,"Fisico"],#1
                    ["Puño Hielo",8,75,"Fisico"],#2
                    ["Demolicion",9,75,"Fisico"],#3
                    ["Patada Ignea",6,85,"Fisico"],#4
                    ["Lanzallamas",6,90,"Especial"],#5
                    ["Avanlancha",13,75,"Fisico"],#6
                    ["Energibola",11,90,"Especial"],#7
                    ["Hoja Aguda",11,90,"Fisico"],#8
                    ["Puntada Sombria",5,80,"Fisico"],#9
                    ["Tajo Aereo",17,75,"Especial"],#10
                    ["Golpe Cuerpo",10,75,"Fisico"],#11
                    ["Bomba Germen",11,75,"Fisico"]]#12
class Pokemon:
    def __init__(self):
        self.nivel = 50
        self.nombre = "pokemon"
        self.tipo1 = 1
        self.tipo2 = 18
        self.vida = 1
        self.vida_actual = 1
        self.ataque = 1
        self.defensa = 1
        self.velocidad = 1
        self.atespecial = 1
        self.dfespecial = 1
        self.movimientos = [0,1,2,3]

    def stats(self):
        texto1 = "Tipo 1: "+tipos[self.tipo1]
        if self.tipo2 != 18:
            texto1 = texto1 +" Tipo 2: "+tipos[self.tipo2]
        texto2 = "Ataque: "+str(self.ataque)
        texto3 = "Defensa: "+str(self.defensa)
        texto4 = "Ataque Especial: "+str(self.atespecial)
        texto5 = "Defensa Especial: "+str(self.dfespecial)
        texto6 = "Velocidad: "+str(self.velocidad)
        return texto1,texto2,texto3,texto4,texto5,texto6

    def pelea(self,movimientoausar,agresor,victima):
        texto = ""
        dano=0
        multiplicador = tabla[movimientosarre[movimientoausar][1]][victima.tipo1]
        if victima.tipo2 != 18:
            multiplicador = multiplicador*tabla[movimientosarre[movimientoausar][1]][victima.tipo2]
        if multiplicador >= 2:
            texto = "Es supereficaz "
        elif multiplicador <= 0.5:
            texto = "Es poco eficaz "
        if movimientosarre[movimientoausar][1] == agresor.tipo1 | movimientosarre[movimientoausar][1] == agresor.tipo2:
            multiplicador = multiplicador*1.5
        dano = math.floor((2*agresor.nivel/5+2))
        if movimientosarre[movimientoausar][3] == "Fisico":
            dano = math.floor(dano*(agresor.ataque*movimientosarre[movimientoausar][2]/victima.defensa))
        else:
            dano = math.floor(dano*(agresor.atespecial*movimientosarre[movimientoausar][2]/victima.dfespecial))
        dano = math.floor(dano/50)
        dano = math.floor(dano+2)
        dano = math.floor(dano*multiplicador*random.randrange(85,100,1)/100)
        critico = random.randrange(0,80,1)
        if critico >= 76:
            dano = dano*2
            texto = texto+"¡GOLPE CRITICO!"
        victima.vida_actual = victima.vida_actual-dano
        texto2 = victima.nombre+" a recibido "+str(dano)+" de daño"
        return texto,texto2
class Swampert(Pokemon):
    def __init__(self):
        super().__init__()
        self.nombre = "Swampert"
        self.tipo1 = 1
        self.tipo2 = 15
        self.vida = 175
        self.vida_actual = 175
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
        self.vida_actual = 155
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
        self.vida_actual = 153
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
        self.tipo1 = 10
        self.tipo2 = 18
        self.vida = 235
        self.vida_actual = 235
        self.ataque = 130
        self.defensa = 85
        self.velocidad = 50
        self.atespecial = 85
        self.dfespecial = 130
        self.movimientos = [0,6,11,12]
