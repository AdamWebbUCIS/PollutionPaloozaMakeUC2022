import os
from tkinter import Y
from turtle import back
import pygame
from player import Player
from level import Level

class Victory(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=True, win=False) -> None:
        super().__init__(player, screen, passed)
        self.screen_pos = screen_pos
        self.win = win

    def draw_level(self):
        super().draw_level()
        background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()
        font = pygame.font.SysFont(None, 24)

        self.screen.blit(background, (0,0))
        txt = font.render('Victory', False, 'Black')
        self.screen.blit(txt, (500, 400))