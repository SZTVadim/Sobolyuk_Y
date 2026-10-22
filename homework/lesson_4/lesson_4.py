# ЗАДАНИЕ 1: Работа с типами данных
string_var = "Привет"
int_var = 42
float_var = 3.14
list_var = [1, 2, 3]

print(type(string_var))
print(type(int_var))
print(type(float_var))
print(type(list_var))

# ЗАДАНИЕ 2: Преобразование регистра строк
convertible_string = "python PROGRAMMING"
convertible_string.lower()
convertible_string.upper()
convertible_string.capitalize()
convertible_string.title()

# ЗАДАНИЕ 3: Удаление пробелов
string_with_spaces = "  Hello World  "
string_with_spaces.strip()
string_with_spaces.lstrip()
string_with_spaces.rstrip()

# ЗАДАНИЕ 4: Разделение и объединение строк
splittable_string = "яблоко,банан,апельсин,груша"
split_string = splittable_string.split(',')
splittable_string = " | ".join(split_string)

# ЗАДАНИЕ 5: Замена подстрок
mutable_string = "Я изучаю Python. Python - это круто!"
modified_string = mutable_string.replace("Python", "Java")

# ЗАДАНИЕ 6: Поиск и подсчет
searchable_string = "Python программирование на Python"
searchable_string.find("Python")
searchable_string.count("Python")
searchable_string.find("Java")

# ЗАДАНИЕ 7: Проверка типа символов
"Hello123".isalnum()
"12345".isdigit()
"Hello".isalpha()
"   ".isspace()

# ЗАДАНИЕ 8: Срезы строк
original_string = 'Python very good'
print(original_string[0:3])
print(original_string[-3:])
print(original_string[::2])
print(original_string[::-1])

# ЗАДАНИЕ 9: Экранирование символов
print("Он сказал: \"Привет\"")
print("Первая строка\nВторая строка")
