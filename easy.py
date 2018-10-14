
__author__ = 'Горлов Андрей Гарриевич'

def new_folder(name):
    ''' Функция берет название папки и создает
        директорию с таким названием'''
    import os
    
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('Директория {} успешно создана!'.format(name))
    except FileExistsError:
        print("Такая директория уже существует!")

def del_folder(name):
    ''' Функция берет название папки и удаляет
        директорию с таким названием'''
    import os
    
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print('Директория {} успешно удалена!'.format(name))
    except FileNotFoundError:
        print("Нет такой директории!")

def show_folder():
    import os
    
    print('Список папок текущей директории: ')
    for path, dirs, files in os.walk(os.getcwd()):
        for i in dirs:
            print(i)

def move_to_folder(name):
    import os

    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.chdir(dir_path)
        print('Переход в директорию {} успешно завершен!'.format(name))
    except FileNotFoundError:
        print("Не удалось перейти! Такой директории не существует")
