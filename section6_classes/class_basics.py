# --- Pythonの基礎: クラスとインスタンス ---

# 1. クラスの定義
# Ruby: class MenuItem ... end
# Python: class MenuItem: (コロンが必要！)
# クラス名のルールはRubyと同じ「アッパーキャメルケース（大文字始まり）」
class MenuItem:
    pass  # pass は「何もしない」という意味（中身が空の時に書く）

# 2. インスタンスの生成
# Ruby: menu_item1 = MenuItem.new
# Python: menu_item1 = MenuItem()  (★ new はいらない！)
menu_item1 = MenuItem()

# 3. インスタンス変数への代入
# Pythonは、インスタンスを作った後に変数を追加できる
# Ruby: @name = ... (クラス内で定義が必要)
# Python: インスタンス.変数名 = ...
menu_item1.name = "サンドイッチ"
print(menu_item1.name)

menu_item1.price = 500
print(menu_item1.price)

# 4. 複数のインスタンス
# 設計図（クラス）は1つでも、実体（インスタンス）は別物
menu_item2 = MenuItem()
menu_item2.name = "チョコケーキ"
menu_item2.price = 400

print("--- メニュー一覧 ---")
print(f"{menu_item1.name}: {menu_item1.price}円")
print(f"{menu_item2.name}: {menu_item2.price}円")