# Методы класса. Self.
# Имена методов в классах это то же атрибуты класса. Просто это функции.

class Point:
    color = 'red'
    circle = 2
    
    # self - ссылка на экземпляр класса который вызывает этот метод. 
    # Чтобы знать какой экземпляр класса вызвал метод.
    def set_coords_1(self):
        print('Вызов метода set_coords' + str(self))
        
    def set_coords_2(self, x, y):
        self.x = x
        self.y = y
        # Тут мы в вызываемом экземпляре класса создали 
        # две переменные self.x и self.y и присвоили им переданные значение x, y.
        
    def get_coords(self):
        return (self.x, self.y)    
        
pt = Point()
pt.set_coords_2(1, 2)
print(pt.__dict__) # {'x': 1, 'y': 2}
print(pt.get_coords()) # (1, 2)
#  Вот для этого и успользуется self чтобы мы могли работать с локальными атрибутами экземпляра класса.


