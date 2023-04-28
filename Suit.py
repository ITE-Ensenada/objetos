# pylint: disable=C0103

'''
    El modulo Suit:

    26/04/2023

    En este modulo se agregaran
    una gran variedad de clases
    derivadas de la clase principal(padre)
    Clothes
'''

class Clothes:
    '''
    Esta es la clase principal (padre):
    contiene todos los atributos GENERALES
    que poseen las prendas de vestir como
    color, textura o estilo
    '''
    def __init__(self, color, texture, style):
        self.color = color
        self.texture = texture
        self.style = style
class Suit(Clothes):
    '''
    Siendo una clase hija, hereda los tres atributos
    posteriores, pero, tratandose de un traje, este
    incluye otros tres atributos que no cualquiera
    prenda de vestir posee.
    '''
    def __init__(self, color, texture, style, ab, botones, corbata):
        super().__init__(color,texture,style)
        self.anti_balas = ab # ab = anti balas
        self.botones = botones
        self.corbata = corbata
    def show_suit(self):
        '''
    		Otro metodo simple, solamente para
            mostrarle al jugador los trajes que
            estan disponibles
    	'''
        print("\nColor de traje:", self.color, "\nTextura: ",self.texture,
            "\nEstilo del traje: ",self.style, "\nAnti-Balas:", + self.anti_balas,
			"\nNumero de botones:", + self.botones, "\nCorbata:", self.corbata)
