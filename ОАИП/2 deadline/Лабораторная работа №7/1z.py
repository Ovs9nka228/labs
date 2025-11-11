def sum_numbers(*args):
    total = 0
    for number in args:
        total = total + number
    return total
print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10, 20))
print(sum_numbers(1.5, 2.5, 3.5))
