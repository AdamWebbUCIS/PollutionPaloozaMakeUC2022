import os
import pygame
from objects.object import BaseObject
from random import randint
import random

class Shark(BaseObject):
    def __init__(self, x, y, width, height, screen, screen_pos) -> None:
        super().__init__(x, y, width, height, screen, screen_pos)
        self.screen_pos = screen_pos

        self.shark = pygame.image.load(os.path.join("assets", "sprites", "Shark.png")).convert_alpha()
        self.img = pygame.transform.scale(self.shark, (self.width, self.height))
        self.rect = self.img.get_rect(topleft=(self.x-self.screen_pos[0], self.y-self.screen_pos[1]))
        self.swim_speed = 3

        self.x_velocity, self.y_velocity = 0,0

        self.x_velocity = random.uniform(1,1.5)
        self.y_velocity = random.uniform(1,1.5)

        self.flip = False

    def blit(self):
        if self.x_velocity > 0:
            self.flip = False
        elif self.x_velocity < 0:
            self.flip = True
        self.img = pygame.transform.scale(self.shark, (self.width, self.height))
        self.img = pygame.transform.flip(self.img, self.flip, False)
        self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))