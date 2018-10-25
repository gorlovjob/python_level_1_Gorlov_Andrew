
__author__ = 'Горлов Андрей Гарриевич'


""" OpenWeatherMap (экспорт)
Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.
Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions
Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.
"""

import csv, json, sys, sqlite3

def read_db():
    ''' Функция делает запрос к базе данных по введенному городу.
        Если город не введен, то запрос по всем городам.'''
    name_bd = "gorlov_database.db"
    conn = sqlite3.connect(name_bd)
    cursor = conn.cursor()

    if city:
        sql = "SELECT * FROM weather WHERE city=?"
        cursor.execute(sql, [(city)])
    else:
        sql = "SELECT * FROM weather"
        cursor.execute(sql)
    return cursor.fetchall()

def csv_file():
    ''' Функция экспортирует данные в csv файл '''
    print('Выгружаются данные... \n')
    data = read_db()
    if city != None:
        path = '{}.csv'.format(city)
    else:
        path = '{}.csv'.format('filename')

    if data:    
        with open(path, 'w') as csv_f:
            go = csv.writer(csv_f)
            for line in data:
                go.writerow(line)
        print('Данные успешно экспортированы в файл {}'.format(path))
    else:
        print('Данных по городу не найдено!')

def json_file():
    ''' Функция экспортирует данные в json файл '''
    data = read_db()
    if city != None:
        path = '{}.json'.format(city)
    else:
        path = '{}.json'.format('filename')

    if data:
        with open(path, 'w') as json_f:
            json.dump(data, json_f)
        print('Данные успешно экспортированы в файл {}'.format(path))
    else:
        print('Данных по городу не найдено!')

def html_file():
    ''' Функция экспортирует данные в html файл '''
    data = read_db()
    if city != None:
        path = '{}.html'.format(city)
    else:
        path = '{}.html'.format('filename')

    if data:
        with open(path, 'w') as html_f:
            for line in data:
                html_f.write(str(line))
        print('Данные успешно экспортированы в файл {}'.format(path))
    else:
        print('Данных по городу не найдено!')
    
# В зависимости от введенного ключа, запускаем функцию
do = {
    "--csv": csv_file,
    "--json": json_file,
    "--html": html_file
}

# Проверяем первый введенный аргумент
try:
    key = sys.argv[1]
except IndexError:
    key = None

# Проверяем второй введенный аргумент
try:
    city = sys.argv[2]
except IndexError:
    city = None

# Проверяем - есть ли введенный ключ в списке соответствия функциям
if key:
    if do.get(key):
        do[key]()
    else:
        print("\n")
        print("Задан неверный ключ \n")
