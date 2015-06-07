import pygame
from pygame.locals import *
from image_loader import get_image
import Menu_Object
import os.path


class highscores_menu(object):


    def __init__(self, screen): #surface, color, x, y, length, height, width, text, text_color, font size
        self.screen = screen
        if not os.path.exists("saved_files/Highscores/"):
            os.makedirs("saved_files/Highscores/")
        if os.path.isfile("saved_files/Highscores/scores.txt") == False:
            scores = open("saved_files/Highscores/scores.txt", "w")
            scores.write("no scores \n")
            scores.close()
        
        if os.path.isfile("saved_files/Highscores/scores.txt") == True:
            scores = open('saved_files/Highscores/scores.txt', 'r')
        
        self.back_button = Menu_Object.Button(screen, (135, 12, 12), 30, 580, 150, 100, 0, "Back", (0, 0, 0), 35)
        
    #draws them
    
    def draw(self):
        self.screen.blit(get_image('assets\images\\backgrounds\highscore.png').convert(), (0, 0, 1280, 720))
        self.back_button.draw()
        
    def handle_event(self, event):     
            
        if event.type == MOUSEBUTTONDOWN and self.back_button.pressed() == True:
            return "main_menu"
