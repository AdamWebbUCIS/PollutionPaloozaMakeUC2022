import pygame

class Player(pygame.sprite.Sprite): 
    def __init__(self, is_alive=True):
        self.is_alive = is_alive
        self.x_pos = 0
        self.y_pos = 0
        
        self.player_emotions = {
            "happy": pygame.image.load('assets\Earth_Lover_ 1.png').convert_alpha()  , 
            "scared_player": pygame.image.load('assets\Earth_Lover_.png').convert_alpha()
        }
        
        self.image = self.player_emotions.happy
        self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # left 
            self.x_pos -= 1
        elif keys[pygame.K_s]: # down 
            self.y_pos -= 1
        elif keys[pygame.K_d]: # right
            self.x_pos += 1
        elif keys[pygame.K_w]: # up
            self.y_pos += 1
        #TODO add more input

    def check_player_state(self):
        if self.is_alive:
            self.player_emotions.happy
        else:
            self.player_emotions.scared
    
    def update(self):
        self.player_input()
        self.check_player_state()
