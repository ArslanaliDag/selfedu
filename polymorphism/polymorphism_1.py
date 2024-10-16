# Полиморфизм в объектно-ориентированном программировании — это способность функций обрабатывать объекты разных классов, 
# если они реализуют одинаковые методы. 
# Основная идея полиморфизма заключается в том, что можно писать код, который может работать 
# с объектами разных типов, не зная их конкретной реализации. 
# Это позволяет создавать гибкие и расширяемые системы.

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

# Функция, принимающая объект любого класса, наследующего Animal
def make_sound(animal):
    print(animal.sound())

# Используем полиморфизм
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    make_sound(animal)

# Есть базовый класс Animal, который определяет метод sound, но не реализует его (используется pass).
# Классы Dog, Cat и Cow наследуют от Animal и предоставляют собственную реализацию метода sound.
# Функция make_sound использует полиморфизм, вызывая метод sound для объектов разных классов, 
# но она не знает, к какому конкретно классу объект принадлежит.
# Полиморфизм позволяет единообразно обрабатывать объекты разных классов, что делает код более универсальным и масштабируемым.