class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"Создан товар: '{self.name}' - {price} руб.")
    def get_info(self):
        """Получить информацию о товаре"""
        return f"Товар: {self.name}, Цена: {self.price} руб."
class DeliveryPerson:
    def __init__(self, speed):
        self.speed = speed
        print(f"Создан доставщик со скоростью {speed} км/ч")
    def deliver(self):
        """Метод доставки"""
        print(f"Доставщик едет со скоростью {self.speed} км/ч")
class Courier(DeliveryPerson):
    def __init__(self, name, speed, phone):
        DeliveryPerson.__init__(self, speed)
        self.name = name
        self.phone = phone
        print(f"Курьер '{self.name}' создан. Телефон: {self.phone}")
    def call_client(self):
        """Курьер умеет звонить клиенту"""
        print(f"Курьер {self.name} звонит клиенту по телефону {self.phone}")
    def deliver(self):
        """Метод доставки для курьера"""
        print(f"Курьер {self.name} доставляет заказ на мотоцикле со скоростью {self.speed} км/ч")
class Drone(DeliveryPerson):
    def __init__(self, model, speed, max_height):
        DeliveryPerson.__init__(self, speed)
        self.model = model
        self.max_height = max_height
        print(f"Дрон '{self.model}' создан. Макс. высота: {max_height} м")
    def fly(self):
        """Дрон умеет летать"""
        print(f"Дрон {self.model} летит на высоте {self.max_height} м")
    def deliver(self):
        """Метод доставки для дрона"""
        print(f"Дрон {self.model} доставляет заказ по воздуху со скоростью {self.speed} км/ч")
class Order:
    STATUSES = ["создан", "в обработке", "доставляется", "доставлен", "отменен"]
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "создан"
        self.products = []
        self.delivery_person = None
        print(f"Создан заказ #{order_id}")
    def add_product(self, name, price):
        """Добавить товар в заказ"""
        product = Product(name, price)
        self.products.append(product)
        print(f"Товар '{name}' добавлен в заказ #{self.order_id}")
    def set_delivery_person(self, delivery_person):
        """Назначить доставщика для заказа"""
        self.delivery_person = delivery_person
        print(f"Доставщик назначен для заказа #{self.order_id}")
    def change_status(self, new_status):
        """Изменить статус заказа"""
        if new_status in self.STATUSES:
            old_status = self.status
            self.status = new_status
            print(f"Статус заказа #{self.order_id} изменен: {old_status} -> {new_status}")
        else:
            print(f"Ошибка: статус '{new_status}' не существует")
    def calculate_total(self):
        """Рассчитать общую стоимость заказа"""
        total = 0
        for product in self.products:
            total += product.price
        return total
    def process_delivery(self):
        """Обработать доставку заказа"""
        if self.delivery_person is None:
            print(f"Ошибка: для заказа #{self.order_id} не назначен доставщик!")
            return
        print(f"\nНачинаем доставку заказа #{self.order_id}")
        print(f"Статус: {self.status}")
        print(f"Количество товаров: {len(self.products)}")
        print(f"Общая стоимость: {self.calculate_total()} руб.")
        self.delivery_person.deliver()
        if isinstance(self.delivery_person, Courier):
            self.delivery_person.call_client()
        elif isinstance(self.delivery_person, Drone):
            self.delivery_person.fly()
        print(f"Заказ #{self.order_id} доставлен!")
        self.change_status("доставлен")
    def show_order_info(self):
        """Показать информацию о заказе"""
        print(f"\n=== Заказ #{self.order_id} ===")
        print(f"Статус: {self.status}")
        print("Товары в заказе:")
        if len(self.products) == 0:
            print("  Нет товаров")
        else:
            for i, product in enumerate(self.products, 1):
                print(f"  {i}. {product.get_info()}")
        
        print(f"Всего товаров: {len(self.products)}")
        print(f"Общая сумма: {self.calculate_total()} руб.")
        
        if self.delivery_person:
            if isinstance(self.delivery_person, Courier):
                print(f"Доставщик: Курьер {self.delivery_person.name}")
            elif isinstance(self.delivery_person, Drone):
                print(f"Доставщик: Дрон {self.delivery_person.model}")
        else:
            print("Доставщик: не назначен")
if __name__ == "__main__":
    print("=== СЛУЖБА ДОСТАВКИ ===\n")
    print("1. Создаем доставщиков:")
    courier1 = Courier("Иван", 40, "+7-999-123-45-67")
    courier2 = Courier("Петр", 35, "+7-999-987-65-43")
    drone1 = Drone("DJI Mavic", 60, 120)
    drone2 = Drone("SkyMaster X1", 80, 200)
    print("\n" + "="*50 + "\n")
    print("2. Создаем заказ 1 (доставка курьером):")
    order1 = Order(1001)
    order1.add_product("Ноутбук", 50000)
    order1.add_product("Мышь", 1500)
    order1.add_product("Чехол", 1000)
    order1.set_delivery_person(courier1)
    order1.change_status("в обработке")
    order1.change_status("доставляется")
    order1.show_order_info()
    order1.process_delivery()
    print("\n" + "="*50 + "\n")
    print("3. Создаем заказ 2 (доставка дроном):")
    order2 = Order(1002)
    order2.add_product("Смартфон", 30000)
    order2.add_product("Наушники", 5000)
    order2.set_delivery_person(drone1)
    order2.change_status("в обработке")
    order2.change_status("доставляется")
    order2.show_order_info()
    order2.process_delivery()
    print("\n" + "="*50 + "\n")
    print("4. Создаем заказ 3 (без доставщика):")
    order3 = Order(1003)
    order3.add_product("Книга", 500)
    order3.add_product("Ручка", 50)
    order3.show_order_info()
    print("\nПытаемся обработать доставку без доставщика:")
    order3.process_delivery()
    print("\n" + "="*50 + "\n")
    print("5. Один доставщик может доставлять несколько заказов:")
    order4 = Order(1004)
    order4.add_product("Цветы", 2000)
    order4.set_delivery_person(courier1)
    order4.change_status("доставляется")
    print(f"\nКурьер {courier1.name} доставляет заказы #{order1.order_id} и #{order4.order_id}")
    print("\n" + "="*50 + "\n")
    print("6. Демонстрация наследования:")
    print(f"courier1 является DeliveryPerson? {isinstance(courier1, DeliveryPerson)}")
    print(f"drone1 является DeliveryPerson? {isinstance(drone1, DeliveryPerson)}")
    print(f"courier1 является Courier? {isinstance(courier1, Courier)}")
    print(f"drone1 является Drone? {isinstance(drone1, Drone)}")
