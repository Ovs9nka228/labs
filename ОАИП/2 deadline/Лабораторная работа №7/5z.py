def format_report(report_title, *data, **properties):
    print(f"--- Отчет: {report_title} ---")
    print()
    print("Данные:")
    if len(data) == 0:
        print("- Данных нет")
    else:
        for item in data:
            print(f"- {item}")
    print()
    print("Свойства:")
    if len(properties) == 0:
        print("- Свойств нет")
    else:
        for key, value in properties.items():
            print(f"- {key}: {value}")
    print()
format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)
