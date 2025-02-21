class Database:
    __instant = None
    
    # Мы проверяем атрибут __instant и если он None то мы создаем класс с помощью родительского super класса __new__,
    # а если он уже создан то просто возвращаем его не создавая новый - singleton. То есть мы не создаем новый класс, а возвращаем ссылку на уже созданный.
    def __new__(cls, *args, **kwargs):
        if cls.__instant is None:
            cls.__instant = super().__new__(cls)
        return cls.__instant
    
    # Тут мы при завершении программы возвращаем все как было по-умолчанияю. 
    # То есть если обьект будет удален сборщиком мусора то __instant снова будет None.
    # Вот и эти строчки с 4 и по 15 определяют патерн Singleton.
    def __del__(self):
        Database.__instant = None
        
    def __init__(self, user, pwd, port):
        self.user = user
        self.pwd = pwd
        self.port = port
        
    def connect(self):
        print(f"Соединение с БД: {self.user}, {self.pwd}, {self.port}")
        
    def close(self):
        print("Закрытие cоединение с БД")
        
    def read(self):
        return "Данные из БД"
    
    def write(self, data):
        print(f"Запись в БД {data}")


db = Database('root', '12345', 80)
db2 = Database('root2', '54321', 40)
print(id(db), id(db2)) 
# 1354867519520 1354867519520
# выведем id обьектов и увидим что они одинаковые. Это нам говорит что у нас создался только один обьект. 
# db2 это не новый обьект Database а ссылка на уже созданный

db.connect()
db2.connect()
# Соединение с БД: root2, 54321, 40
# Соединение с БД: root2, 54321, 40
# Почему мы увидили последние данные ведь не должно было бы меняться?
# Обьект тот же, новый обьект не создался. Просто у нас есть метод __init__ в нем мы каждый раз 
# создаем локальные свойства или меняем если они уже были созданы.
# Чтобы предотвратить такое есть еще один магический метод __call__ но о нем мы поговорим ниже в примере с __call__.
