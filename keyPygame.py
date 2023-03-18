
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
            if event.key == pygame.K_a:
                print("Key A has been pressed")
               
        # checking if key "B" was pressed
            if event.key == pygame.K_b:
                print("Key B has been pressed")
               
        # checking if key "C" was pressed
            if event.key == pygame.K_c:
                print("Key C has been pressed")

        # checking if key "D" was pressed
            if event.key == pygame.K_d:
                print("Key D has been pressed")

        # checking if key "E" was pressed
            if event.key == pygame.K_e:
                print("Key E has been pressed")       

        # checking if key "F" was pressed
            if event.key == pygame.K_f:
                print("Key F has been pressed")

        # checking if key "G" was pressed
            if event.key == pygame.K_g:
                print("Key G has been pressed")       

        # checking if key "H" was pressed
            if event.key == pygame.K_h:
                print("Key H has been pressed")
        # checking if key "I" was pressed
            if event.key == pygame.K_i:
                print("Key I has been pressed")       

        # checking if key "J" was pressed
            if event.key == pygame.K_j:
                print("Key J has been pressed")
        # checking if key "K" was pressed
            if event.key == pygame.K_k:
                print("Key K has been pressed")       

        # checking if key "L" was pressed
            if event.key == pygame.K_l:
                print("Key L has been pressed")

        # checking if key "M" was pressed
            if event.key == pygame.K_m:
                print("Key M has been pressed")       

        # checking if key "N" was pressed
            if event.key == pygame.K_n:
                print("Key N has been pressed")