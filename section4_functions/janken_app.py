# janken_app.py (メイン)

# 1. モジュールの読み込み
import utils
# ランダム機能を使うための標準ライブラリ
import random 

print("--- じゃんけんスタート ---")
print("0:グー, 1:チョキ, 2:パー")

# 2. 入力を受け取る
player_hand = int(input("出す手を入力してください: "))

# 3. バリデーション（正しい数字か？）
if utils.validate(player_hand):
    # コンピュータの手をランダムに決める (0〜2)
    computer_hand = random.randint(0, 2)
    
    # お互いの手を表示 (utilsモジュールを使う)
    utils.print_hand(player_hand, "あなた")
    utils.print_hand(computer_hand, "コンピュータ")
    
    # 勝敗判定
    result = utils.judge(player_hand, computer_hand)
    print("結果は" + result + "です")
else:
    print("正しい数値を入力してください")