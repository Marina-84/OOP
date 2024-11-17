from src.products import Product


def test_product_init(product):
    assert product.name == "Samsung"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product():
    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 200MP камера"
    new_product.price = 180000.0
    new_product.quantity = 5


def test_price_setter(capsys):
    new_product = Product.new_product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    new_product.price = 99999
    assert new_product.price == 99999
    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert new_product.price == 99999
    new_product.price = 100
    assert new_product.price == 100
