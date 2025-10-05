print("Введите ваше ФИО через пробел:")
fio = input()
fio_parts = fio.split()

f = fio[0]
i = fio[11]
o = fio[16]

f_correct = f.capitalize()
i_correct = i.capitalize()
o_correct = o.capitalize()

fio_final = f_correct +  i_correct + o_correct

print("Добро пожаловать", fio_final)
