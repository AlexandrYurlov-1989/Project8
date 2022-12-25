from animals import Human


class Student(Human):
    """ Класс студент """
    def __init__(self, type1, subtype, clacc, food, age, weight, wool, mammary, gender, name, iq, nationality, activity, number_of_completed_tasks):
        super().__init__(type1, subtype, clacc, food, age, weight, wool, mammary, gender, name, iq, nationality, activity)
        self.number_of_completed_tasks = number_of_completed_tasks # количество сданных ДЗ

    def completed_tasks(self):
        """ вывод количества сданных ДЗ """

        print(f'количество сданных ДЗ  {self.number_of_completed_tasks}')

    def say(self):
        """ Функция вывода вопроса о количестве ДЗ """

        print(f'Привет, меня завут {self.name} сколько ДЗ я сдал?')

    def __eq__(self, other):
        """ перегрузка оператора сравнения 
            для сравнения студентов по значению их сданных ДЗ """
        
        return self.number_of_completed_tasks == other.number_of_completed_tasks

