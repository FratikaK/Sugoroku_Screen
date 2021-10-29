import pygame
from pygame.locals import *

import Screen_abc as SC
import effect
from Screen_abc import Screen_abc
import sys

# 背景画像
background_img = pygame.image.load("img/oomoto_img/background_img.png")

# window画像
player1_window = pygame.image.load("img/oomoto_img/window/player1_window.png")
player2_window = pygame.image.load("img/oomoto_img/window/player2_window.png")
player3_window = pygame.image.load("img/oomoto_img/window/player3_window.png")
player4_window = pygame.image.load("img/oomoto_img/window/player4_window.png")
player_icon = pygame.image.load('img/oomoto_img/window/player_icon.png')
coin_img = pygame.image.load('img/oomoto_img/window/coin.png')
building_img = pygame.image.load('img/oomoto_img/window/building.png')
string_window = pygame.image.load("img/oomoto_img/window/string_window.png")
end_window = pygame.image.load("img/oomoto_img/window/end_window.png")
turn_window = pygame.image.load("img/oomoto_img/window/turn_window.png")
item_title_window = pygame.image.load("img/oomoto_img/window/item_title.png")
item_window = pygame.image.load("img/oomoto_img/window/item_window.png")
dice1 = pygame.image.load("img/oomoto_img/window/dice1.jpg")

# フィールド画像
castle_img = pygame.image.load('img/oomoto_img/object/castle.png')
tower_img = pygame.image.load('img/oomoto_img/object/tower.png')
budda_img = pygame.image.load('img/oomoto_img/object/budda.png')
hotspring_img = pygame.image.load('img/oomoto_img/object/hotspring.png')
shrine_img = pygame.image.load('img/oomoto_img/object/shrine.png')
shop_img = pygame.image.load('img/oomoto_img/object/shop.png')
ship_img = pygame.image.load('img/oomoto_img/object/ship.png')
ship_small_img = pygame.image.load('img/oomoto_img/object/ship_small.png')
pinetree_img = pygame.image.load('img/oomoto_img/object/pinetree.png')

# マス画像
blue_img = pygame.image.load('img/oomoto_img/blue.png')
red_img = pygame.image.load('img/oomoto_img/red.png')
green_img = pygame.image.load('img/oomoto_img/green.png')
purple_img = pygame.image.load('img/oomoto_img/purple.png')


