
__author__ = 'Горлов Андрей Гарриевич'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

print('Задача №1')

# Класс имен
class Names:
    def __init__(self, name, surname, surname2):
        self.name = name
        self.surname = surname
        self.surname2 = surname2

    # Получение полного имени
    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.surname2

    # Получение фамилии и инициалов
    def short_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.surname2[0] + '.'

# Класс родителей (наследует класс имен)
class Parent(Names):
    def __init__(self, name, surname, surname2, pupil):
        Names.__init__(self, name, surname, surname2)
        self.pupil = pupil

# Класс учеников (наследует класс имен)
class Pupil(Names):
    def __init__(self, name, surname, surname2, class_room, mother, father):
        Names.__init__(self, name, surname, surname2)
        self.class_room = class_room
        #{'class_num': int(self.class_room.split()[0]),
         #                  'class_char': self.class_room.split()[1]}
        self.mother = mother
        self.father = father

# Класс учителей (наследует класс имен)
class Teacher(Names):
    def __init__(self, name, surname, surname2, class_list, subject):
        Names.__init__(self, name, surname, surname2)
        self.class_list = class_list
        self.subject = subject

Parents = [Parent('Иван', 'Иванов', 'Иванович', 'Макаров А.И'),
           Parent('Ольга', 'Оленова', 'Олеговна', 'Макаров А.И.'),
           Parent('Петр', 'Петров', 'Петрович', 'Комаров Г.П.'),
           Parent('Наталья', 'Нефедова', 'Ефремовна', 'Комаров Г.П.'),
           Parent('Геннадий', 'Городков', 'Петрович', 'Васильев С.Г.'),
           Parent('Юлия', 'Городкова', 'Семеновна', 'Васильев С.Г.')]

Pupils = [Pupil('Андрей', 'Макаров', 'Иванович', '8 А', 'Ольга О.О.', 'Иванов И.И.'),
          Pupil('Григорий', 'Комаров', 'Петрович', '8 А', 'Нефедова Н.Е.', 'Петров П.П.'),
          Pupil('Семен', 'Васильев', 'Геннадиевич', '9 Б', 'Городкова Ю.С.', 'Городков Г.П.')]

Teachers = [Teacher('Василий', 'Шульга', 'Евгеньевич', '8 А, 9 Б', 'математика'),
            Teacher('Михаил', 'Старых', 'Федорович', '9 Б, 8 А', 'литература'),
            Teacher('Юрий', 'Готра', 'Владимирович', '8 А', 'труд')]

print('')
print('Список классов в школе: \n')
l = []
for Pupil in Pupils:
    l.append(Pupil.class_room)
for i in set(l):
    print(i)

print('')
print('Список учеников 8 А класса: \n')
for Pupil in Pupils:
    if Pupil.class_room == '8 А':
        print(Pupil.short_name())

print('')
print('Список предметов Макарова Андрея Ивановича: \n')
for Pupil in Pupils:
    if Pupil.surname == 'Макаров':
        for Teacher in Teachers:
            if Pupil.class_room in Teacher.class_list:
                print('Ученик: {} {} класса. Учитель {} ведет предмет: {}'.format(Pupil.short_name(),
                                                                                  Pupil.class_room,
                                                                                  Teacher.short_name(),
                                                                                  Teacher.subject))
                
mother = ''
father = ''
print('')
print('Имена родителей Васильева Семена Геннадиевича: \n')
for Pupil in Pupils:
    if Pupil.surname == 'Васильев':
        for Parent in Parents:
            if Parent.short_name() == Pupil.mother:
                mother = Parent.full_name()
            elif Parent.short_name() == Pupil.father:
                father = Parent.full_name()
print('Мать:', mother)
print('Отец:', father, '\n')

print('')
print('Cписок учителей, преподающих в 9 Б: \n')   
for Teacher in Teachers:
    if '9 Б' in Teacher.class_list:
        print(Teacher.full_name())
print('')

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')
