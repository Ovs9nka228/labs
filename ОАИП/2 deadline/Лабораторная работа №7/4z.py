call_counter = 0
def increment_counter():
    global call_counter
    call_counter = call_counter + 1
print("До вызовов функции:", call_counter)
increment_counter()
print("После первого вызова:", call_counter)
increment_counter()
print("После второго вызова:", call_counter)
increment_counter()
print("После третьего вызова:", call_counter)
