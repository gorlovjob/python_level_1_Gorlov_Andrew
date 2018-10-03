
__author__ = 'Горлов Андрей Гарриевич'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

#equation = 'y = -12x + 11111140.2121'
#x = 2.5
# вычислите и выведите y

print('Задача №1')

equation = 'y = -12x + 11111140.2121'
x = 2.5
k_str = ''
b_str = ''

for i in equation:
    if i == 'y' or i == ' ' or i == '=':
        pass
    elif i == 'x':
        break
    else:
        k_str = k_str + i
k = float(k_str)

for j in equation[equation.index('x')+1:]:
    if j == '+' or j == ' ':
        pass
    else:
        b_str = b_str + j
b = float(b_str)

print('Дано:')
print('Аргумент k =',k)
print('Аргумент b =',b)
print('Требуется решить уравнение: y =',k,'* x +',b)
print('')

y = k * x + b

print('Пусть х =',x,'. Тогда: y = ',k,'* x + ',b)
print('Ответ: y =',y)

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'

print('Задача №2')

date = '17.12.2010'
day = ''
month = ''
year = ''
month_with_31_day = [1, 3, 5, 7, 8, 10, 12]

print('Пусть заданная дата:',date)

for f in date[:date.index('.')]:
    day = day + f
    
date = date[date.index('.') + 1:]
for g in date[:date.index('.')]:
    month = month + g

year = date[date.index('.') + 1:]
    
print('Результат проверки введенной даты на корректность:')

while True:
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        print('Ошибка! Неверный формат даты!')
        print('Нужно вводить корректную дату в формате dd.mm.yyyy!')
        break
    
    if int(day) >=1 and int(day)<=31 and int(month) in month_with_31_day:
        pass
    elif int(day) >=1 and int(day)<=30 and int(month) not in month_with_31_day:
        pass
    else:
        print('Ошибка! Неверное число!')
        print('Введено число:',day)
        print('Нужно вводить корректную дату в формате dd.mm.yyyy!')
        break
    
    if int(month) >=1 and int(month) <= 12:
        pass
    else:
        print('Ошибка! Неверно введен месяц!')
        print('Введеный месяц:',month)
        print('Нужно вводить корректную дату в формате dd.mm.yyyy!')
        break

    if int(year) >=1 and int(year) <= 9999:
        pass
    else:
        print('Ошибка! Неверно введен год!')
        print('Введеный месяц:',year)
        print('Нужно вводить корректную дату в формате dd.mm.yyyy!')
        break

    print('Дата введена корректно!')
    break

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3