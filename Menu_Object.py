import pygame
from pygame.locals import *
pygame.init()


class Button():
    def __init__(self, surface, color, x, y, length, height, width, text, text_color, font_size):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.rect = pygame.Rect(x,y, length, height)
        
    def draw(self):
        self.draw_button(self.surface, self.color, self.length, self.height, self.x, self.y, self.width)
        self.write_text(self.surface, self.text, self.text_color, self.length, self.height, self.x, self.y, self.font_size)

        
    
    def write_text(self, surface, text, text_color, length, height, x, y, font_size):
        myFont = pygame.font.SysFont("Helvetica", self.font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface
        
    def pressed(self): #checks if the button was pressed
        mouse = pygame.mouse.get_pos()
        if (mouse[0] > self.rect.topleft[0] and
               mouse[1] > self.rect.topleft[1] and
               mouse[0] < self.rect.bottomright[0] and
               mouse[1] < self.rect.bottomright[1]):
            return True
        else:
            return False
   
