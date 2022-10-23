
import pygame 
from player import Player
from level import Level
from levels.level_1 import Level1
from levels.level_2 import Level2
from levels.level_3 import Level3

class Manager:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.screen_pos = [0,0]
        self.levels = [
            Level1,
            Level2,
            Level3,
        ]

        self.curr_level = None

        self.level_initalized = False
        self.level_index = 0
    
    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.screen_pos[0] > -1485:
            self.screen_pos[0] -= 5
            self.player.flip = True
        if keys[pygame.K_d] and self.screen_pos[0] < 1485:
            self.screen_pos[0] += 5
            self.player.flip = False
        if keys[pygame.K_w] and self.screen_pos[1] > -1585:
            self.screen_pos[1] -= 5
        if keys[pygame.K_s] and self.screen_pos[1] < 1585:
            self.screen_pos[1] += 5

    def switch_level(self):
        #change active level
        self.player.active_level = self.active_level

    def run_level(self):

        if not self.level_initalized:
            self.player = Player(True, self.level_index)
            self.curr_level = self.levels[self.level_index](self.player, self.screen, self.screen_pos, False)
            self.level_initalized = True
        if not self.curr_level.passed:
            self.player.update()
            if self.player.is_alive:
                self.get_user_input()  
            else:
                pygame.time.wait(5000)
                self.level_initalized = False
            self.curr_level.draw_level()
        else:
            self.level_index += 1
            self.level_initalized = False
            