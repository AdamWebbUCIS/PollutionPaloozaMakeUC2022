import os
import pygame
from objects.object import BaseObject
from random import randint, choice
import random

class Trash(BaseObject):
        def __init__(self, x, y, width, height, screen, screen_pos) -> None:
            super().__init__(x, y, width, height, screen, screen_pos)
            self.screen_pos = screen_pos

            self.x_velocity = random.uniform(0, 0.3)
            self.y_velocity = random.uniform(0, 0.3)

            self.trash = {
                "bottle": pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "Bottle 1.png")).convert_alpha(),(self.width, self.height)),
                "bottle_two": pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "Bottle.png")).convert_alpha(),(self.width, self.height)),
                "recycle":  pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "Recycle_bin.png")).convert_alpha(),(self.width, self.height)),
                "tire": pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "Tire.png")).convert_alpha(),(self.width, self.height))
            }

            self.img = pygame.transform.rotozoom(choice(list(self.trash.values())), 0, 0.5)
            self.rect = self.img.get_rect(topleft = (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))

        def blit(self):
            self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))