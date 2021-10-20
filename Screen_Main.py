import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

# window画像
player1_window = pygame.image.load("img/window/player1_window.png")
player2_window = pygame.image.load("img/window/player2_window.png")
player3_window = pygame.image.load("img/window/player3_window.png")
player4_window = pygame.image.load("img/window/player4_window.png")
string_window = pygame.image.load("img/window/string_window.png")
end_window = pygame.image.load("img/window/end_window.png")
turn_window = pygame.image.load("img/window/turn_window.png")
item_title_window = pygame.image.load("img/window/item_title.png")
item_window = pygame.image.load("img/window/item_window.png")

# サイコロ画像
dice1 = pygame.image.load("img/oomoto_img/Dice1.jpg")

# その他画像
ozaki_img = pygame.image.load('img/oomoto_img/Ozaki.png')
coin_img = pygame.image.load('img/oomoto_img/Coin.png')
building1_img = pygame.image.load('img/oomoto_img/Building1.png')
building2_img = pygame.image.load('img/oomoto_img/Building2.png')

# マス画像
blue_img = pygame.image.load('img/oomoto_img/Blue.png')
red_img = pygame.image.load('img/oomoto_img/Red.png')
yellow_img = pygame.image.load('img/oomoto_img/Yellow.png')
orange_img = pygame.image.load('img/oomoto_img/Orange.png')
purple_img = pygame.image.load('img/oomoto_img/Purple.png')


