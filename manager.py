
import pygame 
from player import Player
from level import Level

from levels.level_1 import Level1
from levels.game_over import GameOver
from levels.victory import Victory

class Manager:
    def __init__(self, player:Player, screen):
        self.player = player
        self.screen = screen
        self.screen_pos = [0,0]
        self.levels = [
            Level1(self.player, self.screen, self.screen_pos),
            GameOver(self.player, self.screen, self.screen_pos),
            Victory(self.player, self.screen, self.screen_pos)
        ]
        self.level_index = 0
        self.active_level = self.levels[self.level_index]
    
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
        if self.active_level.passed == False:
            if self.active_level.win == False:
                self.level_index += 1
                self.active_level = self.levels[self.level_index]
            else:
                self.level_index += 2
                self.active_level = self.levels[self.level_index]
        self.player.update()
        self.get_user_input()
        self.active_level.draw_level()