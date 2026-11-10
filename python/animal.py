# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return "..."
#
#     def __str__(self):
#         return f"{self.name} says: {self.speak()}"
#
# class Dog(Animal):
#     def speak(self):
#         return "Gav"
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
# print(Dog("Рекс"))
# print(Cat("Мурка"))
# print(Animal("Нечто"))

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def info(self):
#         return f'{self.name}, salary {self.salary}'
#
# class Manager(Employee):
#     def __init__(self, name, salary, team):
#         super().__init__(name, salary)
#         self.team = team
#
#     def info(self):
#         return f'{super().info()}, team {self.team}'
#
# print(Employee("John", 50000).info())
# print(Manager("John", 50000, 5).info())