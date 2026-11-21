from tiny_shop.cart import Cart


def test_add_and_total():
    cart = Cart()
    cart.add("apple", 2.0, 3)
    cart.add("pear", 1.5)
    assert cart.total() == 7.5


def test_receipt_title():
    cart = Cart()
    assert cart.receipt_title() == "Your receipt"


def test_add_same_item_twice_adds_quantity():
    cart = Cart()
    cart.add("apple", 2.0)
    cart.add("apple", 2.0, 2)
    assert cart.items["apple"] == (2.0, 3)
