'''Descripcion: Este archivo contiene la clase HostileObjectsManager,
                la cual se encarga de manejar los objetos hostiles contra el jugador'''

from package_controladores.subpackage_objetos.asteroid_generator import AsteroidGenerator
from package_controladores.subpackage_objetos.npc_generator import NpcGenerator

class HostileObjectsManager:
    '''Clase que se encarga de manejar los objetos hostiles contra el jugador'''''
    
    def __init__(self, game):
        
        self.game = game # Instancia de la clase Game

        self.asteroid_generator = AsteroidGenerator(self.game) # Instancia de la clase AsteroidGenerator
        self.npc_generator = NpcGenerator(self.game) # Instancia de la clase NPCGenerator
    
    def update(self):
        '''Metodo que se encarga de actualizar los objetos hostiles'''
        
        self.asteroid_generator.update()
        self.npc_generator.update()