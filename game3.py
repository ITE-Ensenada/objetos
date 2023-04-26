'''
Created on Feb 8, 2022

@author: songzhao
'''

import pygame, random, sys

# define coordinate x, y axis value range.
X_MIN = 0
Y_MIN = 0 
# the maximize number of pixel units.
X_MAX = 100
Y_MAX = 100

# define the pygame app main window surface object.
MAIN_WINDOW_SURFACE = None

# define the pixel number in one pixel rectangle unit.
PIXEL_UNIT_WIDTH = 15
PIXEL_UNIT_HEIGHT = 15

# True: means draw the pixel unit use the pygame.PixelArray object.
# False: means draw the pixel unit use the pygame.draw.rect() method.
DRAW_PIXEL_UNIT_BY_PIXEL_ARRAY = False
#DRAW_PIXEL_UNIT_BY_PIXEL_ARRAY = True

# create a pygame.time.Clock object.
FPS_CLOCK = pygame.time.Clock()

# this method will initialize the pygame application.
def initialize_pygame():
    
    pygame.init()
    
    # create the game main window.
    main_window_size = (X_MAX, Y_MAX)
    
    global MAIN_WINDOW_SURFACE
    MAIN_WINDOW_SURFACE = pygame.display.set_mode(main_window_size, pygame.RESIZABLE)
    #MAIN_WINDOW_SURFACE = pygame.display.set_mode(main_window_size)
        
    print('MAIN_WINDOW_SURFACE.get_size() = ', MAIN_WINDOW_SURFACE.get_size())
    
    # set the window title.
    window_title = 'Pygame Draw Pixels Example.'
    pygame.display.set_caption(window_title)
    

# this method will return a color value from the color list randomly.
def get_random_color():
    
    # create a color list that contains 7 colors.
    color_list = (pygame.Color('red'), pygame.Color('yellow'), pygame.Color('blue'), pygame.Color('green'), pygame.Color('orange'), pygame.Color('black'), pygame.Color('purple'))
    # choose one color randomly.
    random_color = random.choice(color_list)
    
    return random_color


# this method will draw multiple pixel units use the pygame.draw.Rect() method.
def draw_pixels_by_draw_rect():
    
    pixels_list = build_random_number_pair_list()
    
    print('pixels_list length = ', len(pixels_list))
    
    start_time = pygame.time.get_ticks()
    
    for pixel in pixels_list:
        
        color = get_random_color()
            
        start_position = pixel
                
        rect = pygame.Rect(start_position[0], start_position[1], PIXEL_UNIT_WIDTH, PIXEL_UNIT_HEIGHT)
            
        pygame.draw.rect(MAIN_WINDOW_SURFACE, color, rect)
          
    
    end_time = pygame.time.get_ticks()   
    
    delta_time = end_time - start_time

    print('Draw pixel use pygame.draw.Rect(), delta_time = ', delta_time)
    

# this method will draw multiple pixel units use the pygame.PixelArray object.
def draw_pixels_by_pixel_array():
    
    pixel_array_obj = None
    
    pixel_x = 0
    
    pixel_y = 0
    
    try:
        
        pixels_list = build_random_number_pair_list()
       
        start_time = pygame.time.get_ticks()
    
        # the pygame.PixelArray object has the same dimension and shape of the passed in surface object.
        # get the MAIN_WINDOW_SURFACE's shape with the method get_size(), then you can get the pixelArray object's maximum vertical and horizontal pixels number. 
        pixel_array_obj = pygame.PixelArray(MAIN_WINDOW_SURFACE)
    
        for pixel in pixels_list:
        
            color = get_random_color()
            
            pixel_x = pixel[0]
            
            pixel_y = pixel[1]
        
            # assign the color to the pixel unit.
            pixel_array_obj[pixel_x:pixel_x + PIXEL_UNIT_WIDTH, pixel_y:pixel_y + PIXEL_UNIT_HEIGHT] = color
             
    
        end_time = pygame.time.get_ticks()   
    
        delta_time = end_time - start_time

        print('Draw pixel use pygame.PixelArray, delta_time = ', delta_time)
    
    except IndexError as err:
        
        print('pixel_array_obj.ndim = ', pixel_array_obj.ndim)
    
        print('pixel_array_obj.shape = ', pixel_array_obj.shape)
    
        print('pixel_array_obj.itemsize = ', pixel_array_obj.itemsize)
        
        print(pixel_x, pixel_y)
        
        print('MAIN_WINDOW_SURFACE.get_size = ', MAIN_WINDOW_SURFACE.get_size())
        
        print('MAIN_WINDOW_SURFACE.get_width = ', MAIN_WINDOW_SURFACE.get_width())
        
        print('MAIN_WINDOW_SURFACE.get_height = ', MAIN_WINDOW_SURFACE.get_height())
        
        print("IndexError: {0}".format(err))
      
    finally:   
        
        # unlock the surface object to draw other images.
        del pixel_array_obj
        
            
    
