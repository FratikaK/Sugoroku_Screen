#テキストを一文字ずつ表示するためのクラス。
#このクラスをインポートし、One_letterにString配列を指定すると、
#画面の更新一回ごとに一文字ずつ文字がスライスされて返される
#現在はScreen_abcのsetText_S,M,Lにのみ対応しているものと考える

class TextSlice:

    def __init__(self):
        
        self.Slice_Number = 0

        self.StringList_Object = ''

    def One_letter(self, StringList):

        #引数がストリングを要素としたリストかどうかを判別、違った場合はExceptionをスローする
        if type(StringList) == list:

            if type(StringList[0]) == str:

                pass
            
            else:

                raise Exception
        
        else:

            raise Exception

        StringList_tmp = ','.join(StringList)

        if self.StringList_Object != StringList_tmp:

            self.StringList_Object = StringList_tmp

            self.Slice_Number = 0
        
        Retrun_StringList = self.StringList_Object[0 : self.Slice_Number].split(',')

        if self.Slice_Number < len(self.StringList_Object):

            self.Slice_Number = self.Slice_Number + 1

        return Retrun_StringList