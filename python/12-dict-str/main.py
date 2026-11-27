class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} работает")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def work(self):
        print(f"{self.name} пишет код")

    def __str__(self):
        return  f"Имя: {self.name}, ЗП: {self.salary}, ЯП: {self.language}"


class Designer(Employee):
    def work(self):
        print(f"{self.name} рисует интерфейс")


dev = Developer("Max", 100000, "Python")
print(dev)
print(dev.__dict__)