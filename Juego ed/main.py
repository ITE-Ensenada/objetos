import pygame
from pygame.locals import *
from config import *
from sprites import *
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

pygame.display.set_caption("Earthbound chafa")

icon= pygame.image.load('icon.png')

pygame.display.set_icon(icon)
class Game:
   def __init__(self):
     pygame.init()
     self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
     self.clock = pygame.time.Clock()
     self.running=True

   def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1,2)

   def events(self):
       
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             self.playing=False
             self.running=False

   def update(self):
       self.all_sprites.update()

   def draw(self):
       self.screen.fill(BLUE)
       self.all_sprites.draw(self.screen)
       self.clock.tick(FPS)
       pygame.display.update()
   def main(self):
       while self.playing:
          self.events()
          self.update()
          self.draw()
          self.running = False

   def game_over(self):
       pass
   def intro_screen(self):
      pass

g = Game()
g.intro_screen()
g.new()
while g.running:
       g.main()
       g.game_over()

       pygame.quit()
       