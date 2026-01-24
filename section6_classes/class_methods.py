# --- Pythonの基礎: クラスのメソッドと初期化 ---

class MenuItem:
    # 1. 初期化メソッド (Ruby: initialize)
    # インスタンス生成時に自動で呼ばれる
    # ★重要: Pythonのメソッドは、第1引数に必ず「self（自分自身）」を受け取るルールがある！
    def __init__(self, name, price):
        # Ruby: @name = name
        # Python: self.name = name (自分自身のname変数に代入)
        self.name = name
        self.price = price

    # 2. インスタンスメソッド
    # ここでも必ず (self) が必要！
    def info(self):
        # Ruby: return "#{@name}: #{@price}円"
        # Python: self.name でインスタンス変数にアクセスする
        return f"{self.name}: {self.price}円"

    # 3. 引数のあるメソッド
    # self の後ろに引数を書く
    def get_total_price(self, count):
        total = self.price * count
        
        # 割引ロジック（3個以上で100円引き）
        if count >= 3:
            total -= 100
            
        return total

# --- 実行 ---

# インスタンス生成（__init__が動く）
# selfは自動で渡されるので、引数は name と price だけでOK
menu1 = MenuItem("サンドイッチ", 500)
menu2 = MenuItem("コーヒー", 300)

# メソッド呼び出し
print(menu1.info()) # -> サンドイッチ: 500円

# 計算メソッド呼び出し
count = 4
result = menu1.get_total_price(count)
print(f"{menu1.name}を{count}個買うと: {result}円")