class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    

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
        
        # статические методы также можно вызывать внутри
        print(self.norm2(self.x, self.y))
        
    def get_coords(self):
        return self.x, self.y
    
    # Статический метод не имеет доступа не к атрибутам класса не к атрибутам экземпляра класса.
    # То есть создается некая независимая, самостоятельная функция объявленная внутри класса.
    # Делается для удобства. Обычно такая функция связана с тематикой класса.
    @staticmethod
    def norm2(x, y):
        # Вычисляем квадрат нормы для произвольного радиус вектора.
        return x*x + y*y
    
     
     
v = Vector(1, 2)
print(Vector.norm2(5, 6))


