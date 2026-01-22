# --- Pythonの基礎: 関数 (Function) ---

# 1. 関数の定義
# Ruby: def hello ... end
# Python: def hello(): (コロンが必要！)
def hello():
    print("Hello World")

# 2. 引数と初期値
# Ruby: def greet(name = "Guest")
# Python: 同じ！
def greet(name="Guest"):
    print(f"こんにちは、{name}さん")

# 3. 戻り値 (Return)
# ★重要: Pythonは「return」を書かないと値が返らない（Noneになる）
# Rubyは最後の行が自動で返るが、Pythonは明示が必要。
def add(a, b):
    return a + b

# --- 実行 ---
hello()
greet("Yuyakun")
greet() # 初期値が使われる

result = add(10, 20)
print(f"合計: {result}")