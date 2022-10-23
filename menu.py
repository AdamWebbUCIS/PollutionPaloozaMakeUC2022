import pygame, sys, os
from utils.utils import Button

pygame.init()

SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Menu")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join("assets", "fonts", "font.ttf"), size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(500, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(500, 460), 
                            text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_X_POS = 515
        OPTIONS_Y_POS = 165

        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(45).render("CONTROLS", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)


        OPTIONS_TEXT = get_font(35).render("W = move up", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Y_POS += 40
        OPTIONS_TEXT = get_font(35).render("A = move left", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Y_POS += 40
        OPTIONS_TEXT = get_font(35).render("S = move down", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Y_POS += 40
        OPTIONS_TEXT = get_font(35).render("D = move right", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Y_POS += 80
        OPTIONS_TEXT = get_font(35).render("E = extend tool", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Y_POS += 40
        OPTIONS_TEXT = get_font(35).render("R = retract tool", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Y_POS += 80
        OPTIONS_TEXT = get_font(35).render("C = pickup item", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(OPTIONS_X_POS, OPTIONS_Y_POS))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(500, 760), 
                            text_input="BACK", font=get_font(35), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.fill("black")
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Pollution Palooza", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(500, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join("assets", "buttons", "Play Rect.png")), pos=(500, 250), 
                            text_input="PLAY", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join("assets", "buttons", "Options Rect.png")), pos=(500, 400), 
                            text_input="CONTROLS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join("assets", "buttons", "Quit Rect.png")), pos=(500, 550), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()