class ScreenMain(Screen_abc):

    # 画面生成
    def display(self):
        super().update()

        # 背景
        SC.screen.blit(background_img, (0, 0))

        # プレイヤー情報window
        SC.screen.blit(player1_window, (0, 0))
        SC.screen.blit(player2_window, (320, 0))
        SC.screen.blit(player3_window, (640, 0))
        SC.screen.blit(player4_window, (960, 0))

        for i in range(4):
            SC.screen.blit(player_icon, ((32 * 2 + 16) + (i * 32 * 10), 32 + 18))  # プレイヤーアイコン
            SC.screen.blit(coin_img, ((32 * 6 + 8) + (i * 32 * 10), 32 - 12))  # コインアイコン
            SC.screen.blit(building_img, ((32 * 6 + 8) + (i * 32 * 10), 32 + 18))  # 物件アイコン
            super().setText_S('Player' + str(i + 1), ((32 * 2) + (i * 32 * 10), 32 - 14), 22, SC.Black)  # プレイヤー名
            super().setText_L(str(i + 1), ((32 * 1 + 2) + (i * 32 * 10), 32 + 22), 26, SC.Black)  # 順位
            super().setText_S('0枚', ((32 * 7 + 16) + (i * 32 * 10), 32 - 16), 22, SC.Black)  # コイン数
            super().setText_S('0件', ((32 * 7 + 16) + (i * 32 * 10), 32 + 18), 22, SC.Black)  # 物件数
            i += 1

        # 現在のプレイヤーのカーソル
        super().setText_S('●', (32 * 1 - 3, 32 - 12), 20, SC.White)

        # 青マス（コイン＋）
        for i in range(12):
            SC.screen.blit(blue_img, self.grid[8 + i * 2][5])
            SC.screen.blit(blue_img, self.grid[8 + i * 2][13])
            i += 1

        # 赤マス（コイン－）
        SC.screen.blit(red_img, self.grid[18][5])
        SC.screen.blit(red_img, self.grid[22][5])
        SC.screen.blit(red_img, self.grid[28][5])
        for i in range(11):
            if (i != 5 and i != 7 and i != 9):
                SC.screen.blit(red_img, self.grid[8 + i * 2][13])
            i += 1

        # 紫色マス（特大－マス）
        SC.screen.blit(purple_img, self.grid[12][5])
        SC.screen.blit(purple_img, self.grid[26][13])

        # 緑色マス（物件マス）
        for i in range(5):
            SC.screen.blit(green_img, self.grid[8][5 + i * 2])
            SC.screen.blit(green_img, self.grid[30][5 + i * 2])
            i += 1

        # 物件
        SC.screen.blit(ship_small_img, self.grid[28][4])
        SC.screen.blit(ship_small_img, self.grid[31][5])
        SC.screen.blit(tower_img, self.grid[29][6])
        SC.screen.blit(tower_img, self.grid[29][10])
        SC.screen.blit(ship_small_img, self.grid[31][13])
        SC.screen.blit(ship_small_img, self.grid[28][14])

        # フィールドのオブジェクト
        SC.screen.blit(castle_img, (32 * 17 + 16, 32 * 7 + 8))
        SC.screen.blit(budda_img, (32 * 9 + 4, 32 * 9 - 10))
        SC.screen.blit(budda_img, (32 * 26, 32 * 6))
        SC.screen.blit(shrine_img, (32 * 12 - 4, 32 * 6 + 10))
        SC.screen.blit(shop_img, (32 * 21 + 10, 32 * 6))
        SC.screen.blit(shop_img, (32 * 12 + 8, 32 * 10 + 10))
        SC.screen.blit(ship_img, (32 * 33 + 16, 32 * 14 + 10))
        SC.screen.blit(hotspring_img, (32 * 22 + 22, 32 * 10))
        SC.screen.blit(hotspring_img, (32 * 25 + 22, 32 * 10))
        SC.screen.blit(pinetree_img, (32 * 9 + 24, 32 * 6 + 20))
        SC.screen.blit(pinetree_img, (32 * 12, 32 * 9 + 2))
        SC.screen.blit(pinetree_img, (32 * 14, 32 * 9 + 2))
        SC.screen.blit(pinetree_img, (32 * 16, 32 * 6 + 8))
        SC.screen.blit(pinetree_img, (32 * 18, 32 * 6 + 8))
        SC.screen.blit(pinetree_img, (32 * 17 - 12, 32 * 8 + 8))
        SC.screen.blit(pinetree_img, (32 * 22, 32 * 8 + 16))
        SC.screen.blit(pinetree_img, (32 * 24, 32 * 8 + 16))

        # サイコロ
        SC.screen.blit(dice1, self.grid[35][5])

        # ゲーム終了ボタン
        SC.screen.blit(end_window, (32, 512))
        super().setText_S('ゲーム終了', (32 * 1 + 16, 32 * 16 + 20), 25)

        # ターン表示window
        SC.screen.blit(turn_window, (32, 160))
        super().setText_S('ターン', (32 * 2, 32 * 6), 35)
        super().setText_S('3/15', (32 * 2 + 5, 32 * 8 + 10), 45)
        super().setText_S('【序盤】', (32 + 12, 32 * 11 + 10), 35)

        # 説明表示window
        SC.screen.blit(string_window, (256, 480))
        text = ['アイテム名：BBBBB', '　アイテムの説明']
        super().setText_S(text[0], self.grid[8][15])
        super().setText_S(text[1], self.grid[8][16])

        # アイテム表示window
        SC.screen.blit(item_title_window, (1120, 320))
        SC.screen.blit(item_window, (1088, 352))

        text = ['▼AAAAA', '▼BBBBB', '▼CCCCC']
        grid_y = 11
        for i in text:
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
                    effect.add_effect(effect.ScreenChangeEffect(4))
