# accessify - это отдельный модуль корорый надо установить pip install accessify.
from accessify import private, protected

class Point:
    def __init__(self, x = 0, y = 0):
        # у переменной x тип private, а если с одни подчеркиванием то тип protected
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами!")
    
    @private
    @classmethod
    # инкапсулированными могут быть и методы
    def check_value(cls, arg):
        return type(arg) in(int, float) 
    
    
    def set_coord(self, x, y):
        # if type(x) in(int, float) and type(y) in(int, float):
        # ВОт для таких целей, к примеру, можно и использвоать методы класса.
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами!")
    
    
    def get_coord(self):
        return  self.__x, self.__y
    
    
pt = Point()
pt.set_coord(2, 33)
pt.check_value(5)
# accessify.errors.InaccessibleDueToItsProtectionLevelException: Point.check_value() is inaccessible due to its protection level
# то есть тут мы не вызовим метод check_value потому что он помечен как протектед
# а если мы уберем декоратор @private то никаких ошибок не будет и этот метод будет ка кобычный метод класса
# декорация читается сверху вниз т. е. в начале @private потом @classmethod в такой последовательности
# использование модуля accessify и его декораторов private, protected является более сильной защитой метода чем стандартное __ 
# стандартное __ мы можем обойти вызвав метод так pt._Point__check_value(5), а при использовании accessify так не сделаешь.
# accessify используют когда очень надежно надо защитить методы, обычно бывает достаточно стандартного __ двойного подчеркивания