# --- 成果物: お買い物アプリ (辞書活用版) ---

# 1. 商品データ (辞書)
items = {"リンゴ": 100, "バナナ": 200, "ミカン": 400}

# 2. 所持金の入力
money = int(input("所持金を入力してください："))

print("--- 商品リスト ---")
# 辞書から商品名と価格を取り出して表示
for item_name in items:
    print(f"{item_name}は{items[item_name]}円です")

print("----------------")

# 3. 購入する商品を選択
buy_item = input("購入する商品名を入力してください：")

# 4. 判定ロジック
# 辞書の中にそのキー(商品名)があるかチェック
if buy_item in items:
    price = items[buy_item]
    
    if money >= price:
        print(f"{buy_item}を購入しました")
        print(f"残金は{money - price}円です")
    else:
        print("お金が足りません")
else:
    print("その商品は販売していません")