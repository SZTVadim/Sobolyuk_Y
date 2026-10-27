# ЗАДАНИЕ 1: Добавление элементов в список
fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "груша"])
fruits.insert(1, "виноград")

# ЗАДАНИЕ 2: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.remove("банан")
poped_fruit = fruits.pop()

# ЗАДАНИЕ 3: Поиск элементов в списке
fruits = ["яблоко", "банан", "апельсин", "банан"]
fruits.index("банан")
fruits.count("банан")

# ЗАДАНИЕ 4: Сортировка и реверс списка
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
print(numbers)

# ЗАДАНИЕ 5:
cubes = [c ** 3 for c in range(1, 9)]
cubes_min = min(cubes)
cubes_max = max(cubes)
print("Массив кубов:", cubes)
print("Минимальные и максимальные значения в массиве:",
      cubes_min, "и", cubes_max)

# ЗАДАНИЕ 6:
numbers = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
numbers_over_ten = [n for n in numbers if n > 10]
result = sum(numbers_over_ten)
print(result)

# ЗАДАНИЕ 7:
cities = ["москва", "санкт-петербург", "казань"]
titled_cities = [c.title() for c in cities]
print(titled_cities)
