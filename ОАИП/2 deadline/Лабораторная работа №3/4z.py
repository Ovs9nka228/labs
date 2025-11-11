products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
max_sold = 0
best_selling_product = ""
for product_name, product_info in products.items():
    if product_info["sold"] > max_sold:
        max_sold = product_info["sold"]
        best_selling_product = product_name
print(f"1. Самый продаваемый товар: {best_selling_product} (Продано {max_sold} шт.)")
total_revenue = 0
for product_name, product_info in products.items():
    revenue = product_info["price"] * product_info["sold"]
    total_revenue = total_revenue + revenue
print(f"2. Общая выручка магазина: {total_revenue} рублей")
max_revenue = 0
best_revenue_product = ""
for product_name, product_info in products.items():
    revenue = product_info["price"] * product_info["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        best_revenue_product = product_name
print(f"3. Товар с наибольшей выручкой: {best_revenue_product} (выручка {max_revenue} рублей)")
