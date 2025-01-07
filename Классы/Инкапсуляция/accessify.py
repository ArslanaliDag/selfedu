# accessify - это отдельный модуль корорый надо установить pip install accessify.

class Point:
    def __init__(self, x = 0, y = 0):
        # у переменной x тип private, а если с одни подчеркиванием то тип protected
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами!")
    
    
    @classmethod
    # инкапсулированными могут быть и методы
    def __check_value(cls, arg):
        return type(arg) in(int, float) 
    
    
    def set_coord(self, x, y):
        # if type(x) in(int, float) and type(y) in(int, float):
        # ВОт для таких целей, к примеру, можно и использвоать методы класса.
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами!")
    
    
    def get_coord(self):
        return  self.__x, self.__y
    
    
pt = Point()
pt.set_coord(2, 33)
print(pt.get_coord())