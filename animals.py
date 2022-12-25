class Animals:
    """ Классификация для всех животных"""

    def __init__(self, type1, subtype, clacc, food, age, weight):
        self.type1 = type1      # Тип (хородвые, иглокожие, молюски, членистоногие, и тп )
        self.subtype = subtype  # Подтип (позвоночные, безчерепные, )
        self.clacc = clacc      # Класс (млекопитающие, птицы, земноводные, пресмыкающие)
        self.food = food        # чем питается
        self.age = age          # Возраст (сколько полных лет прожил на земле)
        self.weight = weight    # Вес (в кг)

    def move(self, text):
        """ Способ передвижения """

        print(text)

    def eats(self):
        """ Способ питания животного """

        if self.food == 'хищник':
            print('я ем других животных')
        elif self.food == 'травоядный':
            print('я ем растения')
        else:
            print('всеяден')

class Mammals(Animals):
    """ Класс животных """

    def __init__(self, type1, subtype, clacc, food, age, weight, wool, mammary, gender):
        super().__init__(type1, subtype, clacc, food, age, weight)
        self.wool = wool        # длинна шерсти в сантиметрах 
        self.mammary = mammary  # количество сосков(молочных желёз)
        self.gender = gender    # пол млекопитающего
    
    def wool1(self):
        print(f'есть шерсть длинной {self.wool} см')

class Human(Mammals):
    """ Вид млекопитающих - человек """

    def __init__(self, type1, subtype, clacc, food, age, weight, wool, mammary, gender, name, iq, nationality, activity):
        super().__init__(type1, subtype, clacc, food, age, weight, wool, mammary, gender)
        self.name = name                # имя человека
        self.iq = iq                    # уровень интеллекта 
        self.nationality = nationality  # национальность
        self.activity = activity        # чем занимается

    def intelligent_work(self):
        """ савершаемая деятельность """

        print(f'я {self.activity}')

    def say(self):
        """ назвать свое имя """
        
        print(f'Меня завут {self.name}')

class Cat(Mammals):
    """ Вид млекопитающих - кот """

    def __init__(self, type1, subtype, clacc, food, age, weight, wool, mammary, gender, name, paroda, activity, latok):
        super().__init__(type1, subtype, clacc, food, age, weight, wool, mammary, gender)
        self.name = name         # кличка питомца
        self.paroda = paroda     # парода
        self.activity = activity # что делает
        self.latok = latok       # латок либо пустой либо нет

    def do_something(self):
        """ чем занят """

        print(f'кот делает {self.activity}')

    def meow(self):
        """ кот делает - мяу """

        print('Мяу-мяу!')

    

class Dog(Mammals):
    """ Вид млекопитающих - собака """

    def __init__(self, type1, subtype, clacc, food, age, weight, wool, mammary, gender, name, paroda, activity, chain):
        super().__init__(type1, subtype, clacc, food, age, weight, wool, mammary, gender)
        self.name = name         # кличка питомца
        self.paroda = paroda     # парода
        self.activity = activity # что делает
        self.chain = chain       # длинна цепи (в метрах)

    def do_something(self):
        """ чем занят """

        print(f'сабака {self.activity}  на цепи длинной {self.chain} м')

    def woof(self):
        """ собака делает - гав """

        print('Гав-гав!')

    def walk(self):
        """ прагулка на длинном поводке """

        print(f'')

# B = 'Боб'
# Bob = Human('type1', 'subtype', 'clacc', 'всеяден', 30, 70, 2, 2, 'male', B, 110, 'русский', 'работаю')
# Bob.say()
# Bob.eats()
# Bob.intelligent_work()

# Barsik = Cat('type1', 'subtype', 'clacc', 'всеяден', 2, 4, 5, 6, 'male', 'Barsik', 'блохастый', 'тыгыдык', True)
# Barsik.do_something()

# Muhtar = Dog('type1', 'subtype', 'clacc', 'всеяден', 4, 15, 16, 6, 'male', 'Muhtar', 'овчарка', 'сторожит', 2)
# Muhtar.do_something()
