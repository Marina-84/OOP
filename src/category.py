from src.products import Product


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
        self.__products = products

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: dict):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Нельзя добавлять разные классы")

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @products.setter
    def products(self, new_product):
        self.__products = new_product

    @property
    def products_list(self):
        return self.__products

    def middle_price(self):
        try:
            summary = sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
        return summary
