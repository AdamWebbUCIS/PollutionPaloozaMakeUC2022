import os
from turtle import back
import pygame 
from player import Player

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

