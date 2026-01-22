# utils.py (モジュール)

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name):
    hands = ["グー", "チョキ", "パー"]
    print(name + "は" + hands[hand] + "を出しました")

def judge(player, computer):
    # 0:グー, 1:チョキ, 2:パー
    # 引き分け: 0 vs 0, ...
    # 勝ち: 0 vs 1, 1 vs 2, 2 vs 0
    # 負け: それ以外
    
    if player == computer:
        return "引き分け"
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        return "勝ち"
    else:
        return "負け"