# this method will return a list, the list contains X_MAX number of item.
# each list item is a list object, it saves the pixel unit's start point coordinate value. 
def build_random_number_pair_list():
    
    ret_list = []
    
    # when the window is resized, the window width and height will be changed also, so we should make the list size fixed.
    main_window_width = MAIN_WINDOW_SURFACE.get_width()
    
    print('main_window_width = ', main_window_width)
    
    global X_MAX
    
    if main_window_width < X_MAX:
        
        X_MAX = main_window_width
        
    main_window_height = MAIN_WINDOW_SURFACE.get_height()
    
    print('main_window_height = ', main_window_height)
    
    global Y_MAX
    
    if main_window_height < Y_MAX:
        
        Y_MAX = main_window_height 
        
           
    # get the x, y axis number list.
    x_number_list = list(range(X_MIN, main_window_width))
    y_number_list = list(range(Y_MIN, main_window_height))
    
    
    
    x_number_list_len = len(x_number_list)
    
    for i in range(x_number_list_len):
        
        # only pick the first X_MAX number of pixel coordinate.
        if i >= X_MAX:
            
            break
        
        x = random.choice(x_number_list)
        
        y = random.choice(y_number_list)
    
        pair_list = [x, y]
        
        ret_list.append(pair_list)
        
        
    print(len(ret_list))
     
    return ret_list



def main_loop():
    
    # implement the feature that when clicking the pygame window close button ("X") on window title bar then it will exit the window. 
    # Almost all pygame application will use this kinds of code.
    while True:
        
        # uncomment the below code to implement an pixel animation (trotting horse lamp).
        #draw_pixels(DRAW_PIXEL_UNIT_BY_PIXEL_ARRAY) 
        
        # Loop to get events and listen for event status.
        for event in pygame.event.get():
            
            # if user click the window close button.
            if event.type == pygame.QUIT: 
                               
                # quit pygame.
                pygame.quit()
                
                # quit the application.
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    
                    print('The Esc key is pressed.')
                    
                    # quit pygame.
                    pygame.quit()
                
                    # quit the application.
                    sys.exit()
                    
            elif event.type == pygame.VIDEORESIZE:
                
                # draw the pixel units again when user resize the pygame window. 
                draw_pixels(DRAW_PIXEL_UNIT_BY_PIXEL_ARRAY)  
                       
    
        pygame.display.update()
        
        # set the frame count that will be printed in one seconds. 
        FPS_CLOCK.tick(2)
        

# this function will be called when you want to draw pixel units on the pygame application's main window.
def draw_pixels(byPixelArray=True):
    
    # clear the window background by fill with the white color.
    MAIN_WINDOW_SURFACE.fill(pygame.Color('white'))
    
    if byPixelArray:
        
        draw_pixels_by_pixel_array()
        
    else:
        
        draw_pixels_by_draw_rect()         
    

if __name__ == '__main__':
    
    initialize_pygame()
    
    build_random_number_pair_list()
    
    draw_pixels(DRAW_PIXEL_UNIT_BY_PIXEL_ARRAY)
        
    main_loop()
