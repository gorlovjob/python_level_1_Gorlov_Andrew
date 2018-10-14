
__author__ = 'Горлов Андрей Гарриевич'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('Задача №1')

def new_9_folder():
    ''' Функция берет диапазон цифр от 1 до 9 (10 не включено)
        и создает директории с названиями от dir_1 до dir_9'''
    import os
    
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.mkdir(dir_path)
            print('Директория dir_{} успешно создана!'.format(i))
        except FileExistsError:
            print("Такая директория уже существует!")

def del_9_folder():
    ''' Функция берет диапазон цифр от 1 до 9 (10 не включено)
        и удаляет директории с названиями от dir_1 до dir_9'''
    import os
    
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), "dir_{}".format(i))
        try:
            os.rmdir(dir_path)
            print('Директория dir_{} успешно удалена!'.format(i))
        except FileNotFoundError:
            print("Нет такой директории!")

input('Нажмите Enter, чтобы продемонстрировать создание папок: ')
new_9_folder()

input('Нажмите Enter, чтобы продемонстрировать удаление папок: ')
del_9_folder()

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('Задача №2')

def show_folder():
    import os
    
    print('Список папок текущей директории: ')
    for path, dirs, files in os.walk(os.getcwd()):
        for i in dirs:
            print(i)

show_folder()

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('Задача №3')

def copy_script():
    import os, sys, shutil
    
    my_script = os.path.basename(sys.argv[0])
    copy_my_script = 'copy_' + my_script

    print('Копируем файл, из которого запущен данный скрипт...')
    shutil.copyfile(my_script, copy_my_script)
    
    print('Файл скопирован и называется: {}'.format(copy_my_script))
        
copy_script()

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')
