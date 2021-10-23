import Screen_abc as SC
from Screen_Main import ScreenMain
from Screen_encount import ScreenEncount
from Screen_end import ScreenEnd
from Screen_loading import ScreenLoading
from Screen_setting import ScreenSetting
from Screen_start import ScreenStart


class GameManagement:
    def __init__(self):
        self.screen = [ScreenStart(), ScreenSetting(), ScreenLoading(), ScreenMain(), ScreenEncount(), ScreenEnd()]

    def start_game(self):
        while True:
            self.screen[SC.ScreenNum].reflect_display()


if __name__ == '__main__':
    GameManagement().start_game()


    #test2