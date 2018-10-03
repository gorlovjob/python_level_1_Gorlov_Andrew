
__author__ = 'Горлов Андрей Гарриевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print('Задача №1')

fruits = ['apple', 'orange', 'plum', 'peach', 'banana', 'kivi', 'pineapple']
print('Форматируем список: ',fruits)
n = 1
print('Список фруктов: ')
for i in fruits:
    print('{}.{:>9}'.format(n, i))
    n += 1

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('Задача №2')

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list2 = ['b', 'd', 'g']

print('Даны два списка:')
print('Первый список: ', list1)
print('Второй список:', list2)
print('Удаляем элементы второго списка из первого:')
for i in list1:
    if i in list2:
        list1.remove(i)
print(list1)

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('Задача №3')

list = [2, 3, 4, 7, 4, 8, 6, 9, 4, 2, 89, 453, 6654]
newlist = []

print('Дан список: ', list)
for i in list:
    if i % 2 == 0:
        newlist.append(i/4)
    else:
        newlist.append(i*2)
print('Новый список: ', newlist)

input('Нажмите Enter, чтобы продолжить: ')
