class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return f"{self.name}: ¥{self.price}"

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price -= 100
        return total_price