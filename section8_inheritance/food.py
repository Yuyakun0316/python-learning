# 親クラスを読み込む
from menu_item import MenuItem

# 継承の書き方
# Ruby: class Food < MenuItem
# Python: class Food(MenuItem):  <-- カッコの中に親クラスを書く！
class Food(MenuItem):
    
    # __init__ のオーバーライド
    # カロリー(calorie)という新しい引数を追加したい
    def __init__(self, name, price, calorie):
        # super() を使って親クラスの __init__ を呼び出す（名前と値段のセットは親に任せる）
        # Ruby: super(name, price)
        # Python: super().__init__(name, price) <-- メソッド名まで書く！
        super().__init__(name, price)
        self.calorie = calorie
    
    # info メソッドのオーバーライド
    def info(self):
        # 親クラスの info() の戻り値を受け取って、カロリー情報を付け足す
        return f"{super().info()} ({self.calorie}kcal)"
    
    # 独自のメソッド
    def calorie_info(self):
        print(f"{self.name}は{self.calorie}kcalです")