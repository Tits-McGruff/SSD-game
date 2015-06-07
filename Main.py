import pygame
from pygame.locals import *
import Menu_Object
import main_menu
import SP_menu
import TP_menu
import settings_menu
import highscores_menu
from image_loader import get_image
import os

clock = pygame.time.Clock()
done = False 
pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
current_menu = main_menu.menu(screen)
    
while not done:
    
    for event in pygame.event.get():
        if current_menu.handle_event(event) == "main_menu":
            current_menu = main_menu.menu(screen)
        
        elif current_menu.handle_event(event) == "SP_menu":
            current_menu = SP_menu.sp_menu(screen)
            
        elif current_menu.handle_event(event) == "TP_menu":
            current_menu = TP_menu.tp_menu(screen)
            
        elif current_menu.handle_event(event) == "settings":
            current_menu = settings_menu.settings_menu(screen)
            
        elif current_menu.handle_event(event) == "highscores":
            current_menu = highscores_menu.highscores_menu(screen)
            
        if event.type == pygame.QUIT:
            done = True            
            
    pressed = pygame.key.get_pressed()
    
    current_menu.draw()
    
    pygame.display.flip()
    
    if pressed[pygame.K_ESCAPE]: quit()
    clock.tick(60)
    
