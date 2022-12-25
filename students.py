from student import Student


dz_Sem = 0
dz_Bob = 0

Sem = Student('type1', 'subtype', 'clacc', 'всеяден', 23, 65, 2, 2, 'male', 'Sem', 110, 'русский', 'учусь', dz_Sem)
Bob = Student('type1', 'subtype', 'clacc', 'всеяден', 23, 65, 2, 2, 'male', 'Bob', 110, 'русский', 'учусь', dz_Bob)

check = False
while not check:
    try:
        Sem.say()
        dz_Sem = int(input('Ведите количество сданных ДЗ у Sem: '))
        Bob.say()
        dz_Bob = int(input('Ведите количество сданных ДЗ у Bob: '))
        check = True
    except ValueError:
        print('неверное значение')
        check = False

if Sem == Bob:
    print('количество сданных ДЗ у студентов равное')
else:
    print('количество сданных ДЗ у студентов разное')