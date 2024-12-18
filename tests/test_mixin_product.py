from src.lawn_grass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


def test_mixin_product(capsys):
    Product("Samsung", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product('Samsung', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass('Газонная трава', 'Элитная трава для газона', 500.0, 20)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8)"
