class world: 
    tipo = "tablero"
    def __init__(self,norte,sur,este,oeste):
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste 


class pieza:
    tipo = "peon"
    def __init__(self):
        self.caminar = 2
        self.retroceder = 0
        self.ataque = 1 
    tipo = "rey"
    def __init__(self):
        self.caminar = 1
        self.retroceder = 1
        self.ataque = 1
    tipo = "reyna"
    def __init__(self):
        self.caminar = 8
        self.retroceder = 8
        self.ataque = 8
    tipo = "torre"
    def __init__(self):
        self.caminar = 8
        self.retroceder = 8
        self.ataque = 8
    tipo = "alfil"
    def __init__(self):
        self.caminar = 7
        self.retroceder = 7
        self.ataque = 7
    tipo = "caballo"
    def __init__(self):
        self.caminar = 3
        self.retroceder = 3
        self.ataque = 3
    


