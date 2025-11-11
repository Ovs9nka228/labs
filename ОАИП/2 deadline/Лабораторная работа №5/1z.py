from math import sqrt
point_a = (3, 7)
point_b = (10, 2)
x1 = point_a[0]
y1 = point_a[1]
x2 = point_b[0]
y2 = point_b[1]
diff_x = x2 - x1
diff_y = y2 - y1
square_x = diff_x * diff_x
square_y = diff_y * diff_y
sum_squares = square_x + square_y
distance = sqrt(sum_squares)
print("Точка A:", point_a)
print("Точка B:", point_b)
print("Расстояние между точками:", round(distance, 2))
