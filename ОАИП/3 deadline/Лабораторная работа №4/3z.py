class Character:
    def __init__(self, name):
        self.name = name
        print(f"Создан персонаж: {self.name}")
    def move(self):
        """Метод для перемещения персонажа"""
        print(f"{self.name} идет вперед")
class Archer(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        print(f"{self.name} - это Лучник")
    def shoot(self):
        """Метод для стрельбы из лука"""
        print(f"{self.name} стреляет из лука!")
class Knight(Character):
    def __init__(self, name):
        Character.__init__(self, name)
        print(f"{self.name} - это Рыцарь")
    def attack_sword(self):
        """Метод для атаки мечом"""
        print(f"{self.name} бьет мечом!")
if __name__ == "__main__":
    print("=== Демонстрация RPG-персонажей ===\n")
    print("1. Создаем базового персонажа:")
    hero = Character("Герой")
    hero.move()
    print("\n" + "="*50 + "\n")
    print("2. Создаем Лучника:")
    legolas = Archer("Леголас")
    legolas.move() 
    legolas.shoot()
    print("\n" + "="*50 + "\n")
    print("3. Создаем Рыцаря:")
    lancelot = Knight("Ланселот")
    lancelot.move()
    lancelot.attack_sword()
    print("\n" + "="*50 + "\n")
    print("4. Все персонажи могут двигаться:")
    characters = [
        Character("Путник"),
        Archer("Робин Гуд"),
        Knight("Король Артур")
    ]
    for char in characters:
        char.move()
        if isinstance(char, Archer):
            char.shoot()
        elif isinstance(char, Knight):
            char.attack_sword()
        print()
    print("\n" + "="*50 + "\n")
    print("5. Еще один пример Лучника:")
    elf = Archer("Эльф")
    elf.move()
    elf.shoot()
    print(f"\nЭльф является персонажем? {isinstance(elf, Character)}")
    print(f"Эльф является лучником? {isinstance(elf, Archer)}")
    print(f"Эльф является рыцарем? {isinstance(elf, Knight)}")
