import pygame
from pygame.locals import *
from image_loader import get_image
import Menu_Object


class sp_menu(object):


    def __init__(self, screen): #surface, color, x, y, length, height, width, text, text_color, font size
        self.screen = screen
        self.human_button = Menu_Object.Button(screen, (135, 12, 12), 20, 120, 550, 429, 0, "", (0, 0, 0), 35) #creates the buttons

        self.alien_button = Menu_Object.Button(screen, (135, 12, 12), 831, 120, 550, 429, 0, "", (0, 0, 0), 35)

        self.back_button = Menu_Object.Button(screen, (135, 12, 12), 1000, 600, 100, 50, 0, "Back", (0, 0, 0), 20)
        
        self.screen.blit(get_image('Faction.png').convert(), (0, 0, 1280, 720))
    #draws them
    
    def draw(self):
        self.human_button.draw()
        self.alien_button.draw()
        self.back_button.draw()
        self.screen.blit(get_image('human button.png').convert(), (20, 120, 550, 429))
        self.screen.blit(get_image('alien button.png').convert(), (831, 120, 550, 429))
        
    def handle_event(self, event):    
        if event.type == MOUSEBUTTONDOWN and self.human_button.pressed() == True:
            print ("test")
    
        if event.type == MOUSEBUTTONDOWN and self.alien_button.pressed() == True:
            print ("test")      
            
        if event.type == MOUSEBUTTONDOWN and self.back_button.pressed() == True:
            return self.main_menu.menu(screen)
