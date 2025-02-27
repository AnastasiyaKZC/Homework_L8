# Homework_L8

Основы Python. Часть III. Применение ООП в написании автотестов. Сергей Хомутинин

url = https://github.com/qa-guru/knowledge-base/wiki/7.-%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Python.-%D0%A7%D0%B0%D1%81%D1%82%D1%8C-III

ООП — это стиль программирования, в котором основными элементами являются объекты (объект это экземпляр класса. класс - это шаблон для создания объекта). Эти объекты объединяют данные (атрибуты) и методы (функции, работающие с данными).

Три основных принципа объектно-ориентированного программирования (ООП) — это:
1.	Инкапсуляция: Скрывает внутренние данные объекта, чтобы защитить их от прямого доступа (скрытие внутренней реализации объекта от внешнего мира)
2.	Наследование: Позволяет одному классу (дочернему) унаследовать свойства и методы другого класса (родительского).

	class Animal:  # Базовый класс
        def speak(self):
            return "Some sound"

    class Dog(Animal):  # Подкласс
        def speak(self):
            return "Woof"

    class Cat(Animal):  # Подкласс
        def speak(self):
            return "Meow"
3.	Полиморфизм: Разные классы могут иметь одинаковые методы, но с разной реализацией. Полиморфизм позволяет использовать один и тот же интерфейс для разных типов объектов.

Полиморфизм позволяет объектам разных классов обрабатывать одинаковые сообщения (вызовы методов). Это достигается через переопределение методов в наследниках, что позволяет использовать один интерфейс для работы с разными типами объектов. Полиморфизм способствует гибкости и расширяемости программного обеспечения.
Эти принципы помогают создавать более организованный, понятный и поддерживаемый код.


# Модули и классы
Файлы и папки в Python - это модули. 
Модули могут содержать в себе функции, классы, переменные и другие объекты.

# Вопросы для самоконтроля:
- Для чего нужен self?

self — это способ ссылаться на конкретный объект, с которым вы работаете в данный момент.
- Как используется __init__() в классе? 
	
Метод __init__() — это специальный метод, который автоматически вызывается, когда вы создаёте новый объект (экземпляр) класса. Он используется для инициализации (установки начальных значений) атрибутов объекта.
- Что такое @classmethod?
- Что такое @staticmethod?
- Что такое @property?
- Зачем нужны дата-классы?
- Какие типы данных удобно использовать с Enum?
