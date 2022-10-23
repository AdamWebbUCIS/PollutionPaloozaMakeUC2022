import os
from turtle import back
import pygame 
from player import Player

class Text:
    def __init__(self, font, text, x, y) -> None:
        self.x = x
        self.y = y

        curr_y = y

        self.text_surfaces = []
        for line in text:
            text_surface = font.render(line, True, (255,255,255), (100, 100, 100))
            self.text_surfaces.append(text_surface)
        
    def draw(self, screen:pygame.Surface):
        curr_y = self.y

        for surface in self.text_surfaces:
            screen.blit(surface, (self.x, curr_y))
            curr_y += 15

class Level:
    def __init__(self, player:Player, screen:pygame.Surface, passed=False) -> None:
        self.player = player
        self.screen = screen  
        self.passed = passed
        
    def display_message(self, font, text, x, y):
        curr_y = y
        for line in text:
            text_surface = font.render(line, True, (255,255,255), (100, 100, 100))
            self.screen.blit(text_surface, (x, curr_y))
            curr_y += 15

    def draw_level(self):
        pass

