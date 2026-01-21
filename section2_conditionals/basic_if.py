# --- Pythonの基礎: 条件分岐と真偽値 ---

# 1. 真偽値 (Boolean)
# Ruby: true / false (小文字)
# Python: True / False (★先頭が大文字！)
is_hungry = True

if is_hungry:
    print("腹ペコです") # インデントがブロックの代わりになる

# 2. 比較演算子 (Rubyと同じ)
score = 80
print(score > 70) # True
print(score == 80) # True

# 3. 論理演算子
# Ruby: &&, ||, !
# Python: and, or, not (英語そのまま)
time = 10
is_sunny = True

if time < 12 and is_sunny:
    print("午前中で、かつ晴れです")

if not is_hungry:
    print("お腹はいっぱいです")

# 4. if - elif - else
# Ruby: elsif (sがない)
# Python: elif (else ifの略)
money = 500

if money >= 1000:
    print("豪華なランチ")
elif money >= 500:
    print("普通のランチ")
else:
    print("節約ランチ")