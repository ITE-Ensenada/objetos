# pylint: disable=C0103

'''
    El modulo Weapon:

    26/04/2023

    Contiene una clase padre y una clase hija
    Ambas incluyen metodos

    En este modulo se van a derivar diversas clases hijas
    de la clase padre(Weapon) para que el jugador tenga diversas
    opciones a escoger en el modulo main
'''
# pylint: disable=C0103

class Weapon:
    '''
    Esta es la clase principal (padre):
    contiene todos los atributos GENERALES que posee
    un arma
    '''
    def __init__(self, weapon_type, damage, firemode, fire_distance, material):
        self.weapon_type = weapon_type
        self.damage = damage
        self.firemode = firemode
        self.fire_distance = fire_distance
        self.material = material

    def show_weapon(self):
        '''
            Este metodo de igual forma, le muestra
            al jugador las caracteristicas de las armas
            de tal manera que pueda tener informacion
            detallada y seleccione la que mejor
            le convenga
        '''
        print(self.weapon_type, self.damage, self.firemode,
              self.fire_distance, self.material)

class Melee(Weapon):
    '''
    En esta clase se agregan dos atributos
    ancho y alto, tratandose de armas melees
    se usan estos atributos en caso como
    hachas, katanas, etc.
    '''
    def __init__(self, weaponType, damage, firemode, fire_distance, material, width, height):
        super().__init__(weaponType, damage, firemode, fire_distance, material)
        self.width = width
        self.height = height


# *************** Melee Weapons (Cuerpo a cuerpo) ****************

class Axe(Melee):
    '''
    la clase hacha tendra metodos como:
    dimensiones, rango de ataque, etc
    '''
    def dimensiones(self):
        '''
        En este metodo solo vamos a
        colocar valores predeterminados
        a nuestra arma cuerpo a cuerpo
        '''
        self.width = 15
        self.height = 20

class Pistol(Weapon):
    '''
    Esta clase hereda exactamente todos
    los atributos de la clase principal
    '''
    def shoot(self):
        '''
            Este metodo indica que se esta disparando el arma

            (Luego se implementara un algoritmo para saber
            en que momentos usar este metodo)
        '''
        print("Pew pew")
