import os
import pygame
from objects.object import BaseObject
from random import randint, choice
import random

class Island(BaseObject):
        def __init__(self, x, y, width, height, screen, screen_pos) -> None:
            super().__init__(x, y, width, height, screen, screen_pos)
            self.screen_pos = screen_pos

            self.island = pygame.image.load(os.path.join("assets", "sprites", "Island.png"))
            self.img = pygame.transform.scale(self.island, (self.width, self.height))
            self.rect = self.img.get_rect(topleft=(self.x-self.screen_pos[0], self.y-self.screen_pos[1]))
            
            self.survivors = []
        def add_survivor(self, survivor):
            self.survivors.append(survivor)

        def blit(self):
            self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))