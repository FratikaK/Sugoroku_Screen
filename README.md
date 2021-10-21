# Sugoroku_Screen

### エフェクト表示のやり方  
```python
import Screen_abc as SC

# 基本
SC.effect_group.add(SC.エフェクトクラス)

# 画面切り替え
SC.effect_group.add(SC.ScreenChangeEffect(切り替えたい画面ID,表示形式))
#表示形式は SC.ScreenChangeEffect.SLIDEまたはSC.ScreenChangeEffect.MOSAICで指定してください

# マスに止まる時に表示するエフェクト
SC.effect_group.add(SC.SquareEffect(x座標,y座標,カラー))
# カラーはSC.SquareEffect.BLUEやSC.SquareEffect.REDの形式で指定してください

# コイン獲得時に表示する数字のエフェクト
SC.effect_group.add(SC.CoinNumFontEffect(整数,x座標,y座標)) 
# 数字が0未満なら赤、0以上なら青色で表示されます

# 文字が右から左へ移動するエフェクト
SC.effect_group.add(SC.ScreenLineFontEffect("表示したい文字",カラー（デフォルト白）))
# カラーはScreen_abcのカラー変数を指定してください 　例 SC.WHITE SC.BLUE

```
