print("**Регистрация пароля**")
password = input("Введите пароль: ")
pod = input("Подтвердите пароль: ")
if pod == password:
    print("Успешно")
else:
    print("Пароли не совпадают")
    exit()
    
print("**Автроизация пароля**")
prov = input("Введите пароль: ")
if prov == password:
    print("Access")
else:
    print("Denied")
