import pytest
from homework.models import Product, Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        """Тест добавления продукта в корзину"""
        cart.add_product(product, 2)
        assert cart.products[product] == 2
        cart.add_product(product, 3)
        assert cart.products[product] == 5  # Должно увеличиться

    def test_remove_product(self, cart, product):
        """Тест удаления продукта из корзины"""
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products[product] == 3  # Уменьшилось
        cart.remove_product(product, 5)  # Больше, чем есть
        assert product not in cart.products  # Должно полностью удалиться

    def test_clear(self, cart, product):
        """Тест очистки корзины"""
        cart.add_product(product, 3)
        cart.clear()
        assert len(cart.products) == 0  # Корзина должна быть пустой

    def test_get_total_price(self, cart, product):
        """Тест подсчета общей стоимости"""
        cart.add_product(product, 2)
        assert cart.get_total_price() == 200  # 100 * 2

    def test_buy(self, cart, product):
        """Тест покупки товаров"""
        cart.add_product(product, 3)
        cart.buy()
        assert product.quantity == 997  # 1000 - 3
        assert len(cart.products) == 0  # Корзина должна очиститься

    def test_buy_not_enough(self, cart, product):
        """Тест попытки купить больше, чем есть на складе"""
        cart.add_product(product, 2000)
        with pytest.raises(ValueError, match="Товара.*недостаточно на складе!"):
            cart.buy()
