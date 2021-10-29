import abc
import pygame
from pygame.locals import *
import effect

# 初期化

pygame.init()
# global
screen = pygame.display.set_mode((1280, 640))
clock = pygame.time.Clock()
backImg = pygame.image.load('Grass2_5_32bit.png')  # 座標(0,128,32,32)

# スクリーン切り替え用変数
ScreenNum = 0

# Set Up Colors
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
Navy_Blue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)


class Screen_abc(metaclass=abc.ABCMeta):
    def __init__(self):
        grid = [[0 for j in range(20)] for i in range(40)]
        for i in range(40):
            for j in range(20):
                grid[i][j] = (i * 32, j * 32)
        self.grid = tuple(grid)

        self.Font_L = 'hg創英角ﾎﾟｯﾌﾟ体hgp創英角ﾎﾟｯﾌﾟ体hgs創英角ﾎﾟｯﾌﾟ体'
        self.Font_M = 'yugothicyugothicuisemiboldyugothicuibold'
        self.Font_S = 'simsunnsimsun'

    @abc.abstractmethod
    def display(self):
        pass

    @abc.abstractmethod
    def getEvent(self):
        pass

    def update(self, tick=10):
        effect.group.draw(screen)
        effect.group.update()
        pygame.display.update()
        clock.tick(tick)

    def setBackground(self, imag, imagePosi=(0, 0, 32, 32)):
        for i in self.grid:
            for j in i:
                screen.blit(imag, j, imagePosi)

    # 1280 640以上のサイズの画像を背景にする
    def set_background(self, imag):
        screen.blit(imag, (0, 0))

    # game_managementで実際に使用する
    def reflect_display(self):
        self.display()
        self.getEvent()

    def setText_L(self, text, position, size, color=White):
        font = pygame.font.SysFont(self.Font_L, size)
        message = font.render(text, False, color)
        screen.blit(message, position)

    def setText_M(self, text, position, size, color=White):
        font = pygame.font.SysFont(self.Font_M, size)
        message = font.render(text, False, color)
        screen.blit(message, position)

    def setText_S(self, text, position, size=25, color=White):
        font = pygame.font.SysFont(self.Font_S, size)
        message = font.render(text, False, color)
        screen.blit(message, position)

    # posi:左上の座標(タプル)、widht:boxの横幅,height:boxの高さ,bold：boxの線の太さ
    def setBox(self, color, posi, width, height, bold=1):
        # screenオブジェクト、左上の座標、図形の形(x,y,width,height)
        leftY = posi[1] + height
        rightX = posi[0] + width
        pygame.draw.rect(screen, color, posi + (width, bold))
        pygame.draw.rect(screen, color, posi + (bold, height))
        pygame.draw.rect(screen, color, (rightX, posi[1]) + (bold, height))
        pygame.draw.rect(screen, color, (posi[0], leftY) + (width, bold))

    def setTextBox_S(self, text, textColor, boxColor, posi, width, height, bold=1, size=25, puddingX=10, puddingY=10):
        """
        :param text: text:[文字]
        :param textColor:
        :param boxColor:
        :param posi: (左上の座標)
        :param width:
        :param height:
        :param bold: boxの線の太さ
        :param size:
        :param puddingX: boxの線と一行目の余白 x
        :param puddingY: boxの線と一行目の余白 y
        """
        self.setBox(boxColor, posi, width, height, bold)
        charPosi = (posi[0] + puddingX, posi[1] + puddingY)
        count = 1
        for char in text:
            self.setText_S(char, charPosi, size, textColor)
            charPosi = (charPosi[0], charPosi[1] + size)
            count += 1