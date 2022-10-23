import os
import pygame

class BaseObject():
    def __init__(self, x, y, width, height, screen, screen_pos) -> None:
        self.x = x - screen_pos[0]
        self.y = y - screen_pos[1]
        self.width = width
        self.height = height
        self.screen = screen
        
        self.screen_pos = screen_pos

        self.img = None

    def get_rect(self):
        return self.img.get_rect(topleft=(self.x-self.screen_pos[0], self.y-self.screen_pos[1]))