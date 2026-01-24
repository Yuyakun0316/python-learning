# 別ファイルからクラスを読み込む
from menu_item import MenuItem

# 1. メニュー（インスタンス）の生成
menu_item1 = MenuItem("サンドイッチ", 500)
menu_item2 = MenuItem("チョコケーキ", 400)
menu_item3 = MenuItem("コーヒー", 300)
menu_item4 = MenuItem("オレンジジュース", 200)

# 2. リストにまとめる
menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# 3. メニュー一覧を表示
index = 0
print("--- メニュー ---")
for item in menu_items:
    print(f"{index}: {item.info()}")
    index += 1

print("----------------")

# 4. 注文の入力を受け取る
order = int(input("メニューの番号を入力してください: "))

# 5. 選択されたメニューを取得
selected_menu = menu_items[order]
print(f"選択されたメニュー: {selected_menu.name}")

# 6. 個数の入力を受け取る
count = int(input("何個買いますか？(3個以上で割引): "))

# 7. 計算結果の表示
result = selected_menu.get_total_price(count)
print(f"お会計は {result}円 です")