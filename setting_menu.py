import pygame
from pygame.locals import *
from image_loader import get_image
import Menu_Object


class settings_menu(object):


    def __init__(self, screen): #surface, color, x, y, length, height, width, text, text_color, font size
        self.screen = screen

        self.back_button = Menu_Object.Button(screen, (135, 12, 12), 565, 570, 150, 100, 0, "Back", (0, 0, 0), 35)
        
    #draws them
    
    def draw(self):
        self.screen.blit(get_image('assets/images/backgrounds/settings.png').convert(), (0, 0, 1280, 720))
        self.back_button.draw()
        
    def handle_event(self, event):    
    
        if event.type == MOUSEBUTTONDOWN and self.back_button.pressed() == True:
            return "main_menu"
