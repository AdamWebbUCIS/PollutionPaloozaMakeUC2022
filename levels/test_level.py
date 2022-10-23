import os
from tkinter import Y
from turtle import back
import pygame
from player import Player
from level import Level
from objects.shark import Shark
from objects.trash import Trash
import random

class TestLevel(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos

        self.shark1 = Shark(100, 100, 100, 100, self.screen, self.screen_pos)
        
        self.trash_list = []
        
        for _ in range(10):
            x = random.randint(0,1000)
            y = random.randint(0, 800)
            piece_of_trash = Trash(
                x,
                y,
                100,
                100,
                self.screen,
                self.screen_pos
            )

            self.trash_list.append(piece_of_trash)
        
        self.background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()

    def draw_level(self):
        super().draw_level()
        
        self.screen.blit(self.background, (0-self.screen_pos[0],0-self.screen_pos[1]))
        self.shark1.blit()
        
        for trash in self.trash_list:
            trash.blit()
        if self.player.rect.colliderect(self.shark1.get_rect()):
            print("COLLIDED WITH SHARK1")

        self.group.add(self.player)
        self.group.draw(self.screen)