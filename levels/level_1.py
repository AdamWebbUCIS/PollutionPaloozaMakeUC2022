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

        for _ in range(5):
            x = random.randint(0,1000)
            y = random.randint(0, 800)
            turtle = Turtle(x, y, 100, 100, self.screen, self.screen_pos)
            self.turtle_list.append(turtle)
        
        self.trash_list = []
        
        for _ in range(10):
            x = random.randint(0,1000)
            y = random.randint(0, 800)
            piece_of_trash = Trash(x, y, 100, 100, self.screen, self.screen_pos)
            self.trash_list.append(piece_of_trash)
        
        self.background = pygame.image.load(os.path.join("assets", "backgrounds", "background.jpg")).convert_alpha()

    def draw_level(self):
        super().draw_level()
        self.screen.blit(self.background, (0-self.screen_pos[0],0-self.screen_pos[1]))

        for turtle in self.turtle_list:
            turtle.blit()

            if self.player.rect.colliderect(turtle.get_rect()):
                    turtle.toggle_tangled(False)

            for trash in self.trash_list:
                if trash.rect.colliderect(turtle.get_rect()):
                    turtle.toggle_tangled(True)
        
        for trash in self.trash_list:
            trash.blit()

        self.group.add(self.player)
        self.group.draw(self.screen)