class ScreenMain(Screen_abc):

    # 画面生成
    def display(self):
        super().update()

        # 背景
        super().setBackground(SC.backImg, (0, 128, 32, 32))

        # プレイヤー情報欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        SC.screen.blit(player1_window, (0, 0))
        SC.screen.blit(player2_window, (320, 0))
        SC.screen.blit(player3_window, (640, 0))
        SC.screen.blit(player4_window, (960, 0))

        for i in range(4):
            # super().setBox(SC.Black, (i * 32 * 10, 0), 32 * 10, 32 * 3, 3)  # 外枠
            # display_player_color = pygame.Rect(i * 32 * 10 + 3, 3, 32 * 10 - 3, 32 * 3 - 3)  # 背景色
            # pygame.draw.rect(SC.screen, SC.White, display_player_color)  # 背景色を枠内に配置
            SC.screen.blit(ozaki_img, ((32 * 2 + 16) + (i * 32 * 10), 32 + 18))  # プレイヤーアイコン
            SC.screen.blit(coin_img, ((32 * 6 + 8) + (i * 32 * 10), 32 - 12))  # コインアイコン
            SC.screen.blit(building1_img, ((32 * 6 + 8) + (i * 32 * 10), 32 + 18))  # 物件アイコン
            super().setText_S('Player' + str(i + 1), ((32 * 2) + (i * 32 * 10), 32 - 14), 22, SC.Black)  # プレイヤー名（仮）
            super().setText_L(str(i + 1), ((32 * 1 + 2) + (i * 32 * 10), 32 + 22), 26, SC.Black)  # 順位（仮）
            super().setText_S('0枚', ((32 * 7 + 16) + (i * 32 * 10), 32 - 16), 22, SC.Black)  # コイン数
            super().setText_S('0件', ((32 * 7 + 16) + (i * 32 * 10), 32 + 18), 22, SC.Black)  # 物件数
            i += 1
        # pygame.draw.rect(SC.screen, SC.Black, pygame.Rect(32 * 40 - 3, 32 * 0, 3, 32 * 3))  # 右端の外枠線を追加

        # プレイヤー情報欄の現在のプレイヤーのカーソル（仮）
        super().setText_S('●', (32 * 1, 32 - 12), 20, SC.Red)

        # 青マスを上辺と下辺に配置
        for i in range(12):
            SC.screen.blit(blue_img, self.grid[8 + i * 2][5])
            SC.screen.blit(blue_img, self.grid[8 + i * 2][13])
            i += 1

        # 青マスを左辺と右辺に配置
        for i in range(3):
            SC.screen.blit(blue_img, self.grid[8][7 + i * 2])
            SC.screen.blit(blue_img, self.grid[30][7 + i * 2])
            i += 1

        # 赤マスを上辺と下辺に配置
        for i in range(3):
            SC.screen.blit(red_img, self.grid[12 + i * 8][5])
            SC.screen.blit(red_img, self.grid[10 + i * 8][13])
            i += 1

        # 赤マスを左辺に配置
        SC.screen.blit(red_img, self.grid[8][9])

        # 黄色マス（物件マス）を配置
        SC.screen.blit(yellow_img, self.grid[24][5])
        SC.screen.blit(yellow_img, self.grid[22][13])

        # オレンジ色マス（ボーナスマス）を配置
        SC.screen.blit(orange_img, self.grid[14][13])

        # 紫色マス（特大マイナスマス）を配置
        SC.screen.blit(purple_img, self.grid[30][9])

        # 物件を配置（仮）
        SC.screen.blit(building2_img, (32 * 24, 32 * 3 + 18))
        SC.screen.blit(building2_img, (32 * 22, 32 * 11 + 13))

        # アイテムを配置（仮）
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*29, 32*11+5))
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*20+5, 32*12))

        # マス上に各プレイヤーを配置（仮）
        SC.screen.blit(ozaki_img, self.grid[14][5])  # 現在のプレイヤー
        SC.screen.blit(ozaki_img, self.grid[26][5])
        SC.screen.blit(ozaki_img, self.grid[30][5])
        SC.screen.blit(ozaki_img, self.grid[24][13])

        # マス上の現在のプレイヤーのカーソル（仮）
        super().setText_S('▼', self.grid[14][4], 32, SC.Red)  # 現在のプレイヤー
        super().setText_S('▼', self.grid[24][12], 32, SC.Blue)

        # ターン表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        # display_turn_color = pygame.Rect(32 * 1, 32 * 5, 32 * 5, 32 * 9)
        # pygame.draw.rect(SC.screen, SC.White, display_turn_color)
        # super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][5], 32 * 5, 32 * 9, 3, 25, 10, 10)
        SC.screen.blit(turn_window, (32, 160))
        super().setText_S('ターン', (32 * 2, 32 * 6), 35)
        super().setText_S('3/15', (32 * 2 + 5, 32 * 8 + 10), 45)
        super().setText_S('【序盤】', (32 + 12, 32 * 11 + 10), 35)

        # ゲーム終了ボタン
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        # button_color = pygame.Rect(32 * 1, 32 * 16, 32 * 5, 32 * 2)
        # pygame.draw.rect(SC.screen, SC.White, button_color)
        # super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][16], 32 * 5, 32 * 2, 3, 25, 10, 10)
        SC.screen.blit(end_window, (32, 512))
        super().setText_S('ゲーム終了', (32 * 1 + 16, 32 * 16 + 20), 25)

        # 説明表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        # display_desc_color = pygame.Rect(32 * 8, 32 * 15, 32 * 23, 32 * 4)
        # pygame.draw.rect(SC.screen, SC.White, display_desc_color)
        # super().setTextBox_S(text, SC.Black, SC.Black, self.grid[8][15], 32 * 23, 32 * 4, 3, 30, 20, 20)
        SC.screen.blit(string_window, (256, 480))
        text = ['アイテム名：BBBBB', '　アイテムの説明']
        super().setText_S(text[0], self.grid[8][15])
        super().setText_S(text[1], self.grid[8][16])

        # サイコロ表示欄
        SC.screen.blit(dice1, self.grid[35][5])

        # アイテム表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        # super().setText_L('アイテム', (32 * 35, 32 * 10), 24, SC.Black)
        # display_item_color = pygame.Rect(32 * 34, 32 * 11, 32 * 5, 32 * 3)
        # pygame.draw.rect(SC.screen, SC.White, display_item_color)
        SC.screen.blit(item_title_window, (1120, 320))
        SC.screen.blit(item_window, (1088, 352))

        text = ['▼AAAAA', '▼BBBBB', '▼CCCCC']
        grid_y = 11
        for i in text:
            # super().setTextBox_S(text, SC.Black, SC.Black, self.grid[34][11], 32 * 5, 32 * 3, 3, 25, 10, 10)
            super().setText_S(i, self.grid[34][grid_y])
            grid_y += 1
        super().setText_S('←', (32 * 37 + 12, 32 * 12 + 2), 30, SC.Red)

    # イベント処理
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
                    SC.effect_group.add(SC.ScreenChangeEffect(3))
