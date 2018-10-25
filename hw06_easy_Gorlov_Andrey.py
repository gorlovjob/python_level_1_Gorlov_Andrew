
__author__ = 'Горлов Андрей Гарриевич'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

print('Задача №1')

class triangle:
    def __init__(self, point1, point2, point3):
        # Вводим координаты точек вершин треугольника
        # с помощью двух чисел списка
        self.point1 = [float(point1[0]), float(point1[1])]
        self.point2 = [float(point2[0]), float(point2[1])]
        self.point3 = [float(point3[0]), float(point3[1])]

        # Высчитываем сразу стороны треугольника (для удобства округляю до сотых с помощью round)
        self.a12 = round(((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2)**(1/2), 2)
        self.a13 = round(((self.point3[0] - self.point1[0])**2 + (self.point3[1] - self.point1[1])**2)**(1/2), 2)
        self.a23 = round(((self.point3[0] - self.point2[0])**2 + (self.point3[1] - self.point2[1])**2)**(1/2), 2)

    @property
    def perimeter(self):
        per = self.a12 + self.a13 + self.a23
        return per

    @property
    def area(self):
        # Площадь высчитываем по формуле Герона. p - полупериметр (для удобства округляю до сотых с помощью round)
        p = (self.a12 + self.a13 + self.a23) / 2
        S = round((p * (p - self.a12) * (p - self.a13) * (p - self.a23))**(1/2), 2)
        return S

    @property
    def height(self):
        # Высоту находим на основе формулы площади треугольника (для удобства округляю до сотых с помощью round)
        h = round(((2 * self.area) / self.a12), 2)
        return h

triangle1 = triangle([2,3], [-3,1], [-4,-2])

print('Координаты вершин треугольника: ',triangle1.point1, triangle1.point2, triangle1.point3)
print('Стороны треугольника: ',triangle1.a12, triangle1.a13, triangle1.a23)
print('Периметр треугольника: ',triangle1.perimeter)
print('Площадь треугольника: ',triangle1.area)
print('Высота треугольника: ',triangle1.height)

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

print('Задача №2')

class trapezium:
    def __init__(self, point1, point2, point3, point4):
        # Вводим координаты точек вершин трапеции
        # с помощью двух чисел списка
        self.point1 = [float(point1[0]), float(point1[1])]
        self.point2 = [float(point2[0]), float(point2[1])]
        self.point3 = [float(point3[0]), float(point3[1])]
        self.point4 = [float(point4[0]), float(point4[1])]

        # Высчитываем сразу стороны трапеции (для удобства округляю до сотых с помощью round)
        self.a12 = round(((self.point2[0] - self.point1[0])**2 + (self.point2[1] - self.point1[1])**2)**(1/2), 2)
        self.a23 = round(((self.point3[0] - self.point2[0])**2 + (self.point3[1] - self.point2[1])**2)**(1/2), 2)
        self.a34 = round(((self.point4[0] - self.point3[0])**2 + (self.point4[1] - self.point3[1])**2)**(1/2), 2)
        self.a14 = round(((self.point4[0] - self.point1[0])**2 + (self.point4[1] - self.point1[1])**2)**(1/2), 2)

        # Высчитаем заодно и диогонали трапеции (для удобства округляю до сотых с помощью round)
        self.a13 = round(((self.point3[0] - self.point1[0])**2 + (self.point3[1] - self.point1[1])**2)**(1/2), 2)
        self.a24 = round(((self.point4[0] - self.point2[0])**2 + (self.point4[1] - self.point2[1])**2)**(1/2), 2)

    @property
    def is_isosceles(self):
        # Проверка на равнобокость с помощью свойства о равности диогоналей
        if self.a13 == self.a24:
            answer = 'Трапеция является равнобокой!'
        else:
            answer = 'Трапеция НЕ равнобокая!'
        return answer

    @property
    def perimeter(self):
        per = round(self.a12 + self.a23 + self.a34 + self.a14, 2)
        return per

    @property
    def area(self):
        # Площадь высчитываем по формуле через четыре стороны
        # (для удобства округляю до сотых с помощью round).
        # Формулу разбил на части, чтобы не запутаться
        a = (self.a14 + self.a23) / 2
        b = (self.a14 - self.a23)**2 + self.a12**2 - self.a34**2
        c = 2 * (self.a14 - self.a23)
        d = self.a12**2 - (b / c)**2
        S = round(( a * d**(1/2)), 2)
        return S

trapezium1 = trapezium([-6,0], [-2,2], [2,2], [6,0])

print('Координаты вершин трапеции: ',trapezium1.point1, trapezium1.point2, trapezium1.point3, trapezium1.point4)
print('Стороны трапеции: ',trapezium1.a12, trapezium1.a23, trapezium1.a34, trapezium1.a14)
print('Результат проверки трапеции на равнобокость:',trapezium1.is_isosceles)
print('Периметр трапеции: ',trapezium1.perimeter)
print('Площадь трапеции: ',trapezium1.area)

input('Нажмите Enter, чтобы продолжить: ')
print('===========================================')
