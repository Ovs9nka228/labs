temperatures = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
max_temp = temperatures[0]
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
min_temp = temperatures[0]
for temp in temperatures:
    if temp < min_temp:
        min_temp = temp
sum_temp = 0
for temp in temperatures:
    sum_temp = sum_temp + temp
average_temp = sum_temp / len(temperatures)
days_above_average = 0
for temp in temperatures:
    if temp > average_temp:
        days_above_average = days_above_average + 1
sorted_temperatures = temperatures.copy()
for i in range(len(sorted_temperatures)):
    for j in range(len(sorted_temperatures) - 1):
        if sorted_temperatures[j] > sorted_temperatures[j + 1]:
            temp_value = sorted_temperatures[j]
            sorted_temperatures[j] = sorted_temperatures[j + 1]
            sorted_temperatures[j + 1] = temp_value
fahrenheit_temperatures = []
for temp in temperatures:
    fahrenheit = temp * 9/5 + 32
    fahrenheit_temperatures.append(fahrenheit)
print("Температуры:", temperatures)
print("Максимальная:", max_temp, "°C")
print("Минимальная:", min_temp, "°C")
print("Средняя:", round(average_temp, 1), "°C")
print("Дней выше средней:", days_above_average)
print("Отсортированные температуры:", sorted_temperatures)
print("Температуры в Фаренгейтах:", [round(f, 1) for f in fahrenheit_temperatures])
