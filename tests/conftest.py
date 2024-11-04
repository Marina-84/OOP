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

