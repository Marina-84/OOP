import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


@pytest.fixture
def product1():
    return Product("Samsung", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category():
    return Category(
        "Телевизоры",
        "Современный телевизор, который станет вашим другом",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )


@pytest.fixture
def category2():
    return Category(
        "Смартфоны",
        "Категория смартфонов",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
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
def smartphone():
    return Smartphone.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
            "efficiency": "3.4 Ггц",
            "model": "Galaxy C23 Ultra",
            "memory": "256Gb",
            "color": "Серый",
        }
    )


@pytest.fixture
def lawngrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def new_product():
    return Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture()
def product_invalid():
    return Product("Бракованный товар", "Неверное количество", 1000.0, 0)
