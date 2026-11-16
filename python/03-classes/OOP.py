# class Cat:
#     name =  None
#     age = None
#     isHappy = None
#
#     def __init__(self, name, age, isHappy):
#         self.set_data(name, age, isHappy)
#         self.get_data()
#
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print("Name:", self.name, "age:", self.age, "Happy:", self.isHappy)
#
# cat1 = Cat("Barsik", 3, True)
# cat2 = Cat("Max", 2, False)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Vector: ({self.x}, {self.y})"
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
# v1 = Vector(3, 4)
# v2 = Vector(1,2)
# print(v1 + v2)
# print(v1 - v2)
# print(v1)

# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.count += 1
#
# r1 = Robot("R2")
# r2 = Robot("C3")
# r3 = Robot("BB")
#
# print(Robot.count)
# print(r3.count)

# class Student:
#
#     def __init__(self, name, grades = None):
#         if grades is None:
#             grades = []
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         else:
#             return sum(self.grades) / len(self.grades)
#
# s1 = Student("John")
# s2 = Student("Alice")
# s1.add_grade(5)
# s1.add_grade(4)
#
# print(s1.grades)
# print(s2.grades)
# print(s1.average())
# print(s2.average())

# class Playlist:
#
#     def __init__(self, name, songs= None):
#         self.name = name
#         if songs is None:
#             songs = []
#         self.songs = songs
#
#     def add(self, song):
#         self.songs.append(song)
#
#     def __len__(self):
#         return len(self.songs)
#
#     def __str__(self):
#         return f"Playlist: {self.name}: {len(self.songs)} songs"
#
#
# p1 = Playlist("Rock")
# p2 = Playlist("Jazz")
# p1.add("Song A")
# p1.add("Song B")
# p1.add("Song C")
#
# print(len(p1))   # 3
# print(len(p2))   # 0
# print(p1)        # Плейлист "Рок": 3 песен
# print(p2)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return f"Hello my name is {self.name}. I'm  {self.age} years old"
#
# class Student(Person):
#     def __init__(self, name, age, school):
#         super().__init__(name, age)
#         self.school = school
#     def greet(self):
#         base = super().greet()
#         return f"{base}. I studying at the {self.school}"
#
# boris = Person("Boris", 18)
# print(boris.greet())
# anna = Student("Anna", 22, "MGU")
# print(anna.greet())



# class Ticket:
#     def __init__(self, cost):
#         self.cost = cost
#
#     def final_price(self):
#         return self.cost
#
#
# class ChildTicket(Ticket):
#     def final_price(self):
#         return self.cost // 2
#
#
# child = ChildTicket(400)
# print(child.final_price())