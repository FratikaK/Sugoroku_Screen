from typing import Text
import pygame

from pygame.locals import *

from Screen_abc import *
import Screen_abc as SC

import TextSlice

import random

import sys

MAX_GRIDPOSI = 2147483647 - 1000000000

ALLPROGRAM_NUMBER = [0, 1]  # どのぐらい工程が増えるかは未定

PROGRAM1 = ['バトルテスト画面です。', 'スペースキーを押すと次のテキストが表示されます', '三行目のテスト']
PROGRAM2 = ['次の文はサイコロを振ってくださいというようなテキストを想定しています。', 'サイコロが回り始める...']
PROGRAM3 = ['一人目のプレイヤーがサイコロを投げる']
PROGRAM4 = ['二人目のプレイヤーがサイコロを投げる']
PROGRAM5 = ['勝利者への案内を表示など']
PROGRAM6 = ['終了の案内を表示']

# 定数の配列
PROGRAM_ARRAY = [PROGRAM1, PROGRAM2, PROGRAM3, PROGRAM4, PROGRAM5, PROGRAM6]


class ScreenEncount(Screen_abc):

    def __init__(self):
        super(ScreenEncount, self).__init__()
        self.TextSlice_obj = TextSlice.TextSlice()

        self.Winner_WidthPosi = []
        self.Winner_HeightPosi = [11, 12, 13]
        self.CurrentProgram = ALLPROGRAM_NUMBER[0]

        # 何の文章を表示するか決定するID番号
        self.Program_text_number = 0

        # どのオブジェクトを表示するか決定する変数
        self.FlyVoidProgram0 = MAX_GRIDPOSI
        self.FlyVoidProgram1 = MAX_GRIDPOSI

        # 勝者をランダムに決めるためのプログラム、実際のゲームに実装はしない--
        self.Winner_num = -1
        self.Winner_num = random.randint(1, 2)
        if self.Winner_num == 1:
            self.Winner_WidthPosi = [0]
        else:
            self.Winner_WidthPosi = [24]

        # --------------------------------------------------------------

    def display(self):

        super().update(30)

        # 背景を表示しているのでscreen.fillは大丈夫です
        # Screen_abc.screen.fill(Screen_abc.Black)

        # 工程の切り替え
        self.CurrentProgramjudge()

        # イメージ画像をロード、表示している
        self.img_load()

        # テキストをロード,表示している
        self.text_load()

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

                # スペースで変数を変更し、表示するテキストやオブジェクトを変更する
                if event.key == K_SPACE:

                    # 現在表示しているオブジェクトが1に割り振られているものなら
                    if self.CurrentProgram == 1:
                        # 配列の5個目の文字列を表示
                        self.Program_text_number = 5

                        # 内部変数のリセットのために設置したものの、特に使用しなかった。
                        self.variable_init()

                        # 現在表示するオブジェクトを0に割り振っているものに変更
                        self.CurrentProgram = 0

                    # 内部変数のリセットのために設置したものの、特に使用しなかった。
                    self.variable_init()

                    # 表示するテキストが工程0の時の最終段まで到達したときに
                    if self.Program_text_number == 4:
                        # 表示するオブジェクトを1に割り振っているものに変更
                        self.CurrentProgram = 1

                    if self.Program_text_number == 5:
                        SC.effect_group.add(SC.ScreenChangeEffect(4))

                    # 表示するテキストが工程0の時の最終段以前の時は
                    if self.Program_text_number < 4:
                        # 表示するテキストを更新
                        self.Program_text_number = self.Program_text_number + 1

                if event.key == K_q:
                    # 親クラスに作った変数を削除
                    del Screen_abc.Player1CharaID

                    del Screen_abc.Player2CharaID

                    del Screen_abc.BattleBackGroundID

                    # 変数を初期化しようとおもったが特に使用することはなかった
                    self.variable_init()

                    # クラス変数の初期化
                    self.CurrentProgram = 0

                    self.Program_text_number = 0

                    Screen_abc.ScreenNum = 2

    # 使用するイメージをロードする処理をまとめたもの、ついでに配置もここで行う
    def img_load(self):

        backgroundimg = pygame.image.load('img/suzuki_img/戦闘背景_sample' + str(Screen_abc.BattleBackGroundID) + '.png')

        player1img = pygame.image.load('img/suzuki_img/chara' + str(Screen_abc.Player1CharaID) + '_migi.png')

        player2img = pygame.image.load('img/suzuki_img/chara' + str(Screen_abc.Player2CharaID) + '_hidari.png')

        dice_testimg = pygame.image.load('img/suzuki_img/dicesample.jpg')

        screen.blit(backgroundimg, self.grid[0][0])

        screen.blit(dice_testimg,
                    (self.grid[19][5][0] + self.FlyVoidProgram0, self.grid[19][5][1] + self.FlyVoidProgram0))

        screen.blit(player1img, self.grid[9][7])

        screen.blit(player2img, self.grid[30][7])

    # 表示するテキストをまとめたもの。文字の表示もここで行う
    def text_load(self):
        super().setTextBox_S(self.TextSlice_obj.One_letter(PROGRAM_ARRAY[self.Program_text_number]), White,
                             White,
                             (self.grid[5][14][0] + self.FlyVoidProgram0, self.grid[5][14][1] + self.FlyVoidProgram0),
                             32 * 30, 32 * 5, 1, 25, 10, 10)

        super().setText_S('勝ったのはプレイヤー' + str(self.Winner_num) + 'と想定',
                          (self.grid[10][0][0] + self.FlyVoidProgram1, self.grid[10][0][1] + self.FlyVoidProgram1), 25)

        super().setBox(White,
                       (self.grid[0][10][0] + self.FlyVoidProgram1, self.grid[0][10][1] + self.FlyVoidProgram1), 510,
                       315, 1)

        super().setBox(White,
                       (self.grid[24][10][0] + self.FlyVoidProgram1, self.grid[24][10][1] + self.FlyVoidProgram1), 510,
                       315, 1)

        super().setBox(White,
                       (self.grid[9][5][0] + 7 + self.FlyVoidProgram0, self.grid[9][5][1] + 10 + self.FlyVoidProgram0),
                       45, 40, 1)

        super().setBox(White, (
            self.grid[30][5][0] + 4 + self.FlyVoidProgram0, self.grid[30][5][1] + 10 + self.FlyVoidProgram0), 45, 40, 1)

        super().setText_S('プレイヤー1', (self.grid[8][9][0], self.grid[8][9][1]), 25, White)

        super().setText_S('プレイヤー2', (self.grid[29][9][0], self.grid[29][9][1]), 25, White)

        super().setText_S('  プレイヤー1',
                          (self.grid[0][10][0] + self.FlyVoidProgram1, self.grid[0][10][1] + self.FlyVoidProgram1), 25,
                          White)

        super().setText_S('  プレイヤー2',
                          (self.grid[24][10][0] + self.FlyVoidProgram1, self.grid[24][10][1] + self.FlyVoidProgram1),
                          25, White)

        super().setText_S('→', (
            self.grid[self.Winner_WidthPosi[0]][self.Winner_HeightPosi[0]][0] + self.FlyVoidProgram1,
            self.grid[self.Winner_WidthPosi[0]][self.Winner_HeightPosi[0]][1] + self.FlyVoidProgram1), 25,
                          White)

        super().setText_S('Battle画面 バトルをやめる_Qキーを押す', self.grid[0][0], 15, White)

    # 現在の工程が何番目なのかを判別するメソッド
    def CurrentProgramjudge(self):
        if self.CurrentProgram == 0:
            self.FlyVoidProgram0 = 0
            self.FlyVoidProgram1 = MAX_GRIDPOSI

        elif self.CurrentProgram == 1:
            self.FlyVoidProgram1 = 0
            self.FlyVoidProgram0 = MAX_GRIDPOSI

    # 特に使用することはなかった。
    def variable_init(self):
        pass
