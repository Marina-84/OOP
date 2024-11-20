import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def product():
    return Product(name="Samsung", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5)


@pytest.fixture
def second_category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который станет вашим другом",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


@pytest.fixture
def category3():
    return Category("Ноутбуки", "Современный ноутбук по доступной цене", [])


@pytest.fixture
def category_property():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для " "удобства жизни",
        [
            Product.new_product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product.new_product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def product1():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
