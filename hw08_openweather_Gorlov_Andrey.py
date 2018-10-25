
__author__ = 'Горлов Андрей Гарриевич'


""" 
== OpenWeatherMap ==
OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.
Необходимо решить следующие задачи:
== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)
        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up
        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in
        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"
        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a
        http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a6db101013c120aa9c28abeb272396df
    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a
    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    
== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):
    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных
2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))
3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.
При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.
При работе с XML-файлами:
Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>
Чтобы работать с пространствами имен удобно пользоваться такими функциями:
    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''
    tree = ET.parse(f)
    root = tree.getroot()
    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}
    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...
"""
	
import sqlite3, requests, json, datetime, sys

def get_appid():
    ''' Данная функция получает appid из указанного файла '''
    file = open('hw08_app.id_Gorlov_Andrey.py', 'r')
    
    num_appid = file.read()
    file.close()
    
    return num_appid

def get_city(city):
    ''' Данная функция принимает название города и получает его ID из файла городов,
        выводит сообщение, если город не найден '''
    with open('city.list.json', 'r', encoding='utf-8') as line:
        list_city = []
        dict = json.load(line)
        
        for i in dict:
            if i['name'] == city:
                list_city = i
                
    if list_city == []:
        print('Город не найден')
        sys.exit()
    else:
        pass
    
    return list_city['id']

def create_bd(name_bd):
    ''' Функция принимает имя базы данных и проверяет наличие
        такой базы данных. Если ее нет - создает ее'''
    try:
        print('Создадим базу данных с именем: {}'.format(name_bd))
        conn = sqlite3.connect(name_bd)
        cursor = conn.cursor()
             
        cursor.execute("""CREATE TABLE weather
                            (id_city INTEGER PRIMARY KEY, city VARCHAR(255), date DATE,
                            temperature INTEGER, id_weather INTEGER)
                        """)
        print('Создание таблицы завершено!')
        
    except sqlite3.OperationalError:
        print('База данных уже существует!!!')

def input_bd(data_city, name_bd):
    ''' Функция принимает имя базы данных и список значений.
        Полученные значения записывает в базу, а если такие
        значения уже есть - обновляет данные температуры'''
    conn = sqlite3.connect(name_bd)
    cursor = conn.cursor()
    
    ins = (data_city['id'], data_city['name'], now.strftime("%d-%m-%Y %H:%M"), int(data_city['main']['temp']), int(data_city['weather'][0]['id']))
    print(ins)
    
    try:
        cursor.execute("INSERT INTO weather VALUES (?,?,?,?,?)", ins)
    except sqlite3.IntegrityError:
        print('По данному городу уже есть запись! Идет обновление данных...')
        update = "UPDATE weather SET temperature = {} WHERE id_city = {}".format(int(data_city['main']['temp']), data_city['id'])
        cursor.execute(update)
 
    conn.commit()
    print('Данные успешно записаны в базу данных!')

def get_weth(id_city):
    proxies = {
      'http': '80.120.86.242:46771'
    }

    s=requests.get('http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&APPID=a6db101013c120aa9c28abeb272396df'.format(id_city), proxies=proxies)
    data = s.json()
    return data

# Создаем базу данных, передавая ей имя
name_bd = "gorlov_database.db"
create_bd(name_bd)

# Получаем ID из файла
print('Мой id = {}'.format(get_appid()))

# Программа выполняется пока не прервется
while True:
    city = input('Введите город с большой буквы по-английски: ')

    # Получаем ID города по введенному названию
    id_city = get_city(city)

    # Получаем данные по ID города
    data_city = get_weth(id_city)

    # Получаем текущие дату и время
    now = datetime.datetime.now()

    # Выводим на экран полученные данные
    print('Город: {}. ID города: {}. Дата: {}. Температура: {}. ID погоды: {}.'.format(data_city['name'],
                                                                                       data_city['id'],
                                                                                       now.strftime("%d-%m-%Y %H:%M"),
                                                                                       data_city['main']['temp'],
                                                                                       data_city['weather'][0]['id']))

    # Спрашиваем у пользователя, хочет ли он ввести полученные данные в базу
    answer = input('Добавить данные в базу? (Y/N): ')

    # Вопрос будет задаваться до тех пор, пока не будет корректно введен ответ
    while answer != 'Y' and answer != 'N':
        print('Неверный ввод!')
        answer = input('Добавить данные в базу? (Y/N): ')

    # Если пользователь ответил утвердительно - заносим данные в базу. Иначе - ничего не делаем
    if answer == 'Y':
        input_bd(data_city, name_bd)
    else:
        pass

    # Спрашиваем у пользователя, хочет ли он сделать еще один вопрос
    answer2 = input('Хотите сделать еще запрос? (Y/N): ')

    # Вопрос будет задаваться до тех пор, пока не будет корректно введен ответ
    while answer2 != 'Y' and answer2 != 'N':
        answer2 = input('Хотите сделать еще запрос? (Y/N): ')

    # Если пользователь отвечает утвердительно - цикл повторяется. Иначе - прерывается и программа завершается.
    if answer2 == 'Y':
        continue
    elif answer2 == 'N':
        break
    else:
        break

print('Программа завершена!!!')
