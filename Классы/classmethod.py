class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    
    # Метод класс может обращаться к атрибутам самого класса но не к атрибутам экземпляра класса. Потому что идет ссылка на сам класс.
    # Мы может вызвать метод validate через сам класс. Смотрите ниже. Мы вызываем метод validate без передачи в него доб значения self 
    # потому что это метод класса а не экземпляра класса
    @classmethod
    def validate(cls, ars):
        return cls.MIN_COORD <= ars <= cls.MAX_COORD
    
    def __init__(self, x, y):
        self.x = self.y = 0 # обнуляем переменные
        # вызовем валидатор внутри метода инит
        # Если мы напишем v = Vector(1, 200) то получим в консоли (0, 0)
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        
    def get_coords(self):
        return self.x, self.y
 
    
v = Vector(1, 200)
print(Vector.validate(5))
res = Vector.get_coords(v)
print(res)


