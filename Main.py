import pygame
from pygame.locals import *
import Menu
import Menu_Object
import main_menu
from image_loader import get_image

clock = pygame.time.Clock()
done = False 
pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
current_menu = main_menu.menu(screen)
        
screen.blit(get_image('Main_Menu.png').convert(), (0, 0, 1280, 720))
    
while not done:
    
    for event in pygame.event.get():
        temp = current_menu.handle_event(event)
        if temp is not None:
            current_menu = temp
        if event.type == pygame.QUIT:
            done = True            
            
    pressed = pygame.key.get_pressed()
    
    current_menu.draw()
    
    pygame.display.flip()
    
    if pressed[pygame.K_ESCAPE]: quit()
    clock.tick(60)
    
