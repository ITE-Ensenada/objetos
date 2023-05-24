"""clase para crear el tablero"""
import numpy as np
N_FILAS = 6
N_COLUMNAS = 7
class Tableroparajugar:
    """clase para crear tablero"""
    def crear_tablero() -> np.ndarray:
        """aqui creamos el tablero con ayuda de libreria numpy"""
        tablero = np.zeros((N_FILAS, N_COLUMNAS))
        return tablero
    