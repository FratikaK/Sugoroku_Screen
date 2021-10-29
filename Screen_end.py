import pygame
from pygame.locals import *

import Screen_abc as SC
import effect
from Screen_abc import Screen_abc
import sys


class ScreenEnd(Screen_abc):

    def display(self):
        super().update()

        # 背景画像
        background = pygame.image.load("img/kanno_img/aa.jpg")
        SC.screen.blit(background, self.grid[0][0])
        # かぼちゃの画像
        panpkin = pygame.image.load("img/kanno_img/pipo-halloweenchara2016_01.png")
        SC.screen.blit(panpkin, (self.grid[18][10][0] + 4, self.grid[18][10][1]))
        # player横の人間画像
        coinimg = pygame.image.load("img/kanno_img/sticon2b-3.png")
        Playerimg = pygame.image.load("img/kanno_img/ozaki32.png")
        # 人間の画像
        character1 = pygame.image.load("img/kanno_img/pipo-charachip001a.png")
        SC.screen.blit(character1, self.grid[35][5])
        # お相撲さんの画像
        character2 = pygame.image.load("img/kanno_img/男_赤ふんどし.png")
        SC.screen.blit(character2, self.grid[35][9])
        # 黒人の画像
        character3 = pygame.image.load("img/kanno_img/sample038.png")
        SC.screen.blit(character3, self.grid[35][13])

        # プレイヤー、順位、コイン数の縦位置の変数
        # プレイヤーらの画像のパスを保持している配列
        imgID = 6
        ranking = ["img/kanno_img/iti.png", "img/kanno_img/nii.png", "img/kanno_img/sani.png", "img/kanno_img/yoni.png"]
        for i in ranking:
            resultimg = pygame.image.load(i).convert()
            farst = resultimg.get_at((0, 0))
            resultimg.set_colorkey(farst, RLEACCEL)
            SC.screen.blit(resultimg, self.grid[12][imgID])
            SC.screen.blit(coinimg, self.grid[26][imgID])
            SC.screen.blit(Playerimg, self.grid[2][imgID])
            imgID += 3

        super().setText_L('Result', (self.grid[17][1][0] + 17, self.grid[17][1][1]), 55, (255, 255, 255))

        # self.grid[][][0]+intで縦のピクセル指定
        super().setText_M('Player', (self.grid[2][3][0] + 15, self.grid[2][3][1]), 45, (255, 131, 0))
        super().setText_M('Ranking', (self.grid[11][3][0] + 18, self.grid[12][3][1]), 45, (255, 131, 0))
        super().setText_M('Coin', self.grid[26][3], 45, (255, 131, 0))

        super().setText_M('player1', self.grid[3][6], 35, (255, 131, 0))
        super().setText_M('player2', self.grid[3][9], 35, (255, 131, 0))
        super().setText_M('player3', self.grid[3][12], 35, (255, 131, 0))
        super().setText_M('player4', self.grid[3][15], 35, (255, 131, 0))

        super().setText_M('1st', (self.grid[13][6][0] + 5, self.grid[13][6][1]), 35, (255, 131, 0))
        super().setText_M('2nd', (self.grid[13][9][0] + 5, self.grid[13][9][1]), 35, (255, 131, 0))
        super().setText_M('3rd', (self.grid[13][12][0] + 5, self.grid[13][12][1]), 35, (255, 131, 0))
        super().setText_M('4th', (self.grid[13][15][0] + 5, self.grid[13][15][1]), 35, (255, 131, 0))

        super().setText_M('400', (self.grid[27][6][0], self.grid[27][6][1]), 35, (255, 131, 0))
        super().setText_M('300', (self.grid[27][9][0], self.grid[27][9][1]), 35, (255, 131, 0))
        super().setText_M('200', (self.grid[27][12][0], self.grid[27][12][1]), 35, (255, 131, 0))
        super().setText_M('100', (self.grid[27][15][0], self.grid[27][15][1]), 35, (255, 131, 0))

        super().setText_M('▷もう一度同じ設定で遊ぶ', self.grid[4][18], 40, (255, 255, 255))
        super().setText_M('タイトルに戻る', self.grid[22][18], 40, (255, 255, 255))

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
                    effect.add_effect(effect.ScreenChangeEffect(0))

                if event.key == K_e:
                    effect.add_effect(effect.ScreenChangeEffect(0))
