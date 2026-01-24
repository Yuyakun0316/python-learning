# --- 復習: ロジック構築の練習 ---

# 1. 2重ループ (総当たり)
# 商品と色の組み合わせを全て出力する
# 実務では「在庫データの生成」などでよく使うパターン
items = ["Tシャツ", "スニーカー"]
colors = ["白", "黒", "赤"]

print("--- 商品バリエーション ---")
for item in items:
    for color in colors:
        print(f"{item} : {color}")


# 2. 条件付き集計 (if + for)
# 特定の条件（プレミアム会員など）に合わせて計算を変える
# 実務では「キャンペーン適用価格の計算」などで使うパターン
orders = [
    {"price": 1000, "is_campaign": True},
    {"price": 2000, "is_campaign": False},
    {"price": 3000, "is_campaign": True},
]

total_price = 0

print("\n--- 売上集計 ---")
for order in orders:
    if order["is_campaign"]:
        # キャンペーン対象なら10%引き
        price = order["price"] * 0.9
        print(f"割引適用: {int(price)}円")
        total_price += price
    else:
        # 対象外なら定価
        print(f"定価: {order['price']}円")
        total_price += order["price"]

print(f"最終合計: {int(total_price)}円")