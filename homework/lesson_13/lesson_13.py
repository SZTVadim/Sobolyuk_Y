from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

# Метод написан для выполнения 10 задания что-бы была коллекция для перебора
# Так как __animals приватный атрибут мы не можем обратиться к нему из вне
    def get_animals(self):
        return self.__animals.copy()


# Полиморфизм т.к. даёт разный результат в зависимости от того Dog это или Cat
# Принимает объект общего типа animal, но вызывает метод make_sound в зависимости от того что передано
def animal_sound(animal):
    return animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)
zoo = Zoo("Городской зоопарк")
zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print(zoo.get_animals_count())

for animal in zoo.get_animals():
    animal_sound(animal)

# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
# Animal это абстрактный класс который наследуется от ABC
# Создать экземпляр такого класса нельзя т.к. это шаблон для наследников без реализации
animal = Animal()
