import pygame 
from player import Player

class Level:
    def __init__(self, player:Player, screen:pygame.Surface, passed=False) -> None:
        self.player = player
        self.screen = screen  
        self.passed = passed
    

    def draw(self):
        self.screen.fill()
        

