import pytest
from src.category import Category
from src.products import Product


@pytest.fixture
def product():
    return Product(name="Samsung", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5)


@pytest.fixture
def first_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство получения дополнительных функций для удобства жизни",
        [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который станет вашим другом",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )
