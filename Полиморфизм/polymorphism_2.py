# В этом примере у нас есть несколько классов (Rectangle, Circle, Triangle), 
# и каждый из них имеет метод area, который возвращает площадь фигуры. 
# Хотя фигуры разные, метод area у всех одинаковый по названию, но выполняет разные вычисления.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Полиморфизм: функция может принимать объекты разных классов
def print_area(shape):
    print(f"Площадь: {shape.area()}")

# Создаем объекты разных классов
shapes = [Rectangle(10, 20), Circle(7), Triangle(10, 15)]

# Используем полиморфизм для вызова метода area
for shape in shapes:
    print_area(shape)
    
# Здесь каждый класс реализует метод area по-разному в зависимости от фигуры. 
# Функция print_area не заботится о том, какой именно объект ей передали, она просто вызывает метод area.
