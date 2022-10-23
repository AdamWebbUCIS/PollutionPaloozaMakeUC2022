import os
from tkinter import Y
from turtle import back
import pygame
from player import Player
from level import Level
from objects.turtle import Turtle
from objects.trash import Trash
import random

class Level1(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos

        self.turtle_list = []

        for _ in range(10):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            turtle = Turtle(x, y, 100, 100, self.screen, self.screen_pos)
            self.turtle_list.append(turtle)
        
        self.trash_list = []
        
        for _ in range(20):
            x = random.randint(-1400,2400)
            y = random.randint(-1500,2300)
            piece_of_trash = Trash(x, y, 100, 100, self.screen, self.screen_pos)
            self.trash_list.append(piece_of_trash)
        
        self.background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()

    def draw_level(self):
        super().draw_level()
        self.screen.fill((0,0,0))
        self.screen.blit(self.background, (-1500-self.screen_pos[0],-1600-self.screen_pos[1]))

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

        for i, turtle in enumerate(self.turtle_list):

            for trash in self.trash_list:
                if trash.get_rect().colliderect(turtle.get_rect()):
                    turtle.toggle_tangled(True)
            if self.player.rect.colliderect(turtle.get_rect()):
                turtle.toggle_tangled(False)

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
        
        self.group.add(self.player)
        self.group.draw(self.screen)