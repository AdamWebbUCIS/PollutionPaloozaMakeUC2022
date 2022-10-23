from gc import is_finalized
import os
import pygame
from player import Player
from level import Level
from objects.shark import Shark
from objects.turtle import Turtle
from objects.oil import OilSpill
import random

class Level2(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos
        self.shark_list = []
        self.oil_spill_list = []
        self.font = pygame.font.Font(None, 25)
        self.frame_count = 0
        self.last_hit = 0
        
        for _ in range(15):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            shark = Shark(x, y, 50, 50, self.screen, self.screen_pos)
            self.shark_list.append(shark)
        
        for _ in range(5):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            oil_spill = OilSpill(x, y, 100, 100, self.screen, self.screen_pos)
            self.oil_spill_list.append(oil_spill)

        self.background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()

    def draw_level(self):
        super().draw_level()
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (-1500-self.screen_pos[0],-1600-self.screen_pos[1]))

        for i, oil_spill in enumerate(self.oil_spill_list):
            self.oil_spill_list[i].x += self.oil_spill_list[i].x_velocity
            self.oil_spill_list[i].y += self.oil_spill_list[i].y_velocity

            if oil_spill.x > 2400:
                self.oil_spill_list[i].x_velocity = -(random.uniform(0,0.3))
            elif oil_spill.x < -1400:
                self.oil_spill_list[i].x_velocity = (random.uniform(0,0.3))
            
            if oil_spill.y > 2300:
                self.oil_spill_list[i].y_velocity = -(random.uniform(0,0.3))
            elif oil_spill.y < -1500:
                self.oil_spill_list[i].y_velocity = (random.uniform(0,0.3))
            
            if oil_spill.cleaned_up_time <= 500:
                if self.player.rect.colliderect(oil_spill.get_rect()) and self.player.tool_status:
                    self.oil_spill_list[i].cleaned_up_time += 1
                else:
                    self.oil_spill_list[i].cleaned_up_time = 0
            else:
                if self.player.is_alive:
                    self.oil_spill_list.pop(i)

            oil_spill.blit()

        for i, shark in enumerate(self.shark_list):
            self.shark_list[i].x += self.shark_list[i].x_velocity
            self.shark_list[i].y += self.shark_list[i].y_velocity

            if shark.x > 2400:
                self.shark_list[i].x_velocity = -(random.uniform(1,1.5))
            elif shark.x < -1400:
                self.shark_list[i].x_velocity = (random.uniform(1,1.5))
            
            if shark.y > 2300:
                self.shark_list[i].y_velocity = -1 *(random.uniform(1,1.5))
            elif shark.y < -1500:
                self.shark_list[i].y_velocity = (random.uniform(1,1.5))

            if self.player.rect.colliderect(shark.get_rect()):
                if self.player.health > 0 and not self.passed:
                    self.player.health -= 0.32
            shark.blit()

        self.display_message(self.font, [f"Health: {int(self.player.health)}"], 0, 0)
        self.display_message(self.font, [f"Oil Spills: {len(self.oil_spill_list)}"], 850, 0)

        self.group.add(self.player)
        self.group.draw(self.screen)
        self.frame_count += 1

        if self.player.health <= 0 and not self.passed:
            self.display_message(self.font, ["GAME OVER YOU DIDN'T","FIX THE OIL SPILL!"], 450, 375)
            self.player.is_alive = False
        elif len(self.oil_spill_list) <= 0:
            self.display_message(self.font, ["YOU WON!!!"], 480, 375)
            self.passed = True