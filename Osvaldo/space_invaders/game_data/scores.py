'''Descripcion: '''

import os

class ScoresManager:
    '''Clase'''

    def __init__(self, game):
        self.game = game
        self.__file_path = 'game_data/highscore.txt'
        self.score = self.search_highscore_file()
        self.temp_score = 0

        
    def search_highscore_file(self):
        '''Metodo que busca el archivo highscore.txt'''

        if os.path.exists(self.get_path):
            with open(self.get_path, "r") as file:
                for line in file:
                    score = int(line.strip())
                    return score
        else:
            self.generate_highscore_file()
            self.search_highscore_file()

            
    def generate_highscore_file(self):
        '''Metodo que genera un archivo con extension .txt para guardar los highscores del juego'''

        with open(self.get_path, 'w') as file:
            file.write('0')

    def add_points_asteroid(self):
        self.temp_score += 9

        
    def save_high_scores(self):
        '''Metodo que guarda el puntaje del juego si este mismo supera el record'''

        if self.temp_score > self.score:
            with open(self.get_path, 'w') as file:
                file.write(str(self.temp_score))

    @property
    def load_high_score(self):
        return self.score
        
    @property
    def get_path(self):
        return self.__file_path


#-------------------------------------------------------------------------------------------------------------------------------


    def test(self):
        '''Funcion de prueba'''
