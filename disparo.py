# pylint: disable=too-few-public-methods
class Arma:
    """Te dice las especificaciones de un arma"""
    arma = "Dispara"
    def __init__(self, danio, cadencia):
        self.damage = danio
        self.caden = cadencia

    def accion(self):
        """Muestra el daño de un arma"""
        print(f"Daño = {self.damage}\nCadencia: {self.caden}")

class Disparo(Arma):
    """Tipo de arma especial que dispara 3 balas"""
    triple_bala = "Tres balas en una"
    def __init__(self, danio, cadencia):
        super().__init__(danio, cadencia)
        self.tiempo = 20
