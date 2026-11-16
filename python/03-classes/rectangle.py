class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

r = Rectangle(3, 4)
r2 = Rectangle(5, 6)

print(r.area())
print(r.perimeter())
print(r2.area())
print(r2.perimeter())