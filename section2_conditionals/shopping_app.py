# --- 成果物: お買い物アプリ ---

# 商品データ
apple_price = 200
money = 1000

# 1. 入力を受け取る (Ruby: gets.chomp)
# input()を使うと、ユーザーの入力を待つ状態になる
# 注意: inputで受け取った値はすべて「文字列 (str)」になる
count_str = input("リンゴを何個買いますか？：")

# 2. 型変換 (String -> Integer)
# 計算するために整数に変換する
count = int(count_str)

# 3. 合計金額の計算
total_price = apple_price * count

print(f"購入数: {count}個")
print(f"合計金額: {total_price}円")

# 4. 購入判定
if money >= total_price:
    print("購入できます")
    print(f"残金: {money - total_price}円")
else:
    print("お金が足りません")
    print(f"不足額: {total_price - money}円")