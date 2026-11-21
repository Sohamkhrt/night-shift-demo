"""A tiny shopping cart used to demo Night Shift."""


class Cart:
    def __init__(self):
        self.items = {}  # name -> (price, quantity)

    def add(self, name, price, quantity=1):
        if name in self.items:
            old_price, old_qty = self.items[name]
            self.items[name] = (old_price, old_qty + quantity)
        else:
            self.items[name] = (price, quantity)

    def total(self):
        return sum(price * qty for price, qty in self.items.values())

    def receipt_title(self):
        return "Your receipt"
