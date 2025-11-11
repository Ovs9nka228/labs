colors = {
    "красный": (255, 0, 0),
    "зеленый": (0, 255, 0),
    "синий": (0, 0, 255),
    "белый": (255, 255, 255),
    "черный": (0, 0, 0),
    "желтый": (255, 255, 0),
    "фиолетовый": (128, 0, 128)
}
print("Доступные цвета:")
for color_name, rgb in colors.items():
    print(f"{color_name}: {rgb}")
print()
color1 = "красный"
color2 = "синий"
print(f"Смешиваем {color1} и {color2}:")
rgb1 = colors[color1]
rgb2 = colors[color2]
print(f"{color1}: {rgb1}")
print(f"{color2}: {rgb2}")
mixed_r = (rgb1[0] + rgb2[0]) // 2
mixed_g = (rgb1[1] + rgb2[1]) // 2
mixed_b = (rgb1[2] + rgb2[2]) // 2
mixed_color = (mixed_r, mixed_g, mixed_b)
print(f"Результат смешивания: {mixed_color}")
print()
color_to_invert = "белый"
print(f"Инвертируем цвет {color_to_invert}:")
original_rgb = colors[color_to_invert]
print(f"Исходный цвет: {original_rgb}")
inverted_r = 255 - original_rgb[0]
inverted_g = 255 - original_rgb[1]
inverted_b = 255 - original_rgb[2]
inverted_color = (inverted_r, inverted_g, inverted_b)
print(f"Инвертированный цвет: {inverted_color}")
print()
print("Все цвета и их инверсия:")
for color_name, rgb in colors.items():
    inverted_r = 255 - rgb[0]
    inverted_g = 255 - rgb[1]
    inverted_b = 255 - rgb[2]
    inverted_rgb = (inverted_r, inverted_g, inverted_b)
    print(f"{color_name}: {rgb} -> {inverted_rgb}")
