from food import Food
from menu_item import MenuItem

# 1. 親クラスのインスタンス（普通のメニュー）
menu1 = MenuItem("コーヒー", 300)
print(menu1.info())

# 2. 子クラスのインスタンス（食べ物）
# 引数が3つ（名前, 値段, カロリー）になっていることを確認
food1 = Food("ハンバーガー", 500, 800)

# オーバーライドされた info メソッドを確認
print(food1.info()) 
# -> ハンバーガー: ¥500 (800kcal) と表示されれば成功！

# 親クラスから継承したメソッドも使えるか確認
print(f"合計金額: {food1.get_total_price(4)}円")