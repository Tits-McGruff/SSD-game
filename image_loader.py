import pygame
from pygame.locals import *
import os

_image_library = {}
def get_image(path): #this makes loading pictures work, make sure that the picture you're loading is in the same directory as the file
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
