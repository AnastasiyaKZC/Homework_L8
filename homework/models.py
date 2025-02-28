class Product: #описание класса, свойства
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity): #создание экземпляра
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if not self.check_quantity(quantity):
            raise ValueError(
                f"Недостаточно товара: запрашиваемое количество {quantity} превышает доступное {self.quantity}.")

        self.quantity -= quantity  # Уменьшаем количество на запрашиваемое

        print(f"Покупка {quantity} единиц товара '{self.name}' завершена.")

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}  # Словарь {Продукт: Количество}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:
            if remove_count is None or remove_count >= self.products[product]:
                del self.products[product]  # Полностью удалить продукт
            else:
                self.products[product] -= remove_count  # Уменьшить количество

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        return sum(product.price * quantity for product, quantity in self.products.items())

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                raise ValueError(
                    f"Товара '{product.name}' недостаточно на складе! Запрашиваемое: {quantity}, доступно: {product.quantity}."
                )
            # После проверки уменьшаем количество товаров
        for product, quantity in self.products.items():
            product.quantity -= quantity  # Вычитаем купленное количество

            # Очищаем корзину после успешной покупки
        self.products.clear()

