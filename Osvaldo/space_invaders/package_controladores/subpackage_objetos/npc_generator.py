'''Descripcion: Este archivo contiene la clase NpcGenerator,
                la cual se encarga de generar los nps'''

import pygame
import random
from game_data.general_settings.settings import(
    ANCHO,
    ALTO,
    NPC_HEIGHT,
    NPC_WIDTH,
    NPC_INTERVAL,
    WAVE_ROWS_SIZE,
    WAVE_COLUMN_SIZE)   
from package_controladores.subpackage_objetos.npc import Npc

class NpcGenerator:
    '''Clase que se encarga de generar npc's y de sus patrones y ataques'''

    def __init__(self, game):

        self.game = game # Instancia de la clase game

        self.npc_list = pygame.sprite.Group() # Lista de enemigos

        self.last_wave = 0 # TIempo de la ultima wave de enemigos

        self.wave_pattern = self.generate_pattern() # Patrones de oleadas

        self.wave_rows_size = WAVE_ROWS_SIZE # Tamaño de la oleada

        self.do = True

    def generate_pattern(self):
        '''Generar patrones de oleadas'''

        pattern = [[random.randint(0, 1) for i in range(int(WAVE_COLUMN_SIZE))] for j in range(int(WAVE_ROWS_SIZE))]

        return pattern

    def spawn_enemy_wave(self):
        '''Generar oleada de enemigos'''
        spacing_vertical = 2
        spacing_horizontal = 4
        x_offset =( (ANCHO - (NPC_WIDTH + spacing_horizontal) * WAVE_COLUMN_SIZE) // 2 )
        y_offset = -NPC_HEIGHT - spacing_vertical  # Para hacer spawn fuera de la pantalla

        for i in range(int(WAVE_ROWS_SIZE)):
            for j in range(int(WAVE_COLUMN_SIZE)):
                if self.wave_pattern[i][j] == 1:
                    x = x_offset + j * (NPC_WIDTH + spacing_horizontal)
                    y = y_offset + i * (NPC_HEIGHT + spacing_vertical)
                    npc = Npc(self.game, x, y)
                    self.npc_list.add(npc)


        

    def generate_enemies(self, index):
        npc = Npc(self.game, index * 48, 50)
        self.npc_list.add(npc)

    def eliminate_npc(self):
        for npc in self.npc_list:
            if npc.life <= 0:
                self.game.score_manager.add_points_npc()

            elif (npc.life <= 0 
                or npc.rect.top >= ALTO):
                npc.kill()

    def update(self):
        '''Actualizar generador de npc's'''
        if self.do:
            self.spawn_enemy_wave()
            self.do = False
        self.npc_list.update() # Actualizar npc's