import os
import pygame
from objects.object import BaseObject
from random import randint, choice
import random

class RadioactiveCan(BaseObject):
        def __init__(self, x, y, width, height, screen, screen_pos) -> None:
            super().__init__(x, y, width, height, screen, screen_pos)
            self.screen_pos = screen_pos

            self.x_velocity = random.uniform(0, 0.3)
            self.y_velocity = random.uniform(0, 0.3)

            self.can = pygame.image.load(os.path.join("assets", "sprites", "Can.png")).convert_alpha()

            self.img = pygame.transform.rotozoom(self.can, 0, 0.1)
            self.rect = self.img.get_rect(topleft = (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))

        def blit(self):
            self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))