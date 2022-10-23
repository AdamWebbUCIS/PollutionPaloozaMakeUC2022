import os
import pygame
from objects.object import BaseObject

class Turtle(BaseObject):
    def __init__(self, x, y, width, height, screen, screen_pos) -> None:
        super().__init__(x, y, width, height, screen, screen_pos)
        self.screen_pos = screen_pos

        self.is_tangled = False
        self.turtle = pygame.image.load(os.path.join("assets", "sprites", "Happy_Turtle.png")).convert_alpha()
        self.tangled_turtle = pygame.image.load(os.path.join("assets", "sprites", "Sad_Turtle.png")).convert_alpha()
        self.img = pygame.transform.scale(self.turtle, (self.width, self.height))

        self.swim_speed = 3
    
    def blit(self):
        if self.is_tangled:
            self.img = pygame.transform.scale(self.tangled_turtle, (self.width, self.height))
        else:
            self.img = pygame.transform.scale(self.turtle, (self.width, self.height))

        self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))

    def swim(self):
        self.x += (1 - self.screen_pos)

    def toggle_tangled(self, is_tangled):
        self.is_tangled = is_tangled