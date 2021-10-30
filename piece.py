import random


class Piece:
    """
    各プレイヤーの情報が格納されたPlayer,NPCのスーパークラス
    """

    instance_num = 0
    piece_img = [[], [], [], [], [], [], []]

    def __init__(self):
        # 識別番号
        self.id = Piece.instance_num
        Piece.instance_num += 1
        # プレイヤーの名前
        self.name = 'Player' + str(self.id + 1)
        # プレイヤーの座標
        self.position = (0, 0)
        # プレイヤーを表す画像 4パターン
        self.img = Piece.piece_img[random.randrange(len(Piece.piece_img))]
        Piece.piece_img.remove(self.img)
        # 所持アイテムを格納
        self.item: list[str] = []  # [Item.NAME,Item.NAME,Item.NAME]
        # 所有物件idを格納
        self.building: list[int] = []
        # 所持コイン
        self.coin = 0
        # 周回数
        self.round_count = 0

    def add_item(self, item: str):
        """
        引数で渡されたItem(Enumクラス名)を変数itemに追加。

        :param item: Item.NAME
        :return: アイテムが追加でTrue
        """
        if len(self.item) < 3:
            self.item.append(item)
            return True
        return False

    def remove_item(self, target_item: str):
        """
        対象アイテムを削除する

        :param target_item: Item.NAME
        :return: なし
        """
        self.item.remove(target_item)

    def add_building(self, building_id: int, use_coin: int):
        """
        use_coin分のプレイヤーのコインを減らし、物件idを追加する。
        コインが足りなければ物件idは追加しない

        :param building_id: Buildingのid
        :param use_coin: 減らすコイン数
        :return: self.coin >= use_coin
        """
        flag = False
        if self.coin >= use_coin:
            self.building.append(building_id)
            flag = True
        self.coin -= use_coin
        return flag

    def remove_building(self, target_building_id: int):
        """
        対象の物件idを削除する

        :param target_building_id: 対象の物件id
        :return: なし
        """
        self.building.remove(target_building_id)

    def throw_dice(self, dice: int = random.randrange(1, 7)):
        """
        ダイスを振る。引数diceを指定する場合はその数値を返す。

        :param dice: ダイスの目
        :return: ダイスの目
        """
        return dice

    def change_coin(self, coin: int):
        """
        プレイヤーのコインを増減させる

        :param coin: 増減させるコイン数
        :return: なし
        """
        self.coin += coin
        if self.coin < 0:
            self.coin = 0

    def set_posi(self, position=(0, 0)):
        """
        プレイヤーの座標を設定する

        :param position: 設定したい座標。(int,int)で指定
        :return: なし
        """
        self.position = position


class Player(Piece):
    """
    ユーザーが操作するインスタンス
    """

    def __init__(self):
        super().__init__()


class NPC(Piece):
    """
    NPCが操作するインスタンス
    """

    def __init__(self):
        super().__init__()
