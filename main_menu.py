import pygame
from pygame.locals import *
import Menu_Object
from image_loader import get_image


class menu(object):
    def __init__(self, screen): #surface, color, x, y, length, height, width, text, text_color, font size
        self.screen = screen    
    
        self.SP_button = Menu_Object.Button(screen, (135, 12, 12), 1000, 160, 200, 100, 0, "Single Player", (0, 0, 0), 35) #creates the buttons

        self.TP_button = Menu_Object.Button(screen, (135, 12, 12), 1000, 270, 200, 100, 0, "Two Player", (0, 0, 0), 35)

        self.settings_button = Menu_Object.Button(screen, (135, 12, 12), 1000, 380, 200, 100, 0, "Settings", (0, 0, 0), 35)

        self.highscores_button = Menu_Object.Button(screen, (135, 12, 12), 1000, 490, 200, 100, 0, "High score", (0, 0, 0), 35)

        self.exit_button = Menu_Object.Button(screen, (135, 12, 12), 1000, 600, 200, 100, 0, "Quit", (0, 0, 0), 35)
        
    #draws them
    def draw(self):
        self.screen.blit(get_image('assets\images\\backgrounds\Main_Menu.png').convert(), (0, 0, 1280, 720))
        self.SP_button.draw()
        self.TP_button.draw()
        self.settings_button.draw()
        self.highscores_button.draw()
        self.exit_button.draw()
        
        
    def handle_event(self, event):    
        if event.type == MOUSEBUTTONDOWN and self.SP_button.pressed() == True:
            return "SP_menu"
            
        if event.type == MOUSEBUTTONDOWN and self.TP_button.pressed() == True:
            return "TP_menu"

        if event.type == MOUSEBUTTONDOWN and self.settings_button.pressed() == True:
            return "settings"
            
        if event.type == MOUSEBUTTONDOWN and self.highscores_button.pressed() == True:
            return "highscores"
          
        if event.type == MOUSEBUTTONDOWN and self.exit_button.pressed() == True:
            quit()
        return None 
