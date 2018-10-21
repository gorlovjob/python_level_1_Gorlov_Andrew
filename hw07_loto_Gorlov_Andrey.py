
__author__ = 'Горлов Андрей Гарриевич'

# Создадим класс, который создает карты лото
class Card():
    def __init__(self):

        import random

        def del_num(list):
            ''' Данная функция будет рандомно убирать
                лишние 4 числа в карте лото'''
            p = []
            i = 0
            while i != 4:
                p = random.randint(0,8)
                if list[p] != '  ':
                    list[p] = '  '
                    i += 1
            return list

        # Создаем список из 27-ми неповторяющихся чисел в диапазоне от 1 до 90,
        # которые будут использоваться в карте лото
        list_num = []
        str1 = []
        str2 = []
        str3 = []
        card = []

        while len(list_num) != 27:
            n = random.randint(1,90)
            if n not in list_num:
                list_num.append(n)

        # Разбиваем список чисел на 3 списка (строки) по 9 чисел и сортируем каждый
        for i in list_num[:9]:
            str1.append(i)
            str1 = sorted(str1)
        for i in list_num[9:18]:
            str2.append(i)
            str2 = sorted(str2)
        for i in list_num[18:]:
            str3.append(i)
            str3 = sorted(str3)

        # Собираем три сортированных списка (строки) в один список.
        # С одним списком чисел будет проще работать.
        # К каждому списку (строке) применяем функцию удаления лишних
        # чисел, так как по условию их должно быть 5, а клеток в строке 9.
        self.card = del_num(str1) + del_num(str2) + del_num(str3)
        
    @property  
    def card_output(self):
        ''' Данное свойство красиво выводит карту в консоль'''
        print('{:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2}\n' \
              '{:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2}\n' \
              '{:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2} {:^2}' \
              .format(self.card[0], self.card[1], self.card[2],
                      self.card[3], self.card[4], self.card[5],
                      self.card[6], self.card[7], self.card[8],
                      self.card[9], self.card[10], self.card[11],
                      self.card[12], self.card[13], self.card[14],
                      self.card[15], self.card[16], self.card[17],
                      self.card[18], self.card[19], self.card[20],
                      self.card[21], self.card[22], self.card[23],
                      self.card[24], self.card[25], self.card[26]))
        print('----------------------------\n')

    def exist_num(self, number):
        ''' Функция проверяет наличие введенного числа в карточке '''
        return number in self.card

    def close_num(self, number):
        ''' Функция вычеркивает введенное число из карточки '''
        k = self.card.index(number)
        self.card[k] = '-'

    def num_in_card(self):
        ''' Функция проверяет все ли числа карты зачеркнуты.
            Так как чисел в карте 15, должно быть 15 черточек '''
        return self.card.count('-') == 15
        

import random, sys

def gen_list_keg():
    ''' Функция создает список чисел, которые будут по порядку
        "озвучиваться ведущим лото" '''
    list_keg = []
    while len(list_keg) != 90:
        k = random.randint(1,90)
        if k not in list_keg:
            list_keg.append(k)
    return list_keg

def menu():
    ''' Функция вывода меню на экран '''
    print('Введите "y" если у вас есть такой номер в карте и вы хотите его зачеркнуть')
    print('Введите "n" если у вас нет такого номера')
    print('Введите "quit" если хотите завершить игру \n')

# Создадим карты игроков при помощи класса Card и сгенерируем список бочонков
player_card = Card()
robot_card = Card()
list_keg = gen_list_keg()

# Счетчик оставшихся бочонков:
count = 89

# Приветствие игры
print('')
print('Добро пожаловать на игру "Лото"!\n')
print('Раздаются карточки....\n')
input('Чтобы начать игру, нажмите Enter \n')

# Начинается игра
for keg in list_keg:
    print('=============================================================== \n')
    print('Новый бочонок: {} (осталось: {})\n'.format(keg, count))
    print('-------- Ваша карта --------')
    player_card.card_output
    print('----- Карта компьютера -----')
    robot_card.card_output

    # Игра не продолжится, пока игрок не введет правильное значение
    menu()
    choise = input('Каков будет ваш выбор? --> ')
    while choise != 'n' and choise != 'y' and choise != 'quit':
        print('Неверный ввод! \n')
        menu()
        choise = input('Каков будет ваш выбор? --> ')
        print('')

    # Обработка выбора игрока
    # Если игрок хочет вычеркнуть число, проверяем есть ли оно.
    # Если его нет в карте - игрок проигрывает, игра завершается.
    if choise == 'y':
        if player_card.exist_num(keg) == True:
            player_card.close_num(keg)
            print('Вы зачеркиваете число {}! \n'.format(keg))
        else:
            print('Это ложь! У вас нет числа {}! \n'.format(keg))
            print('Увы, вы проиграли! \n')
            sys.exit()

    # Если игрок не хочет вычеркивать число, проверяем есть ли оно.
    # Если оно есть в карте - игрок проигрывает, игра завершается.
    elif choise == 'n':
        if player_card.exist_num(keg) == False:
            pass
        else:
            print('Это ложь! У вас есть число {}! \n'.format(keg))
            print('Увы, вы проиграли! \n')
            sys.exit()

    # Если игрок вводит команду завершения - завершаем программу.
    elif choise == 'quit':
        print('Вы ввели команду завершения программы! \n')
        print('До встречи!!!')
        sys.exit()

    # Если каким-то невиданным образом игрок умудрится обойти while,
    # программа выдаст об этом сообщение и завершится.
    else:
        print('Завершение из-за ощибки программы!')
        print('Пользователь как-то обошел цикл while!!!')
        sys.exit()

    # Проверка наличия числа в карте компьютера и вычеркивание
    # его, если оно есть.
    if robot_card.exist_num(keg) == True:
        robot_card.close_num(keg)
        print('Компьютер зачеркивает число {}! \n'.format(keg))
    count -= 1

    # Проверяем - все ли числа в картах игроков зачеркнуты.
    # Если и у игрока, и у компьютера зачеркнуты все числа - ничья.
    if player_card.num_in_card() == True and robot_card.num_in_card() == True:
        print('Оба игрока зачеркнули последнее число! \n')
        print('НИЧЬЯ!!! \n')
        break

    # Если у игрока зачркнуты васе числа, а у компьютера - нет, игрок выиграл.
    elif player_card.num_in_card() == True and robot_card.num_in_card() == False:
        print('Вы зачеркнули последнее число! \n')
        print('ВЫ ВЫИГРАЛИ!!! \n')
        break

    # Если у компьютера зачеркнуты все числа, а у игрока - нет, игрок проиграл.
    elif player_card.num_in_card() == False and robot_card.num_in_card() == True:
        print('Компьютер зачеркнул последнее число! \n')
        print('Увы, вы проиграли! \n')
        break
    # Если и у игрока, и у компьютера не все числа зачеркнуты, играем дальше.
    else:
        input('Hажмите Enter, чтобы перейти к следующему раунду... \n')

# Завершаем игру.
print('ИГРА ЗАКОНЧЕНА!!!')

    

