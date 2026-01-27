# --- ロジック特訓: 購入済みかどうかの判定 (フラグ管理) ---

def has_purchased_item(purchase_history, target_item_id):
    # 1. フラグを「False（まだ見つかっていない）」で初期化
    has_purchased = False
    
    # 2. ループで全データをチェック
    for history in purchase_history:
        # 3. 条件に合致するか判定
        if history["item_id"] == target_item_id:
            # 4. 見つかったらフラグを「True」にして、ループを抜ける（break）
            has_purchased = True
            break # これ以上探す必要がないため
    
    # 5. 結果を返す
    return has_purchased

# --- 実行データ ---
# 過去の購入履歴
history_data = [
    {"user_id": 1, "item_id": 101, "date": "2026-01-20"},
    {"user_id": 1, "item_id": 102, "date": "2026-01-25"},
    {"user_id": 1, "item_id": 105, "date": "2026-01-27"},
]

# チェックしたい商品ID
target_id = 102

# 判定実行
if has_purchased_item(history_data, target_id):
    print(f"商品ID {target_id} は購入済みです。")
else:
    print(f"商品ID {target_id} はまだ購入していません。")