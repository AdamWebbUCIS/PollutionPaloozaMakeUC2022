
import pygame
import os 

class Player(pygame.sprite.Sprite): 
    def __init__(self, is_alive=True):
        super().__init__()
        self.is_alive = is_alive
        self.x_pos = 475
        self.y_pos = 375
        
        self.player_emotions = {
            "happy": pygame.image.load(os.path.join('assets','sprites','player','Earth_Lover_ 1.png')).convert_alpha(), 
            "scared_player": pygame.image.load(os.path.join('assets','sprites','player','Earth_Lover_.png')).convert_alpha()
        }
        
        self.image = pygame.transform.scale(self.player_emotions["happy"], (50,50))
    
        self.rect = self.image.get_rect(topleft = (self.x_pos,self.y_pos))

    def check_player_state(self):
        if self.is_alive:
            self.player_emotions["happy"]
        else:
            self.player_emotions["scared"]
    
    def update(self):
        self.check_player_state()

