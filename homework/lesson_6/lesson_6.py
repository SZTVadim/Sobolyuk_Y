# ЗАДАНИЕ 1: Работа со словарями и перебор элементов
student_info = {"имя": "Иван", "возраст": 20, "курс": 2, "город": "Москва"}
print(student_info.keys())
print(student_info.values())
for key, value in student_info.items():
    print(f"{key}: {value}")
for value in student_info.values():
    print(value)

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей
prices = {"яблоко": 50, "банан": 30, "апельсин": 40, "груша": 35, "виноград": 60}
original_prices = prices.copy()  # Сохранил состояние для последующего использования для словаря со скидками
del prices["груша"]
removed_value = prices.pop("виноград")

# Новый словарь с теми же фруктами, но с ценами со скидкой 10%
discount_prices = {fruit: price * 0.9 for fruit, price in original_prices.items()}
print(discount_prices)

# ЗАДАНИЕ 3: Объединение словарей
student1 = {"имя": "Иван", "возраст": 20, "курс": 2}
student2 = {"имя": "Мария", "возраст": 21, "город": "Санкт-Петербург"}

# Сохранил состояние оригинального словаря student1 для последующего объединения ИСХОДНЫХ словарей в student3
original_student1 = student1.copy()

student1.update(student2)
print(student1)

# Использую переменные с ИСХОДНЫМИ словарями
student3 = original_student1.copy()
student3.update(student2)

# Вывод ИСХОДНЫХ словарей student1 (сохранившего оригинальное состояние в original_student1),student2 и нового student3
print(original_student1)
print(student2)
print(student3)
