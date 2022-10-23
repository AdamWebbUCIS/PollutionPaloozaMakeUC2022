import os
import pygame
from player import Player
from level import Level
from objects.turtle import Turtle
from objects.trash import Trash
from level import Text
import random

class Level1(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        print("init for level1")
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos
        self.turtle_list = []
        self.trash_list = []
        self.tangled_turtles = 0
        self.font = pygame.font.Font(None, 25)
        self.tick = 0
        self.enable_level = False
        
        self.instructions = Text(self.font, ["Use 'e' to extend your net and press 'c' to pick up all the trash!", "If you pass any tangled turtles be sure to free them...", "Pick up all the trash and free all turtles to progress!"], 250, 300)
        self.description = Text(self.font, [
                "The great Pacific Garbage Patch is a cluster of marine debris particles in the central North Pacific", 
                "Ocean, consisting of 45-129 thousand metric tons of plastic. Some of the plastic is over 50 years",
                "old and the patch is rapidly accumulating to this day…This growing patch contributes to other environmental", 
                "damage to marine ecosystems and species."
            ],80, 400)

        
        for _ in range(10):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            turtle = Turtle(x, y, 100, 100, self.screen, self.screen_pos)
            self.turtle_list.append(turtle)
        
        
        for _ in range(20):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            piece_of_trash = Trash(x, y, 100, 100, self.screen, self.screen_pos)
            self.trash_list.append(piece_of_trash)
        
        self.background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()

    def draw_level(self):
        super().draw_level()
        tangled_turtles = 0
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (-1500-self.screen_pos[0],-1600-self.screen_pos[1]))

        if self.enable_level:
            for i, trash in enumerate(self.trash_list):
                self.trash_list[i].x += self.trash_list[i].x_velocity
                self.trash_list[i].y += self.trash_list[i].y_velocity

                if trash.x > 2400:
                    self.trash_list[i].x_velocity = -(random.uniform(0,0.3))
                elif trash.x < -1400:
                    self.trash_list[i].x_velocity = (random.uniform(0,0.3))
                
                if trash.y > 2300:
                    self.trash_list[i].y_velocity = -(random.uniform(0,0.3))
                elif trash.y < -1500:
                    self.turtle_list[i].y_velocity = (random.uniform(0,0.3))

                trash.blit()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_c] and (self.player.player_index == 4):
                    if self.player.rect.colliderect(trash.get_rect()):
                        self.trash_list.pop(i)

            for i, turtle in enumerate(self.turtle_list):
                for trash in self.trash_list:
                    if trash.get_rect().colliderect(turtle.get_rect()):
                        turtle.toggle_tangled(True)
                if self.player.rect.colliderect(turtle.get_rect()):
                    turtle.toggle_tangled(False)
                if turtle.is_tangled:
                    tangled_turtles += 1
                self.turtle_list[i].x += self.turtle_list[i].x_velocity
                self.turtle_list[i].y += self.turtle_list[i].y_velocity

                if turtle.x > 2400:
                    self.turtle_list[i].x_velocity = -(random.uniform(1,1.5))
                elif turtle.x < -1400:
                    self.turtle_list[i].x_velocity = (random.uniform(1,1.5))
                
                if turtle.y > 2300:
                    self.turtle_list[i].y_velocity = -1 *(random.uniform(1,1.5))
                elif turtle.y < -1500:
                    self.turtle_list[i].y_velocity = (random.uniform(1,1.5))
                turtle.blit()

            self.tangled_turtles = len([t for t in self.turtle_list if t.is_tangled])
            self.display_message(self.font, [f"Tangled Turtles: {self.tangled_turtles}"],0,0)
            self.display_message(self.font, [f"Trash Left: {len(self.trash_list)}"],850,0)


            self.group.add(self.player)
            self.group.draw(self.screen)

            if self.tangled_turtles <= 0 and len(self.trash_list) <= 0:
                self.passed = True
                self.display_message(self.font, ["YOU WIN!!!"], 480, 375)
                self.player.is_alive = False

        if self.tick <= 1500:
            self.instructions.draw(self.screen)
            self.description.draw(self.screen)
        else:
            self.enable_level = True
        self.tick += 1