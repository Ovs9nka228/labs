def power(number, exponent=2):
    result = 1
    for i in range(exponent):
        result = result * number
    return result
print(power(3, 3))
print(power(5))
