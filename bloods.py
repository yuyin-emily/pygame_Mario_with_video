import pygame

class bloods():
    def __init__(self):
        self.position = [50,50]
        self.img = pygame.image.load("./image/blood.png")
        self.show = True