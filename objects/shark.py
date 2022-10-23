import os
import pygame
from objects.object import BaseObject

class Shark(BaseObject):
    def __init__(self, x, y, width, height, screen, screen_pos) -> None:
        super().__init__(x, y, width, height, screen, screen_pos)
        self.screen_pos = screen_pos
        self.img = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "sprites", "Scary_Sea_Monster_.png")).convert_alpha(),
            (self.width, self.height)
        )

        self.swim_speed = 3
    
    def blit(self):
        self.screen.blit(self.img, (self.x-self.screen_pos[0], self.y-self.screen_pos[1]))

    def swim(self):
        self.x += (1 - self.screen_pos)