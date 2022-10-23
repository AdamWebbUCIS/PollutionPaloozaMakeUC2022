import os
from tkinter import Y
from turtle import back
import pygame
from player import Player
from level import Level
from objects.shark import Shark
import random

class TestLevel(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos

        self.shark1 = Shark(100, 100, 100, 100, self.screen, self.screen_pos)
    def draw_level(self):
        super().draw_level()
        background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()
        
        self.screen.blit(background, (0-self.screen_pos[0],0-self.screen_pos[1]))
        self.shark1.blit()

        if self.player.rect.colliderect(self.shark1.get_rect()):
            print("COLLIDED WITH SHARK1")

        self.group.add(self.player)
        self.group.draw(self.screen)
