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
