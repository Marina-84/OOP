class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
        self.name = name
        self.description = description
        self.products = products


if __name__ == "__main__":
    category1 = Category(
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

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом",
        [{"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}],
    )

    #category3 = Category("Ноутбуки", "Современный ноутбук по доступной цене", [])


    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category2.name)
    print(category2.description)
    print(category2.products)
    #print(category3.name)
    #print(category3.description)
    #print(category3.products)
    print(category2.category_count)
    print(Category.product_count)
