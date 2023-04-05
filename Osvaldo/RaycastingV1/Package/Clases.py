class Player:
    def __init__(self, posX, posY, angle, fov):
        self._posX = posX
        self._posY = posY
        self._angle = angle
        self._fov = fov
        self._halfFOV = fov / 2

    @property
    def fov(self):
        return self._fov

    @property
    def halfFOV(self):
        return self._halfFOV

    @property
    def fov(self):
        return self._fov
    
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self._angle += value
    
    @property
    def posX(self):
        return self._posX
    
    @posX.setter
    def posX(self, value):
        self._posX += value
    
    @property
    def posY(self):
        return self._posY
    
    @posY.setter
    def posY(self, value):
        self._posY += value
