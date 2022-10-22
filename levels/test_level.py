import pygame
from player import Player
from level import Level


class TestLevel(Level):
    def __init__(self, player: Player, screen: pygame.Surface, screen_pos=[], passed=False) -> None:
        super().__init__(player, screen, passed)
        self.group = pygame.sprite.GroupSingle()
        self.screen_pos = screen_pos
        
    def draw_level(self):
        super().draw_level()
        self.group.add(self.player)
        img = pygame.image.load("assets\sprites\Scary_Sea_Monster_.png").convert_alpha()
        r = pygame.transform.scale(img, (100, 100))
        self.screen.blit(r, (0-self.screen_pos[0],0-self.screen_pos[1]))
        self.group.draw(self.screen)
