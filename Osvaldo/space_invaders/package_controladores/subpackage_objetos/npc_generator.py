'''Descripcion: Este archivo contiene la clase NpcGenerator,
                la cual se encarga de generar los nps'''

import pygame
from game_data.general_settings.settings import ALTO, NPC_INTERVAL
from package_controladores.subpackage_objetos.npc import Npc

class NpcGenerator:
    '''Clase que se encarga de generar npc's y de sus patrones y ataques'''

    def __init__(self, game):

        self.game = game # Instancia de la clase game

        self.npc_list = pygame.sprite.Group() # Lista de enemigos

        self.last_wave = 0 # TIempo de la ultima wave de enemigos


    def generate_wave(self,):
        pass