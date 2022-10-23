import pygame
from sys import exit
from manager import Manager
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()
    
    player = Player()
    manager = Manager(player, screen)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        manager.run_level()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(128)

if __name__ == "__main__":
    main()