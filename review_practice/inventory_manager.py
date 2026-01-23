# --- 復習: 関数・ループ・条件分岐の組み合わせ ---

# 商品データ（辞書のリスト）
products = [
    {"name": "Apple", "price": 100, "stock": 3},
    {"name": "Banana", "price": 50, "stock": 0},
    {"name": "Orange", "price": 80, "stock": 5},
]

# 機能: 在庫がある商品だけを表示する関数
def show_available_products(items):
    print("--- 販売中の商品 ---")
    for item in items:
        # 在庫が0より大きい場合だけ表示（ifとforの組み合わせ）
        if item["stock"] > 0:
            print(f"{item['name']}: {item['price']}円 (残り{item['stock']}個)")

# 機能: 商品を購入して在庫を減らす関数
def buy_product(items, target_name, count):
    for item in items:
        # 名前が一致したら（if）
        if item["name"] == target_name:
            # 在庫が足りるかチェック（ifのネスト）
            if item["stock"] >= count:
                item["stock"] -= count
                print(f"{target_name}を{count}個購入しました！")
                return # 処理終了（これ以上ループする必要がないため）
            else:
                print(f"{target_name}の在庫が足りません...")
                return

    print("その商品は見つかりませんでした。")

# --- 実行 ---
show_available_products(products)

print("\n--- 購入処理 ---")
buy_product(products, "Apple", 2)
buy_product(products, "Banana", 1)

print("\n--- 更新後の在庫 ---")
show_available_products(products)