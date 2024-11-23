import pytest

from src.products import Product


def test_product_init(product1):
    assert product1.name == "Samsung"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product():
    new_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    new_product.name = "Samsung Galaxy S23 Ultra"
    new_product.description = "256GB, Серый цвет, 200MP камера"
    new_product.price = 180000.0
    new_product.quantity = 5


def test_price_setter(capsys):
    new_product = Product.new_product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    new_product.price = 99999
    assert new_product.price == 99999
    new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    assert new_product.price == 99999
    new_product.price = 100
    assert new_product.price == 100


def test_product_str(product2):
    assert str(product2) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_add_product(product1, product2):
    assert product1 + product2 == 1334000
    with pytest.raises(TypeError):
        product1 + 1


def test_quantity_zero(capsys):
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        message = capsys.readouterr()
        assert message.out.strip().split("\n")[-1] == (
            "Возникла ошибка ValueError"
            "прерывающая работу программы при попытке"
            "добавить продукт с нулевым количеством"
        )
