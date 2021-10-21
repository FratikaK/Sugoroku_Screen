import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

images = [pygame.image.load("img/uma/uma01.png"),
          pygame.image.load("img/uma/uma02.png"),
          pygame.image.load("img/uma/uma03.png"),
          pygame.image.load("img/uma/uma04.png"),
          pygame.image.load("img/uma/uma05.png"),
          pygame.image.load("img/uma/uma06.png")]

texts = ["Now Loading", "Now Loading.", "Now Loading..", "Now Loading...", "Now Loading....", "Now Loading....."]

index = 0


class ScreenLoading(Screen_abc):
    """
    NowLoadingを表示させるだけの画面
    """

    def __init__(self):
        super().__init__()
        self.count = 0
        self.flag = False

    def __initialize(self):
        self.count = 0
        self.flag = False

    def display(self):
        global index
        SC.screen.fill((0, 0, 0))
        SC.screen.blit(images[index], (1160, 550))
        index = index + 1
        if index > len(images) - 1:
            index = 0
        super().setText_M(texts[index], (820, 570), 40)

        if not self.flag:
            self.count += 1
            if self.count > 80:
                self.flag = True
            super().update(10)
            return
        else:
            SC.effect_group.add(SC.ScreenChangeEffect(3))
            self.__initialize()
            super().update(30)

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
