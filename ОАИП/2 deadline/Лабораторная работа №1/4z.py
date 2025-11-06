from random import randint
random_num = randint(1, 100)
pop = 0
print("Угадай число от 1 до 100",random_num)
while True:
    print("Попробуйте угадать число")
    num = int(input("Введите число: "))
    pop = pop + 1
    if num == random_num:
        print(f"Угадал c {pop} попытки")
        break
    elif num < random_num:
        print("Больше, попробуй еще")
    else:
        print("Меньше, попробуй еще")
    
        
