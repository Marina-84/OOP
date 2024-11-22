from src.products import Product


def test_mixin_product(capsys):
    Product("Samsung", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
