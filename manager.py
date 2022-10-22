
import pygame 
from player import Player
from level import Level

from levels.test_level import TestLevel

class Manager:
    def __init__(self, player:Player, screen):
        self.player = player
        self.screen = screen
        self.screen_pos = [0,0]
        self.active_level = TestLevel(self.player, self.screen, self.screen_pos)
    
    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.screen_pos[0] -= 2
        if keys[pygame.K_d]:
            self.screen_pos[0] += 2
        if keys[pygame.K_w]:
            self.screen_pos[1] -=2
        if keys[pygame.K_s]:
            self.screen_pos[1] += 2
    
    def run_level(self):
        self.get_user_input()
        self.active_level.draw_level()


