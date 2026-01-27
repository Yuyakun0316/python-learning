# --- ロジック特訓: 対象商品の在庫更新 ---

def update_stock(products, target_id, count):
    for product in products:
        if product["id"] == target_id:
            # 在庫を減らす
            product["stock"] -= count
            print(f"{product['name']} の在庫を {count} 個減らしました。")
            print(f"残り在庫: {product['stock']}")
            return # 見つけて処理したら終了
            
    print("対象の商品が見つかりませんでした。")

# --- 実行データ ---
products_data = [
    {"id": 1, "name": "Tシャツ", "stock": 10},
    {"id": 2, "name": "スニーカー", "stock": 5},
]

# ID: 2 の商品を 3個 購入処理
update_stock(products_data, 2, 3)