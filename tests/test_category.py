from src.category import Category


def test_category_init(second_category):
    assert second_category.name == "Телевизоры"
    assert second_category.description == "Современный телевизор, который станет вашим другом"
    assert second_category.products == [
        {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    ]


def test_category_count(first_category, second_category):
    assert Category.category_count == 2
    assert first_category.category_count == 2
    assert second_category.category_count == 2


def test_product_count(first_category, second_category):
    assert Category.product_count == 4
    assert first_category.product_count == 4
    assert second_category.product_count == 4
