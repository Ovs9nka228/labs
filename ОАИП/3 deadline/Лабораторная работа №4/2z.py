class CreditCard:
    owner_name = "Иван Иванов"
    _balance = 1000.0
    def __init__(self, card_number, cvc_code, pin_code):
        self.__number = card_number
        self.__cvc = cvc_code
        self.__pin = pin_code
        print(f"Карта создана для владельца: {self.owner_name}")
    def __check_pin(self, pin_to_check):
        """Проверить ПИН-код"""
        if self.__pin == pin_to_check:
            return True
        else:
            return False
    def pay(self, amount, pin_code):
        """Оплатить покупку"""
        print(f"Попытка оплаты на сумму: {amount} руб.")
        if self.__check_pin(pin_code):
            if amount <= self._balance:
                self._balance -= amount
                print(f"Оплата успешна! С карты списано: {amount} руб.")
                print(f"Остаток на карте: {self._balance} руб.")
                return True
            else:
                print("Недостаточно средств на карте!")
                return False
        else:
            print("Неверный ПИН-код! Оплата отменена.")
            return False
    def show_info(self):
        """Показать информацию о карте"""
        print(f"Владелец: {self.owner_name}")
        print(f"Баланс: {self._balance} руб.")
        if hasattr(self, '_CreditCard__number'):
            masked_number = "**** **** **** " + self.__number[-4:]
            print(f"Номер карты: {masked_number}")
    def check_balance(self):
        """Проверить баланс"""
        return self._balance
if __name__ == "__main__":
    print("=== Банковская карта ===")
    my_card = CreditCard(
        card_number="1234567812345678",
        cvc_code="123",
        pin_code="0000"
    )
    print("\nИнформация о карте:")
    my_card.show_info()
    print("\n--- Попытка оплаты с правильным ПИН-кодом ---")
    my_card.pay(500, "0000")
    print("\n--- Попытка оплаты с неправильным ПИН-кодом ---")
    my_card.pay(200, "1111")
    print("\n--- Попытка оплаты суммы больше баланса ---")
    my_card.pay(800, "0000")
    print(f"\nТекущий баланс: {my_card.check_balance()} руб.")
    print(f"\nДоступ к защищенному атрибуту: {my_card._balance} руб.")
    print(f"Владелец карты: {my_card.owner_name}")
