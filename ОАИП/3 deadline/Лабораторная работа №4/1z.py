class SmartLight:
    brightness = 50
    color = "белый"
    def __init__(self):
        self.__is_on = False
    def turn_on(self):
        """Включить лампочку"""
        self.__is_on = True
        print("Лампочка включена")
    def turn_off(self):
        """Выключить лампочку"""
        self.__is_on = False
        print("Лампочка выключена")
    def set_color(self, new_color):
        """Изменить цвет лампочки"""
        self.color = new_color
        print(f"Цвет изменен на: {new_color}")
    def check_status(self):
        """Проверить статус лампочки"""
        if self.__is_on:
            return "Лампочка включена"
        else:
            return "Лампочка выключена"
if __name__ == "__main__":
    my_lamp = SmartLight()
    print("Доступные атрибуты:")
    print(f"Яркость: {my_lamp.brightness}")
    print(f"Цвет: {my_lamp.color}")
    my_lamp.turn_on()
    print(my_lamp.check_status())
    my_lamp.set_color("красный")
    print(f"Новый цвет: {my_lamp.color}")
    my_lamp.turn_off()
    print(my_lamp.check_status())
