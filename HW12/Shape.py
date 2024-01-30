"""
Реалізував клас через точки на координатній прямій.

Я ненавиджу геометрію, але шкільник курс був вимушений повторювати :)

Хотів додати візуалізацію цих фігур, але документація до matplotlib виявилась доволі обширною.
Пробував це робити для себе, вийшло не так гарно як хотілось. Тому її прибрав.

"""

import math

class Shape:
    """Базовий клас для геометричних фігур"""

    def __init__(self, *args):
        """
        Ініціалізація класу з введеними аргументами.

        Parameters:
            args (tuple): Кортеж координат вершин фігури.
        """
        self.args = args

    def calculate_side_lengths(self):
        """
        Обчислення довжин сторін фігури.

        Returns:
            list: Список довжин сторін.
        """
        return [math.sqrt((self.args[i][0] - self.args[j][0]) ** 2 + (self.args[i][1] - self.args[j][1]) ** 2)
                for i in range(len(self.args)) for j in range(i + 1, len(self.args))]

    def perimeter(self):
        """
        Обчислення периметру фігури.

        Returns:
            float: Значення периметру.
        """
        if len(self.args) == 2:  # Коло
            center, point_on_circle = self.args
            radius = math.sqrt((point_on_circle[0] - center[0]) ** 2 + (point_on_circle[1] - center[1]) ** 2)
            return 2 * math.pi * radius
        elif len(self.args) == 3:  # Трикутник
            return sum(self.calculate_side_lengths())
        elif len(self.args) == 4:  # Прямокутник
            side_lengths = self.calculate_side_lengths()
            return 2 * (side_lengths[0] + side_lengths[1])

    def area(self):
        """
        Обчислення площі фігури.

        Returns:
            float: Значення площі.
        """
        if len(self.args) == 2:  # Коло
            center, point_on_circle = self.args
            radius = math.sqrt((point_on_circle[0] - center[0]) ** 2 + (point_on_circle[1] - center[1]) ** 2)
            return math.pi * radius ** 2
        elif len(self.args) == 3:  # Трикутник
            s = sum(self.calculate_side_lengths()) / 2
            return math.sqrt(s * (s - self.calculate_side_lengths()[0]) *
                             (s - self.calculate_side_lengths()[1]) *
                             (s - self.calculate_side_lengths()[2]))
        elif len(self.args) == 4:  # Прямокутник
            side_lengths = self.calculate_side_lengths()
            return side_lengths[0] * side_lengths[1]

    def validate(self):
        """
        Перевірка правильності введених аргументів для фігури.

        Returns:
            bool: Результат валідації.
        """
        if len(self.args) == 2:  # Коло
            return len(self.args[0]) == 2 and len(self.args[1]) == 2
        elif len(self.args) == 3:  # Трикутник
            return all(len(vertex) == 2 for vertex in self.args)
        elif len(self.args) == 4:  # Прямокутник
            return all(len(vertex) == 2 for vertex in self.args)


class Rectangle(Shape):
    """Клас для представлення прямокутника."""

    def __init__(self, *args):
        """
        Ініціалізація класу для прямокутника.

        Parameters:
            args (tuple): Кортеж координат вершин прямокутника.
        """
        super().__init__(*args)

    def build(self):
        """
        Побудова та виведення інформації про прямокутник.
        """
        if len(self.args) == 4 and self.validate():
            x_values, y_values = zip(*self.args)
            min_x, max_x = min(x_values), max(x_values)
            min_y, max_y = min(y_values), max(y_values)

            print("Будуємо прямокутник з вершинами:", self.args)
            print("Ширина: {}, Висота: {}".format(max_x - min_x, max_y - min_y))
            print("Периметр:", self.perimeter())
            print("Площа:", self.area())
        else:
            print("Не вірна кількість аргументів або невірні вершини для прямокутника")


class Circle(Shape):
    """Клас для представлення кола."""

    def __init__(self, *args):
        """
        Ініціалізація класу для кола.

        Parameters:
            args (tuple): Кортеж координат центру та точки на колі.
        """
        super().__init__(*args)

    def build(self):
        """
        Побудова та виведення інформації про коло.
        """
        if len(self.args) == 2 and self.validate():
            center, point_on_circle = self.args
            radius = math.sqrt((point_on_circle[0] - center[0]) ** 2 + (point_on_circle[1] - center[1]) ** 2)

            print("Будуємо коло з центром у точці {} і точкою на колі {}".format(center, point_on_circle))
            print("Радіус:", radius)
            print("Периметр:", self.perimeter())
            print("Площа:", self.area())
        else:
            print("Не вірна кількість аргументів або невірні вершини для кола")


class Triangle(Shape):
    """Клас для представлення трикутника."""

    def __init__(self, *args):
        """
        Ініціалізація класу для трикутника.

        Parameters:
            args (tuple): Кортеж координат вершин трикутника.
        """
        super().__init__(*args)

    def build(self):
        """
        Побудова та виведення інформації про трикутник.
        """
        if len(self.args) == 3 and self.validate():
            print("Будуємо трикутник з вершинами:", self.args)
            print("Периметр:", self.perimeter())
            print("Площа:", self.area())
        else:
            print("Не вірна кількість аргументів або невірні вершини для трикутника")



rectangle_instance = Rectangle((1, 1), (5, 1), (1, 4), (5, 4))
rectangle_instance.build()

circle_instance = Circle((0, 0), (1, 1))
circle_instance.build()

triangle_instance = Triangle((0, 0), (1, 0), (0, 1))
triangle_instance.build()
