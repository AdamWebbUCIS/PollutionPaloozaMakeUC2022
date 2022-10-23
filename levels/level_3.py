from ast import Is
from asyncio import create_subprocess_exec
from codecs import latin_1_decode
from distutils.util import subst_vars
import enum
from gc import is_finalized
import os
from venv import create
import pygame
from player import Player
from level import Level
from objects.mutated_creature import MutatedCreature
from objects.radioactive_can import RadioactiveCan
from objects.island import Island
from objects.survivors import Survivor
import random

class Level3(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        print("INITALIZING LEVEL 3")
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos
        self.creature_list = []
        self.radioactive_material_list = []
        self.survivors = []
        self.latest_survivor_index = None
        self.latest_survivor_name = None
        self.font = pygame.font.Font(None, 25)

        for _ in range(5):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            creature = MutatedCreature(x, y, 50, 50, self.screen, self.screen_pos)
            self.creature_list.append(creature)
        
        for _ in range(7):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            can = RadioactiveCan(x, y, 100, 100, self.screen, self.screen_pos)
            
            self.radioactive_material_list.append(can)

        for _ in range(5):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            survivor = Survivor(x,y, 100, 100, self.screen, self.screen_pos)
            self.survivors.append(survivor)

        self.background = pygame.image.load(os.path.join("assets", "backgrounds", "Radioactive_Background.jpg")).convert_alpha()
        self.island = Island(600, 500, 500, 500, self.screen, self.screen_pos)
    
    def draw_level(self):
        super().draw_level()
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (-1500-self.screen_pos[0],-1600-self.screen_pos[1]))

        self.island.blit()
        
        for i, r_material in enumerate(self.radioactive_material_list):
            self.radioactive_material_list[i].x += self.radioactive_material_list[i].x_velocity
            self.radioactive_material_list[i].y += self.radioactive_material_list[i].y_velocity

            if r_material.x > 2400:
                self.radioactive_material_list[i].x_velocity = -(random.uniform(0,0.3))
            elif r_material.x < -1400:
                self.radioactive_material_list[i].x_velocity = (random.uniform(0,0.3))
            
            if r_material.y > 2300:
                self.radioactive_material_list[i].y_velocity = -(random.uniform(0,0.3))
            elif r_material.y < -1500:
                self.radioactive_material_list[i].y_velocity = (random.uniform(0,0.3))

            if self.player.rect.colliderect(r_material.get_rect()):
                if self.player.health > 0 and not self.passed:
                    self.player.health -= 0.32
            r_material.blit()

        for i, creature in enumerate(self.creature_list):
            self.creature_list[i].x += self.creature_list[i].x_velocity
            self.creature_list[i].y += self.creature_list[i].y_velocity

            if creature.x > 2400:
                self.creature_list[i].x_velocity = -(random.uniform(1,1.5))
            elif creature.x < -1400:
                self.creature_list[i].x_velocity = (random.uniform(1,1.5))
            
            if creature.y > 2300:
                self.creature_list[i].y_velocity = -1 *(random.uniform(1,1.5))
            elif creature.y < -1500:
                self.creature_list[i].y_velocity = (random.uniform(1,1.5))

            if self.player.rect.colliderect(creature.get_rect()):
                if not self.passed:
                    self.player.health = 0

            creature.blit()

        for i, survivor in enumerate(self.survivors):
            self.survivors[i].x += self.survivors[i].x_velocity
            self.survivors[i].y += self.survivors[i].y_velocity

            if survivor.x > 2400:
                self.survivors[i].x_velocity = -(random.uniform(0,0.3))
            elif survivor.x < -1400:
                self.survivors[i].x_velocity = (random.uniform(0,0.3))
            
            if survivor.y > 2300:
                self.survivors[i].y_velocity = -(random.uniform(0,0.3))
            elif survivor.y < -1500:
                self.turtle_list[i].y_velocity = (random.uniform(0,0.3))

            if self.player.rect.colliderect(survivor.get_rect()) and not self.player.has_survivor:
                self.player.has_survivor = True
                self.survivors[i].picked_up = True
                self.latest_survivor_name = survivor.name
                self.latest_survivor_index = i

            if not survivor.picked_up:
                survivor.blit()
        
        if self.player.rect.colliderect(self.island.get_rect()) and self.player.has_survivor:
            self.player.has_survivor = False
            self.survivors.pop(self.latest_survivor_index)
        if self.player.has_survivor:
            self.display_message(self.font, [f"You just picked up {self.survivors[self.latest_survivor_index].name}", "Take them to the island!",], 0,0)
        elif not self.player.has_survivor and isinstance(self.latest_survivor_index, int):
            self.display_message(self.font, [f"You just rescued {self.latest_survivor_name}", "Go grab another!",], 0,0)

        self.display_message(self.font, [f"Health: {self.player.health}"], 900, 0)
        self.group.add(self.player)
        self.group.draw(self.screen)

        if self.player.health <= 0 and not self.passed:
            self.display_message(self.font, ["GAME OVER YOU DIED!","(and probably turned into a mutant...)"], 450, 375)
            self.player.is_alive = False
        elif len(self.survivors) <= 0:
            self.display_message(self.font, ["YOU BEAT ALL THE DISASTERS!","(congrats, no more people were harmed :)"], 420, 375)
            self.passed = True