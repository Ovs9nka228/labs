class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier
    def __call__(self, number):
        return self.multiplier * number
by_5 = Multiplier(5)
print(by_5(10))
print(by_5(2))
by_3 = Multiplier(3)
print(by_3(4))
print(by_3(7))
