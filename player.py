import pygame
import os 

class Player(pygame.sprite.Sprite): 
    def __init__(self, is_alive=True, active_level=None):
        super().__init__()
        self.is_alive = is_alive
        self.active_level = active_level
        self.x_pos = 475
        self.y_pos = 375
        self.flip = False

        self.health = 100
        
        self.player_index = 0
        self.player_tool = []
        self.tool_status = False
        self.has_survivor = False

        if self.active_level is not None:
            if self.active_level == 0:
                self.player_tool = [
                    pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 5.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 4.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 3.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 2.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player','Top_View_Boat 1.png')).convert_alpha()
                ]
            elif self.active_level == 1:
                self.player_tool = [
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_1.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_2.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_3.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_4.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_5.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_6.png')).convert_alpha(),
                    pygame.image.load(os.path.join('assets','sprites','player_net','Net_7.png')).convert_alpha()
                ]
            elif self.active_level == 2:
                self.player_tool = [
                    pygame.image.load(os.path.join('assets','sprites','player','Hazmat.png'))
                ]

        self.image = pygame.transform.scale(self.player_tool[self.player_index], (250, 250))
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

    def extend_tool(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.tool_status = True
            if (self.player_index < (len(self.player_tool) - 1)):
                self.player_index += 1
                self.update_image()

    def retract_tool(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.tool_status = False
            if (self.player_index > 0):
                self.player_index -= 1
                self.update_image()

    def update_image(self):
        if self.flip:
            self.image = pygame.transform.scale(self.player_tool[self.player_index], (250, 250))
            self.image = pygame.transform.flip(pygame.transform.scale(self.player_tool[self.player_index], (250, 250)), True, False)
        else:
            self.image = pygame.transform.scale(self.player_tool[self.player_index], (250, 250))

    def update(self):
        self.update_image()
        self.extend_tool()
        self.retract_tool()

    def reset(self):
        self.is_alive = True
        self.has_survivor = False
        self.tool_status = False
        self.health = 100