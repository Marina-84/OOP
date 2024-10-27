import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture
def third_product():
    return Product(
        name="55 QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7
    )


@pytest.fixture
def fourth_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=32000.0,
        quantity=14,
    )


@pytest.fixture
def first_category():
    return Category(
        name="Category",
        description="Description of the category",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product number two",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Category number two",
        description="Description of the category number two",
        products=[
            Product(
                name="Product",
                description="Description of the product",
                price=84.50,
                quantity=10,
            ),
            Product(
                name="Product number two",
                description="Description of the product number two",
                price=155.87,
                quantity=34,
            ),
            Product(
                name="Product three",
                description="Description of the product three",
                price=8467.56,
                quantity=32,
            ),
        ],
    )


@pytest.fixture
def product_dict():
    return {
        "name": "Product 4",
        "description": "Description of the product 4",
        "price": 145.75,
        "quantity": 23,
    }
