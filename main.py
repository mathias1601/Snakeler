import pygame

from src.options import WIDTH, HEIGHT
from src.main_menu import MainMenu
from src.game import run


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    menu = MainMenu(screen)
    start_game = menu.run()

    if start_game:
        run(screen)
    else:
        pygame.quit()


if __name__ == "__main__":
    main()