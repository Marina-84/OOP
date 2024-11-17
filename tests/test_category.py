from src.category import Category


def test_category_init(second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор, который станет вашим другом"
    assert second_category.products_list == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]
    assert Category.category_count == 1
    assert len(second_category.products_list) == 1
    assert Category.product_count == 1


def test_empty_list(category3):
    assert category3.products_list == []
    assert category3.name == "Ноутбуки"
    assert category3.description == "Современный ноутбук по доступной цене"


def test_category_products_property(category_property):
    assert category_property.products == (
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n" "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
