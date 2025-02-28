"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        # Проверяем, что можно купить, если количество в наличии
        assert product.check_quantity(1) is True
        assert product.check_quantity(500) is True
        assert product.check_quantity(1000) is True

        # Проверяем, что нельзя купить больше, чем есть
        assert product.check_quantity(1001) is False
        assert product.check_quantity(5000) is False
        pass

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        # Покупаем 100 товаров - количество должно уменьшиться
        product.buy(100)
        assert product.quantity == 900

        # Покупаем оставшиеся 900 - должно стать 0
        product.buy(900)
        assert product.quantity == 0


    def test_product_buy_more_than_available(self, product, excinfo="Недостаточно товара.*превышает доступное.*"):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        """Тест покупки больше, чем есть в наличии (должно вызвать ошибку)"""
        with pytest.raises(ValueError, match=r"Недостаточно товара.*превышает доступное.*"):
            product.buy(2000)  # Пытаемся купить 2000, когда есть только 1000


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
