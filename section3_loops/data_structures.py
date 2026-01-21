# --- Pythonの基礎: リスト(配列)・辞書(ハッシュ)・ループ ---

# 1. リスト (Ruby: Array)
# 定義
fruits = ["Apple", "Banana", "Orange"]

# 要素の取得 (インデックスは0から)
print(fruits[0])

# 追加 (Ruby: push または <<)
fruits.append("Grape")

# 更新
fruits[0] = "Cherry"
print(fruits)

# 2. for文 (Ruby: each)
# 構文: for 変数 in リスト:
print("--- リストのループ ---")
for fruit in fruits:
    print(f"好きな果物は{fruit}です")

# 3. 辞書 (Ruby: Hash)
# キーは「文字列」にするのが一般的 (Rubyのシンボル :key はPythonにはない)
# 定義: { キー: 値 }
scores = {"Math": 90, "English": 80}

# 要素の取得 (キーを指定)
print(scores["Math"])

# 追加・更新
scores["Science"] = 100 # 新しいキーなら追加
scores["Math"] = 95     # 既存キーなら更新

# 4. 辞書のループ
print("--- 辞書のループ ---")
# 辞書をforで回すと「キー」が取れる
for subject in scores:
    value = scores[subject]
    print(f"{subject}の点数は{value}点です")

# 5. while文とbreak/continue
print("--- while文 ---")
x = 1
while x <= 5:
    if x == 3:
        x += 1
        continue # 次のループへスキップ
    
    print(f"カウント: {x}")
    x += 1