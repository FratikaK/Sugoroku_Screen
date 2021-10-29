import pygame
from pygame.locals import *

import Screen_abc as SC
import Screen_setting
from Screen_setting import *
from Screen_abc import Screen_abc
import sys

# width = 1280
# height = 640

selectY = 0  # 選択アイコンの座標
menu = ['ひとりで遊ぶ', 'みんなで遊ぶ']  # メニューのリスト

# 画像はstaticで先にロードしておくといいです
selecticonList = [pygame.image.load('img/ozaki_img/dice1.png'),
                  pygame.image.load('img/ozaki_img/dice2.png')]  # アイコンのimageのリスト


# selectYの座標を計算
def y(y):
    global selectY
    selectY = selectY + y


class ScreenStart(Screen_abc):

    def display(self):
        pygame.display.set_caption("スタート画面")
        super().update()

        # 背景画面
        background = pygame.image.load("img/ozaki_img/1021023_coin_fall_1-1.jpg")
        SC.screen.blit(background, self.grid[0][0])

        # 罫線
        # pygame.draw.line(SC.screen, SC.Black, (0,0),(width,0), 2) 
        # pygame.draw.line(SC.screen, SC.Black, (0,height/2),(width,height/2), 1) #横線
        # pygame.draw.line(SC.screen, SC.Black, (width/2,0),(width/2,height), 1)  #縦線

        # キャラクターの出力
        leftcharacter = pygame.image.load("img/ozaki_img/画像テストウルトラマン.png")  # 左のキャラクター
        rightcharacter = pygame.image.load("img/ozaki_img/画像テストウルトラマンかぼちゃ.png")  # 右のキャラクター
        SC.screen.blit(leftcharacter, self.grid[1][4])
        SC.screen.blit(rightcharacter, self.grid[30][4])

        super().setText_L('すごろく', self.grid[16][4], 64, SC.Black)  # タイトル

        # タイトルの左のサイコロ
        leftsugoroku = pygame.image.load("img/ozaki_img/1.png")
        leftsugoroku = pygame.transform.scale(leftsugoroku, (100, 100))
        SC.screen.blit(leftsugoroku, self.grid[13][3])

        # タイトルの右のサイコロ
        rightsugoroku = pygame.image.load("img/ozaki_img/6.png")
        rightsugoroku = pygame.transform.scale(rightsugoroku, (100, 100))
        SC.screen.blit(rightsugoroku, self.grid[24][3])

        # super().setBox(SC.Black,self.grid[16][12],32*8-5,32*6)

        # メニューの出力
        for i, font in enumerate(menu):
            menuBackground = pygame.Rect(544, 416 + (32 * i * 3) - 3, 32 * 6, 32 * 1)
            pygame.draw.rect(SC.screen, (150, 150, 150), menuBackground)
            super().setText_M(font, self.grid[18][13 + i * 3], 25, SC.Black)

            # メニューを選択するときのアイコン
        selecticon = pygame.transform.scale(selecticonList[selectY], (25, 25))
        SC.screen.blit(selecticon, self.grid[17][13 + selectY * 3])

    def getEvent(self):
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    if selectY == 0:
                        Screen_setting.SOLO = False
                    elif selectY == 1:
                        Screen_setting.SOLO = True
                    effect.add_effect(effect.ScreenChangeEffect(1, effect.ScreenChangeEffect.MOSAIC))
                if event.key == K_UP:  # 「↑」が押されたとき
                    if selectY > 0:
                        y(-1)
                        print(selectY)  # 確認用
                if event.key == K_DOWN:  # 「↓」が押されたとき
                    if selectY < len(menu) - 1:
                        y(1)
                        print(selectY)  # 確認用
