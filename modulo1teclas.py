# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
 
# creating a running loop
while True:
       
    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            # checking if key "A" was pressed
            if event.key == pygame.K_UP:
                print("Key UP has been pressed")
               
            # checking if key "J" was pressed
            if event.key == pygame.K_DOWN:
                print("Key DOWN has been pressed")
               
            # checking if key "P" was pressed
            if event.key == pygame.K_LEFT:
                print("Key LEFT has been pressed")
             
            # checking if key "M" was pressed
            if event.key == pygame.K_RIGHT:
                print("Key RIGHT has been pressed")