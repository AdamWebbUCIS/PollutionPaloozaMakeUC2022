
import pygame 
from player import Player
from level import Level

from levels.level_1 import Level1

class Manager:
    def __init__(self, player:Player, screen):
        self.player = player
        self.screen = screen
        self.screen_pos = [0,0]
        self.levels = [
            Level1(self.player, self.screen, self.screen_pos),
        ]
        self.active_level = self.levels[0]
    
    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.screen_pos[0] -= 5
        if keys[pygame.K_d]:
            self.screen_pos[0] += 5
        if keys[pygame.K_w]:
            self.screen_pos[1] -= 5
        if keys[pygame.K_s]:
            self.screen_pos[1] += 5

    def switch_level(self):
        #change active level
        self.player.active_level = self.active_level

    def run_level(self):
        self.player.update()
        self.get_user_input()
        self.active_level.draw_level()