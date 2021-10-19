import pygame
from pygame.locals import *

import Screen_abc as SC


class GameManagement:
    def __init__(self):
        self.screen = []

    def start_game(self):
        while True:
            self.screen[SC.ScreenNum].reflect_display()


if __name__ == '__main__':
    GameManagement().start_game()
