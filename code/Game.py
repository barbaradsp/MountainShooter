import pygame

from code.Const import *
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            if menu_return == MENU_OPTION[3]:
                pass
            else:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
