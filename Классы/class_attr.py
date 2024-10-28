# Аттрибуты класса.

class Point:
    "Это описание класса которое можно прочитать Point.__doc__"
    color = 'red'
    circle = 2
# Переменные в классе называют свойствами или атрибутами.


# print(Point.__dict__) # Покажет все свойства класса Point. В этом словаре будут и наши два свойства color = 'red' и circle = 2.
# {'__module__': '__main__', 'color': 'red', 'circle': 2, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}

a = Point() # Создание экземпляра класса.

setattr(Point, "new_attr", "new") # Добавляет динамически новый атрибут к классу или же можно поменять значение атрибута в классе.

# print(Point.__dict__) 

print(getattr(Point, "color", False)) # Получаем атрибуты с помощью getattr и если такого атрибута нету то возвращаем False. 
# Если атрибут будет то выведет его значение.

del Point.color # Удаление атрибута.
delattr(Point, 'circle') # Второй способ удаления атрибута.
hasattr(Point, 'color') # Проверет есть ли такой атрибут.
# Это применимо и к экземплярам класса.

print(Point.__doc__)