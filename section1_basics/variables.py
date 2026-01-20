# --- Pythonの基礎: 変数とデータ型 ---

# 1. 出力 (Ruby: puts)
# print関数を使う。文字列はシングル(')でもダブル(")でもOK。
print("Hello Python")

# 2. 変数 (Rubyと同じで型宣言不要)
name = "Yuyakun"
age = 26

# 3. 文字列の連結
# Ruby: "名前は #{name}"
# Python: f"名前は {name}" (f文字列と言います。これが一番モダンで便利)
print(f"私の名前は{name}です。")

# 従来の連結方法（型変換が必要）
# Ruby: name + age.to_s
# Python: name + str(age)  (str関数で文字列に変換する)
print("年齢は" + str(age) + "歳です。")

# 4. 数値の計算
# Rubyとほぼ同じ
print(10 + 5)  # 足し算
print(10 / 2)  # 割り算（結果は 5.0 という小数になるのがPythonの特徴）
print(10 // 2) # 切り捨て割り算（結果は 5 という整数になる）

# 5. 変数の更新とデータ型
number = 100
print(type(number)) # <class 'int'> (整数型)

number = 100.5
print(type(number)) # <class 'float'> (浮動小数点数型)