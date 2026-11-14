class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."
    def is_long(self):
        return self.pages > 300


book1 = Book("Код. Тайный язык информатики", "Чарльз Петцольд", 100)
book2 = Book("Грокаем алгоритмы", "Адитья Бхаргава", 200)
book3 = Book("Изучаем Python", "Эрик Мэтиз", 500)
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())


class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
        return False
    def get_balance(self):
        return self.balance

bank_acc = BankAccount("Ян", 1000)
bank_acc.deposit(100)
bank_acc.withdraw(200)
print(bank_acc.get_balance())
bank_acc.withdraw(3000)
