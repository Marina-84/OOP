# Работа с классами (основы OOП)

## Описание:
Использование классов и объектов на основе темы e-commerce

## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/Marina_84/OOP.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Структура проекта:
1. tests/ - папка, в которой содержатся тесты проекта.
2. src/ - папка, содержащая файлы с функциями проекта.
3. data/ - папка, содержащая файлы с данными.

## Использование:
1. category.py. В модуле описан класс Category
class Category:
    """Класс для предоставления категорий товаров"""

    name: str
    description: str
    products: list  # приватный атрибут
    category_count = 0
    product_count = 0
В классе есть приватный атрибут products

2. products.py. В модуле описан класс Product
class Product:
    """Класс для представления товара"""

    name: str
    description: str
    __price: float
    quantity: int
В классе есть приватный атрибут price

Для каждого класса прописан метод __str __ для строкового отображения информации в определённом формате:

<Название продукта>, n руб. Остаток: m шт.
<Название категории>, количество продуктов: n шт.
В классе Product реализована возможность складывать продукты. Итогом сложения является полная стоимость всех товаров на складе.

3. lawn_grass.py. Модуль содержит класс LawnGrass, наследуемый от класса Product
class LawnGrass(Product):
    """Класс для предствления товаров категории 'Трава газонная'"""
    
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str
4. smartphone.py. Модуль содержит класс Smartphone, наследуемый от класса Product
class Smartphone(Product):
    """Класс для предствления товаров категории 'Смартфоны'"""
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
5. utils.py. В модуле реализована функция для чтения данных из JSON-файла и созания на их основе объектов классов

## Документация:
Для получения дополнительной информации обратитесь к документации.

## Лицензия:
Этот проект лицензирован по 
