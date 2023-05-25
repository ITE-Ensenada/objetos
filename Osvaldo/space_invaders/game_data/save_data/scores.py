'''Descripcion: Clase que maneja los puntajes del juego'''

import os

class ScoresManager:
    '''Clase que maneja los puntajes del juego'''

    def __init__(self, game):
        self.game = game
        self.__file_path = 'game_data/save_data/high_score.txt'
        self.score = None
        self.search_high_score_file()
        self.temp_score = 0


    def search_high_score_file(self):
        '''Metodo que busca el archivo highscore.txt'''

        if os.path.exists(self.get_path):
            self.score = self.get_score_from_txt()
        else:
            self.generate_high_score_file()
            self.score = self.get_score_from_txt()


    def get_score_from_txt(self):
        '''Metodo que obtiene el puntaje del archivo highscore.txt'''

        with open(self.get_path, "r") as file:
            for line in file:
                score = int(line.strip())
            file.close()
            return score

    def generate_high_score_file(self):
        '''Metodo que genera un archivo con extension .txt para guardar los highscores del juego'''

        with open(self.get_path, 'w') as file:
            file.write('0')
            file.close()

    def add_points_asteroid(self):
        self.temp_score += 9


    def save_high_scores(self):
        '''Metodo que guarda el puntaje del juego si este mismo supera el record'''

        if self.temp_score > self.score:
            with open(self.get_path, 'w') as file:
                file.write(str(self.temp_score))
                file.close()

    @property
    def load_high_score(self):
        '''Metodo que carga el puntaje del juego'''

        return self.score

    @property
    def get_path(self):
        '''Metodo que retorna la ruta del archivo highscore.txt'''

        return self.__file_path
