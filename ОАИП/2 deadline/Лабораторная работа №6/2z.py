def simple_calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Ошибка: неизвестный оператор"
    return result
result1 = simple_calculator(10, 5, "*")
print(result1)
result2 = simple_calculator(10, 5, "+")
print(result2)
result3 = simple_calculator(10, 5, "-")
print(result3)
result4 = simple_calculator(10, 5, "/")
print(result4)
