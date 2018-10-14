
__author__ = 'Горлов Андрей Гарриевич'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# ====================================================
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("\n \n")
    print("help - получение справки \n")
    print("mkdir <dir_name> - создание директории \n")
    print("cp <file_name> - создание копии указанного файла \n")
    print("rm <file_name> - удаление указанного файла \n")
    print("cd <full_path or relative_path> - смена текущей директории на указанную \n")
    print("ls - отображение полного пути текущей директории \n")
    print("ping - тестовый ключ \n \n")


def make_dir():
    if not dir_name:
        print("\n")
        print("Необходимо указать имя директории вторым параметром \n")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print("\n")
        print('директория {} создана \n'.format(dir_name))
    except FileExistsError:
        print("\n")
        print('директория {} уже существует \n'.format(dir_name))

def copy_file():
    if not dir_name:
        print("\n")
        print("Необходимо указать имя файла вторым параметром \n")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    copy_my_script = 'copy_' + dir_name
    new_file_path = os.path.join(os.getcwd(), copy_my_script)
    try:
        print("\n")
        print('Копируем файл {} ... \n'.format(dir_name))
        shutil.copyfile(file_path, new_file_path)
    
        print('Файл скопирован и называется: {}'.format(copy_my_script))
    except FileNotFoundError:
        print("\n")
        print("Не удалось скопировать файл! Нет такого файла! \n")

def rem_file():
    if not dir_name:
        print("\n")
        print("Необходимо указать имя файла вторым параметром \n")
        return
    print('Вы уверены, что хотите удалить файл {} ? \n'.format(dir_name))
    g = input("Нажмите 'Y' для подтверждения или любую клавишу для отмены \n")
    if g == 'Y':
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.remove(dir_path)
            print('Файл {} успешно удален! \n'.format(dir_name))
        except FileNotFoundError:
            print("Нет такого файла! \n")
    else:
        print("Действие отменено! \n")

def change_dir():
    if not dir_name:
        print("\n")
        print("Необходимо указать имя директории вторым параметром \n")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print("\n")
        print('Переход в директорию {} успешно завершен \n!'.format(dir_path))
    except FileNotFoundError:
        print("\n")
        print("Не удалось перейти! Такой директории не существует \n")

def list_dir():
    print("\n")
    print('Текущая директория: {} \n'.format(os.getcwd()))

def ping():
    print("\n")
    print("pong \n")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": rem_file,
    "cd": change_dir,
    "ls": list_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("\n")
        print("Задан неверный ключ \n")
        
print("Укажите ключ help для получения справки \n")
