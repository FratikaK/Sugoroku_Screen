import abc
import pygame
from pygame.locals import *

# 初期化
pygame.init()
# global
screen = pygame.display.set_mode((1280, 640))
clock = pygame.time.Clock()
backImg = pygame.image.load('Grass2_5_32bit.png')  # 座標(0,128,32,32)
# エフェクト表示用のGroup
effect_group = pygame.sprite.Group()

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
        self.draw_effect()
        pygame.display.update()
        clock.tick(tick)

    def draw_effect(self):
        effect_group.draw(screen)
        effect_group.update()

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

    # text:[文字],posi:(左上の座標),bold：boxの線の太さ、pudding:boxの線と一行目の余白
    def setTextBox_S(self, text, textColor, boxColor, posi, width, height, bold=1, size=25, puddingX=10, puddingY=10):
        self.setBox(boxColor, posi, width, height, bold)
        charPosi = (posi[0] + puddingX, posi[1] + puddingY)
        count = 1
        for char in text:
            self.setText_S(char, charPosi, size, textColor)
            charPosi = (charPosi[0], charPosi[1] + size)
            count += 1


# -----------------------------------------------------------------------------------
# 以下エフェクトクラス
# -----------------------------------------------------------------------------------
# 画面遷移を行う時に表示するエフェクト
class ScreenChangeEffect(pygame.sprite.Sprite):
    def __init__(self, next_screen_id: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/screen_change.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 0
        self.next_screen_id = next_screen_id
        self.wait_time = 10

    def update(self):
        if self.rect.x > 1100:
            self.rect.x -= 50
        elif 80 < self.rect.x <= 1100:
            self.rect.x -= 200
            if self.rect.x <= 0:
                self.rect.x = 0
        elif self.rect.x > 0:
            self.rect.x -= 50
            if self.rect.x <= 0:
                self.rect.x = 0

        elif self.rect.x <= 0:
            global ScreenNum
            if ScreenNum != self.next_screen_id:
                ScreenNum = self.next_screen_id
            if self.wait_time > 0:
                if self.rect.x <= 0:
                    self.rect.x = 0
                self.wait_time -= 1
            else:
                if self.rect.x > -50:
                    self.rect.x -= 10
                elif -1800 < self.rect.x <= -50:
                    self.rect.x -= 300
                else:
                    self.rect.x -= 10

            if self.rect.x < -1300:
                self.remove(effect_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# コインが増減する時に出現させるエフェクト
class CoinNumFontEffect(pygame.sprite.Sprite):
    def __init__(self, num: int, x_location, y_location):
        pygame.sprite.Sprite.__init__(self)
        if num > 0:
            self.color = (0, 255, 255)
            self.message = "+ " + str(num)
        else:
            self.color = (255, 0, 0)
            self.message = "- " + str(abs(num))
        self.font = pygame.font.SysFont("yugothicyugothicuisemiboldyugothicuibold", 30)
        self.image = self.font.render(self.message, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x_location, y_location)
        self.move_amount = 50

    def update(self):
        if self.move_amount >= 20:
            self.rect.y -= 20
            self.move_amount -= 20
        else:
            self.rect.y -= 1
            self.move_amount -= 1
            if self.move_amount < 0:
                self.remove(effect_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# 文字を右から左へ移動させるアニメーション
class ScreenLineFontEffect(pygame.sprite.Sprite):
    def __init__(self, message: str, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("yugothicyugothicuisemiboldyugothicuibold", 70)
        self.image = self.font.render(message, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 280

    def update(self):
        if self.rect.x > 600:
            self.rect.x -= 100
        elif 500 <= self.rect.x <= 600:
            self.rect.x -= 5
        else:
            self.rect.x -= 200
        if self.rect.x < -300:
            self.remove(effect_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# ウマが歩くだけのアニメーション
class UmaEffect(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.uma_images = [pygame.image.load("img/uma/uma01.png"),
                           pygame.image.load("img/uma/uma02.png"),
                           pygame.image.load("img/uma/uma03.png"),
                           pygame.image.load("img/uma/uma04.png"),
                           pygame.image.load("img/uma/uma05.png"),
                           pygame.image.load("img/uma/uma06.png")]
        self.image = self.uma_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 60

    def update(self):
        if self.index >= len(self.uma_images):
            self.remove(effect_group)
            return
        self.image = self.uma_images[self.index]
        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# 氷が出現して砕けるアニメーション
class IceEffect(pygame.sprite.Sprite):
    def __init__(self, x_location: int, y_location: int):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.effect_images = list()
        for i in range(1, 22):
            if i < 10:
                self.effect_images.append(pygame.image.load("img/effect/sample_effect_00" + str(i) + ".png"))
            else:
                self.effect_images.append(pygame.image.load("img/effect/sample_effect_0" + str(i) + ".png"))
        self.image = self.effect_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x_location, y_location)

    def update(self):
        if self.index >= len(self.effect_images):
            self.kill()
            return
        self.image = self.effect_images[self.index]
        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# 円が広がるようなエフェクトを表示する
class CircleEffect(pygame.sprite.Sprite):
    def __init__(self, x_location: int, y_location: int):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.effect_images = list()
        for i in range(1, 16):
            self.effect_images.append(pygame.image.load("img/circle/circle_effect" + str(i) + ".png"))
        self.image = self.effect_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x_location, y_location)

    def update(self):
        if self.index >= len(self.effect_images):
            self.kill()
            return
        self.image = self.effect_images[self.index]
        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
