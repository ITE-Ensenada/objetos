'''Hace que se mueva creo xd'''
from librerias.personaje import goku, vegeta
class Rect:
    '''se mueve'''
    def __init__(self, rect, eje_x, eje_y):
        self.rect=rect
        self.rect.x=eje_x
        self.rect.y=eje_y
    def update(self, vel, rect):
        '''se mueve mas xd'''
        self.rect.x-= vel
        return rect

muve_goku=Rect(goku.img.get_rect(), 10, 10)
muve_vegeta=Rect(vegeta.img.get_rect(), 1000, 600)
