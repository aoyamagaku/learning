# def count_even(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count +=1
#     return count
#
# print(count_even([1, 2, 3, 4, 6]))
# print(count_even([1, 3, 5]))
# print(count_even([]))
from dataclasses import replace
from time import sleep


# def is_palindrome(text):
#     ready_text = text.replace(" ", "").lower()
#     reverse_text = ready_text[::-1]
#     if ready_text == reverse_text:
#         return True
#     else:
#         return False
#
# print(is_palindrome("шалаш"))
# print(is_palindrome("А роза упала на лапу Азора"))
# print(is_palindrome("Python"))

# def most_common_word(text):
#     text = text.lower()
#     text_dict = {}
#     for i in text.split():
#         if i in text_dict:
#             text_dict[i] += 1
#         else:
#             text_dict[i] = 1

#     best_word = None
#     best_count = 0
#     for key in text_dict:
#         if text_dict[key] > best_count:
#             best_word = key
#             best_count = text_dict[key]
#     return best_word

# print(most_common_word("кот пёс кот рыба Кот пёс"))

# list_numbers = []

# while True:
#     number = input("Please enter a number: ")
#     if number == "stop":
#         break
#     try:
#         number = float(number)
#         list_numbers.append(number)
#     except ValueError:
#         print("Это не число")
# if len(list_numbers) == 0:
#     print("Чисел нет")
# else:
#     count = len(list_numbers)
#     total = sum(list_numbers)
#     average = round(sum(list_numbers) / count, 2)
#     print(f"Кол-во чисел: {count}, Сумма всех чисел: {total}, Среднее число: {average}")

class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Неверная сумма")
        else:
            self.balance += amount
            self.history.append(f"+{amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Неверная сумма")
        elif amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            self.history.append(f"-{amount}")

    def transfer(self, other, amount):
        if amount <= 0:
            print("Неверная сумма")
        elif amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            other.balance += amount
            self.history.append(f"перевод -{amount} → {other.name}")
            other.history.append(f"перевод +{amount} ← {self.name}")

    def show_history(self):
        for i in self.history:
            print(i)


    def __str__(self):
        return f"{self.name}: {self.balance}"

ivan = Account("Иван")
maria = Account("Мария")

ivan.deposit(200)
ivan.withdraw(50)
ivan.transfer(maria, 100)
ivan.transfer(maria, 500)

print(ivan)
print(maria)

print("История Ивана:")
ivan.show_history()
print("История Марии:")
maria.show_history()


