import os
import pygame
from objects.object import BaseObject
from random import randint, choice
import random

class MutatedCreature(BaseObject):
        def __init__(self, x, y, width, height, screen, screen_pos) -> None:
            super().__init__(x, y, width, height, screen, screen_pos)
            self.screen_pos = screen_pos

            self.x_velocity = random.uniform(0, 0.3)
            self.y_velocity = random.uniform(0, 0.3)
            
            self.flip = False

            self.creatures = {
                "wart_fish": pygame.image.load(os.path.join("assets", "sprites", "Wart_Fish.png")).convert_alpha(),
                "two_head_shark": pygame.image.load(os.path.join("assets", "sprites", "Two_Headed_Shark.png")).convert_alpha(),
                "boss":  pygame.image.load(os.path.join("assets", "sprites", "Boss_Fish.png")).convert_alpha(),
            }
            self.creature = choice(list(self.creatures.values()))
            self.img = pygame.transform.scale(self.creature, (self.width, self.height))
            self.rect = self.img.get_rect(topleft=(self.x-self.screen_pos[0], self.y-self.screen_pos[1]))

        def blit(self):
            if self.x_velocity < 0:
                self.flip = True
            elif self.x_velocity > 0:
                self.flip = False

            self.img = pygame.transform.scale(self.creature, (self.width, self.height))
            self.img = pygame.transform.flip(self.img, self.flip, False)
            self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))