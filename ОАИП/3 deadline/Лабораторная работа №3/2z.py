def sum_digits(number):
    if number < 0:
        number = -number
    if number < 10:
        return number
    last_digit = number % 10 
    remaining_number = number // 10 
    return last_digit + sum_digits(remaining_number)
print(sum_digits(12345))
print(sum_digits(100))
print(sum_digits(9))
print(sum_digits(-123))
