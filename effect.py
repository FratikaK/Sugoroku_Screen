import pygame
import Screen_abc as SC

group = pygame.sprite.Group()


def add_effect(instance):
    """
    effectを追加する
    instanceにはpygame.sprite.Spriteを継承しているクラスのインスタンスを入れてください。
    """
    group.add(instance)


class SquareEffect(pygame.sprite.Sprite):
    BLUE = "blue"
    RED = "red"
    color_names = [BLUE, RED]

    def __init__(self, x_location, y_location, color_name: str = "blue"):
        """
        マスに止まった時に表示するエフェクト

        :param x_location: 整数のx座標
        :param y_location: 整数のy座標
        :param color_name: 色の名前　SquareEffect.REDやSquareEffect.BLUEのように指定してください
        """
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.effect_images = list()
        if SquareEffect.color_names.__contains__(color_name):
            self.color_name = color_name
        else:
            self.color_name = "blue"
        for i in range(1, 14):
            self.effect_images.append(
                pygame.image.load("img/effect/square/square_effect_" + self.color_name + "_" + str(i) + ".png"))
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


class ScreenChangeEffect(pygame.sprite.Sprite):
    SLIDE = "slide"
    MOSAIC = "mosaic"

    def __init__(self, next_screen_id: int, screen_format: str = SLIDE):
        """
        画面遷移を行う時に表示するエフェクト

        ScreenNumを直接編集せずに画面切り替えが可能

        :param next_screen_id: 次に表示したい画面のid
        :param screen_format: 画面切り替え方式 ScreenChangeEffect.SLIDEや、ScreenChangeEffect.MOSAICのように指定してください
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen_format = screen_format
        self.index = 0
        self.next_screen_id = next_screen_id
        self.wait_time = 10
        if screen_format == ScreenChangeEffect.MOSAIC:
            self.images = list()
            for i in range(1, 12):
                self.images.append(pygame.image.load("img/screen_change/mosaic/screen_change_mosaic" + str(i) + ".png"))
            self.limit = len(self.images) - 1
            self.is_changed = False
            self.image = self.images[self.index]
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load("img/screen_change/screen_change.png")
            self.rect = self.image.get_rect()
            self.rect.x = 1280
            self.rect.y = 0

    def update(self):
        # MOSAIC形式処理
        if self.screen_format == ScreenChangeEffect.MOSAIC:
            if not self.is_changed:
                if self.index > self.limit:
                    self.is_changed = True
                    self.index = self.limit
                    SC.ScreenNum = self.next_screen_id
                    return
                self.image = self.images[self.index]
                self.index += 1
            elif self.is_changed:
                if self.wait_time < 0:
                    if self.index < 1:
                        self.kill()
                        return
                    self.image = self.images[self.index]
                    self.index -= 1
                else:
                    self.wait_time -= 1

        else:  # SLIDE処理
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
                if SC.ScreenNum != self.next_screen_id:
                    SC.ScreenNum = self.next_screen_id
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
                    self.remove(group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class CoinNumFontEffect(pygame.sprite.Sprite):
    def __init__(self, num: int, x_location, y_location):
        """
        コインが増減する時に出現させるエフェクト

        :param num: 表示する数字
        :param x_location: 整数のx座標
        :param y_location: 整数のy座標
        """
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
                self.remove(group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class ScreenLineFontEffect(pygame.sprite.Sprite):
    def __init__(self, message: str, color=(255, 255, 255)):
        """
        文字を右から左へ移動させるアニメーション

        :param message: 表示したい文字
        :param color: 色　Screen_abcのstaticカラー指定可能
        """
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
            self.remove(group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
