from piece import Piece


class PieceManager:
    """
    PieceManagementをシングルトンで実装するためのクラス。
    実際にインスタンスを使う場合、PieceManagement.get_instance()で取得する
    PieceManagerは使用しないこと。
    """

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        # PlayerとNPCのインスタンスを、GlobalCondition.UserNumおよび、
        # GlobalCondition.NPCNUM変数に応じた数だけ、ダイスを振る順番に格納。
        self.players: list[Piece] = []

        # GlobalCondition.EventPlayer変数を参照コピー
        # 次のイベントに参加するプレイヤー (Pieceインスタンス) のIDを格納
        self.event_players: list[int] = []

        # イベント参加プレイヤーから徴収したコインを格納
        self.collect_coin: int = 0

        # Pieceのグラフィックが移動する可能性のあるMassインスタンスの位置情報が、
        # サイコロで進む順に格納されたタプル
        # Map.mapPosi[]と同じ内容になるので、変更の可能性アリ。
        self.mass_location: list[tuple[int, int]] = []

    def move_piece(self, piece_id: int, position: int, move_animation: int = 1):
        """
        引数で受けとったpiece.IDのインスタンスのposition変数を、
        引数で受け取った数値(int)に対応するmassLocation変数(タプル)に書き換える。

        :param piece_id: Pieceのid
        :param position: 移動させるマスの番号
        :param move_animation: マス移動アニメーション(デフォルトで1マスずつ)
        :return: なし
        """
        # TODO 駒を1マス毎に進めるアニメーション
        piece = self.players[piece_id]
        piece.set_posi(self.mass_location[position])

    def encount_event(self):
        pass

    def collect_coin(self):
        """
        event_playersに格納されたプレイヤーから、
        ゲーム進行（序盤10%、中盤20%、終盤40%）に応じてコインを徴収。
        合計をcollect_coin変数に格納

        :return: なし
        """
        collection_rate = 0.1
        # game_condition = GlobalCondition.gameCondition
        # if game_condition == 1:
        #     collection_rate = 0.1
        # elif game_condition == 2:
        #     collection_rate = 0.2
        # elif game_condition == 3:
        #     collection_rate = 0.3
        for player_id in self.event_players:
            player = self.players[player_id]
            collect = int(player.coin * collection_rate)
            player.change_coin(-collect)
            self.collect_coin += collect

    def add_coin(self, piece_id: int):
        """
        引数で受けとったpiece.IDのインスタンスに変数collect_coinだけコインを付与する。
        その後、変数collect_coinとevent_playersを初期化

        :param piece_id: Pieceのid
        :return: なし
        """
        piece = self.players[piece_id]
        piece.change_coin(self.collect_coin)
        self.collect_coin = 0
        self.event_players.clear()

    def get_piece_info(self, piece_id):
        """
        引数で渡されたIDのPieceインスタンスが所持する
        変数coin(int), item(str), 所有物件(str) をdictionary型で返す。

        :param piece_id: Pieceのid
        :return: 辞書型配列
        """
        piece = self.players[piece_id]
        building = []
        for building_id in piece.building:
            # TODO building.append(building.name)
            building.append(building_id)
        return {
            "coin": piece.coin,
            "item": piece.item,
            "building": piece.building
        }

    def rob_item(self, piece_id: int, target_piece_id: int, item_id: int):
        """
        引数で渡された、奪う(ID)に引数のitemIDのitemを付与。
        奪われるPlayer(ID)の所有itemからitemを削除

        :param piece_id: アイテムを取得するプレイヤーid
        :param target_piece_id: アイテムを奪われるプレイヤーid
        :param item_id: アイテムを奪われるプレイヤーのitemのid
        :return: なし
        """
        piece = self.players[piece_id]
        target_piece = self.players[target_piece_id]
        target_item = target_piece.item[item_id]
        piece.add_item(target_item)
        target_piece.remove_item(target_item)

    # def item_effect_sample(self):
    #     """
    #     アイテムのエフェクトを出す
    #     :return:
    #     """
    #     pass

    # # 使用用途はないので実装せず
    # def sort_order(self, player_ids: list[int]):
    #     pass


# シングルトン
class PieceManagement(PieceManager):
    """
    Piece型のインスタンスを管理するクラス。
    Piece型インスタンスが持つ変数はこのクラスを介して変更する。
    シングルトン。
    """

    def __init__(self):
        super().__init__()
