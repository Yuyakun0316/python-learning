# --- 応用課題: 条件分岐とループを組み合わせた集計 ---

def calculate_total_price(cart_items):
    total_price = 0
    
    for item in cart_items:
        # 商品の種類によって計算ルールを変える
        if item['type'] == 'food':
            # 食料品は10%引き (0.9倍)
            discount_price = round(item['price'] * 0.9)
            total_price += discount_price
            
        elif item['type'] == 'clothes':
            # 服は1000円引き
            discount_price = item['price'] - 1000
            total_price += discount_price
            
        else:
            # それ以外は定価
            total_price += item['price']
            
    return total_price

# --- 実行データ ---
cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000},
    {'name': 'シューズ', 'type': 'shoes', 'price': 15000},
    {'name': 'ドリンク', 'type': 'food', 'price': 150}
]

# 計算実行
result = calculate_total_price(cart_items)
print(f"合計金額: {result}円")