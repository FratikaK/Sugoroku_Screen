import pygame
import Screen_abc as SC

# RPG版の背景画像
from Sugoroku_Screen.MassEnum import MassEnum

rpg_opening = pygame.image.load("img/mapimg/background/RPG＿序盤.png")
rpg_opening_object = pygame.image.load("img/mapimg/background/RPG_序盤(物件あり).png")
rpg_middle = pygame.image.load("img/mapimg/background/RPG_中盤.png")
rpg_middle_object = pygame.image.load("img/mapimg/background/RPG_中盤_建物あり.png")
rpg_final = pygame.image.load("img/mapimg/background/RPG_終盤.png")
rpg_final_object = pygame.image.load("img/mapimg/background/RPG物件あり（終盤）.png")

# 無人島の背景画像
island_opening = pygame.image.load("img/mapimg/background/無人島(序盤1).png")
island_opening_object = pygame.image.load("img/mapimg/background/無人島(序盤1)_物件あり.png")
island_middle = pygame.image.load("img/mapimg/background/無人島_中盤（物件なし）.png")
island_middle_object = pygame.image.load("img/mapimg/background/無人島_中盤（物件あり）.png")
island_final = pygame.image.load("img/mapimg/background/無人島_終盤.png")
island_final_object = pygame.image.load("img/mapimg/background/無人島_終盤_物件あり.png")

# マス画像のロード
mass_blue = pygame.image.load("img/mapimg/mass/blue.png")
mass_green = pygame.image.load("img/mapimg/mass/green.png")
mass_purple = pygame.image.load("img/mapimg/mass/purple.png")
mass_red = pygame.image.load("img/mapimg/mass/red.png")
mass_reinbo = pygame.image.load("img/mapimg/mass/reinbo-.png")
mass_yellow = pygame.image.load("img/mapimg/mass/yellow.png")

# 物件画像のロード
rpg_hause = pygame.image.load("img/mapimg/object/hausu.png")


class Map:
    def __init__(self):
        self.map_img = [[rpg_opening, rpg_opening_object, island_opening, island_opening_object],
                        [rpg_middle, rpg_middle_object, island_middle, island_middle_object],
                        [rpg_final, rpg_final_object, island_final, island_final_object]
                        ]
        self.map_Posi = [(256, 160), (320, 160), (384, 160), (448, 160), (512, 160), (576, 160), (640, 160), (704, 160),
                         (768, 160), (832, 160), (896, 160), (960, 160),
                         # 上ライン
                         (960, 224), (960, 288), (960, 352), (960, 416),  # 右ライン
                         (896, 416), (832, 416), (768, 416), (704, 416), (640, 416), (576, 416), (512, 416), (448, 416),
                         (384, 416), (320, 416), (256, 416),
                         # 下ライン
                         (256, 352), (256, 288), (256, 224)]  # ソースコードの整理　CTRL＋ALT＋L ボタンを押す
        self.map_Mass_enum = [MassEnum.AddCoin.value,MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.Building.value, MassEnum.Building.value, MassEnum.Building.value, MassEnum.AddCoin.value, MassEnum.Building.value, MassEnum.Building.value, MassEnum.Building.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value, MassEnum.AddCoin.value]
        self.mass_img = [mass_blue, mass_red, mass_yellow, mass_reinbo, mass_purple]
        self.building = []

    def init(self):
        pass

    def set_mappring_on_screen(self):
        count = 0
        SC.screen.blit(rpg_opening, (0, 0))  # 仮
        building_mass_posi = [(896, 128), (960, 128), (992, 224), (992, 352), (992, 416), (896, 448)]
        for i in self.map_Posi:
            SC.screen.blit(self.mass_img[self.map_Mass_enum[count-1]], i)
            count += 1
            if (count >= 30):
                break
        for i in building_mass_posi:
            SC.screen.blit(rpg_hause, i)

    def getBuildingfo(self):
        pass
