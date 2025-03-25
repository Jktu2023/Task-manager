# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class Store:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = dict()

    def add_item(self, product, price):
        self.items[product] = price  # Добавляем пару товар: цена в словарь
        print(f'Добавлен товар: {product}, цена: {price} руб.')

    def del_item(self, product):
        if product in self.items:
            del self.items[product] # удаляем товар из словаря
            print(f'Удален товар: {product}')
        else:
            print(f'Такого товара нет: {product}')
            return None

    def get_price(self, product): # `None` если нет
        if product in self.items:
            print(f'Цена на {product}: {self.items[product]} рублей.')
        else:
            print(f'Такого товара нет: {product}')
            return None

    def set_price(self, product, price):
        if product in self.items:
            old = self.items[product]
            self.items[product] = price
            print(f'Цена на {product} изменена с {old} на {self.items[product]} руб.')
        else:
            print(f'Такого товара нет: {product}')
            return None

    def info(self, ):
        print('\n                 ***')
        print(f'Общая информация о магазине: {self.name}')
        print(f'Адрес: {self.adress}')
        print(f'Ассортимент: {self.items}')



Meloch_1000 = Store('1000 Мелочей', 'Ленина 55')
Meloch_1000.add_item('Pepsi',98)
Meloch_1000.add_item('Fanta',95)
Meloch_1000.add_item('7-Up',90)
Meloch_1000.del_item('Pepsi')
Meloch_1000.get_price('Fanta')
Meloch_1000.set_price('7-Up', 92)
Meloch_1000.info()

