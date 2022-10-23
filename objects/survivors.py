from distutils.ccompiler import gen_lib_options
import os
from re import L
import pygame
from objects.object import BaseObject
from random import randint, choice
import random

class Survivor(BaseObject):
    num_male, num_female = 0,0
    names = {
        "male_names": ["Paul", "Luke", "Adam", "Harold", "Gerald", "Kenneth", "Steven", "Doug"],
        "female_names": ["Susan", "Carol", "Morgan", "Grace", "Nancy", "Lisa", "Karen", "Ethel"]
    }
    def __init__(self, x, y, width, height, screen, screen_pos) -> None:
        super().__init__(x, y, width, height, screen, screen_pos)
        self.screen_pos = screen_pos

        self.x_velocity = random.uniform(0, 0.3)
        self.y_velocity = random.uniform(0, 0.3)
        
        self.gender = {
            "man": pygame.image.load(os.path.join("assets", "sprites", "Man.png")).convert_alpha(),
            "woman": pygame.image.load(os.path.join("assets", "sprites", "Woman.png")).convert_alpha()
        }

        decided_gender = choice(list(self.gender.values()))

        if decided_gender == self.gender["man"]:
            Survivor.num_male += 1
            self.name = choice(Survivor.names["male_names"])
        else:
            Survivor.num_female += 1
            self.name = choice(Survivor.names["female_names"])

        self.img = pygame.transform.rotozoom(decided_gender, 0, 0.1)
        self.rect = self.img.get_rect(topleft = (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))
        self.is_rescued = False
        self.picked_up = False
        print(
            f"A new survivor was created named: {self.name}"
        )

    def rescue(self):
        self.is_rescued = True

    def blit(self):
        self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))