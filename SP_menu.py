import pygame
from pygame.locals import *
from image_loader import get_image
import Menu_Object


class sp_menu(object):


    def __init__(self, screen): #surface, color, x, y, length, height, width, text, text_color, font size
        self.screen = screen
        
        self.human_button = Menu_Object.Button(screen, (120, 120, 120), 20, 140, 429, 550, 0, "", (0, 0, 0), 35) #creates the buttons

        self.alien_button = Menu_Object.Button(screen, (120, 120, 120), 831, 140, 429, 550, 0, "", (0, 0, 0), 35)

        self.back_button = Menu_Object.Button(screen, (135, 12, 12), 565, 570, 150, 100, 0, "Back", (0, 0, 0), 35)
        
    #draws them
    
    def draw(self):
        self.screen.blit(get_image('assets\images\\backgrounds\Faction.png').convert(), (0, 0, 1280, 720))
        self.human_button.draw()
        self.alien_button.draw()
        self.screen.blit(get_image('assets\images\\buttons\\human_button.png').convert(), (20, 140, 550, 429))
        self.screen.blit(get_image('assets\images\\buttons\\alien_button.png').convert(), (831, 140, 550, 429))
        self.back_button.draw()
        
    def handle_event(self, event):    
        if event.type == MOUSEBUTTONDOWN and self.human_button.pressed() == True:
            print ("human")
    
        if event.type == MOUSEBUTTONDOWN and self.alien_button.pressed() == True:
            print ("alien")      
            
        if event.type == MOUSEBUTTONDOWN and self.back_button.pressed() == True:
            return "main_menu"
