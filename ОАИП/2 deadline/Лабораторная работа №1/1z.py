num = int(input("Введите число: "))
zero = 0
while num > 0:
    last_num = num % 10
    zero = zero + last_num
    num = num // 10
print("Сумма цифр: ", zero)
    
