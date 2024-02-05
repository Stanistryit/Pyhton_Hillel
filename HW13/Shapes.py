from abc import ABC, abstractmethod
from math import sqrt
from collections.abc import Iterable

class Point():
    """
    Class to store point
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: ['Point']):
        if self.x == other.x and self.x == other.y:
            return True
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y})"

class Line():

    def __init__(self, point1:Point, point2:Point):
        self.p1 = point1
        self.p2 = point2

    def calc_slope(self):
        try:
            return (self.p1.x - self.p2.x) / (self.p1.y - self.p2.y)
        except ZeroDivisionError:
            return 1

    def calc_lenth(self):
        return sqrt((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)

    def is_on_line(self, p3):
        if self.calc_slope() == Line(self.p1, p3).calc_slope():
            return True
        else:
            return False

class Shape(ABC):
    __name = "shape"

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_perim(self):
        pass

    @abstractmethod
    def calc_squeare(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def __repr__(self):
        print(f"{self.__name} have "
              +"perim {self.calc_perim()} and squeare {self.calc_squeare()}")

class Polygon(Shape):

    def __init__(self, *args: Iterable['Point']):
        """
        має вміти отримувати від конструктора довільну кількість точок більшу або рівну 3-м
        розрзаховувати довжину сторін і зберігати їх в собі, щоб потім використати в методах
        """
        points = args
        points_end = *args[1:], args[0]
        edges = []
        slopes = []
        for start, end in zip(points, points_end):
            line = Line(start, end)
            edges.append(line.calc_lenth())
            slopes.append(line.calc_slope())
        self.edges = edges
        self.slopes = slopes


    def calc_perim(self):
        self.perimeter = sum(self.edges)
        return self.perimeter


    def calc_squeare(self):
        pass


    def validate(self):
        pass

class Triangle(Polygon):

    def __init__(self, *args: Iterable['Point']):
        super().__init__(*args)
        # Валідація трикутника
        Triangle.validate(self.edges)

    def calc_squeare(self):
        # Використовуємо формулу Герона для обчислення площі трикутника(Я НЕНАВИДЖУ ГЕОМЕТРІЮ!)
        s = self.calc_perim() / 2
        area = sqrt(s * (s - self.edges[0]) * (s - self.edges[1]) * (s - self.edges[2]))
        return area

    @staticmethod #task4
    def validate(edges):
        # Додаємо валідацію для трикутника
        if len(edges) != 3:
            raise ValueError("Трикутник повинен мати рівно 3 точки.")
        if edges[0] + edges[1] <= edges[2] or \
                edges[0] + edges[2] <= edges[1] or \
                edges[1] + edges[2] <= edges[0]:
            raise ValueError("Недійсний трикутник. Сума будь-яких двох сторін має бути більшою за третю.")


class Rectangle(Polygon):
    figure_name = "rectangle"

    def __init__(self, *args):
        super().__init__(*args)

    def calc_perim(self):
        self.perimeter = sum(self.edges)
        return self.perimeter

    def calc_square(self):
        self.square = self.edges[0] * self.edges[1]
        return self.square

    @classmethod
    def diagonal_rectangle(cls, diagonal_point1: 'Point', diagonal_point2: 'Point'):
        """
        Створює прямокутник за допомогою двох точок, які є протилежними кутами діагоналі.
        Нагадаю, я ненавиджу геометрію!
        """
        # Знаходимо інші дві вершини прямокутника за допомогою переданих діагональних точок
        x1, y1 = diagonal_point1.x, diagonal_point1.y
        x2, y2 = diagonal_point2.x, diagonal_point2.y

        # Знаходимо координати інших двох точок, використовуючи діагональні точки
        # Точка 3
        x3 = x1
        y3 = y2
        # Точка 4
        x4 = x2
        y4 = y1

        # Створюємо прямокутник і повертаємо його екземпляр
        return cls(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4))

    @staticmethod #task 4
    def validate(edges):
        # Додаємо валідацію для прямокутника
        if len(edges) != 4:
            raise ValueError("Прямокутник повинен мати рівно 4 точки.")
        # В прямокутнику протилежні сторони повинні мати однакову довжину
        diagonal1 = Line(edges[0], edges[2]).calc_lenth()
        diagonal2 = Line(edges[1], edges[3]).calc_lenth()
        if diagonal1 != diagonal2:
            raise ValueError("Недійсний прямокутник. Діагоналі не мають однакову довжину.")


if __name__ == "__main__":
    r1 = Rectangle(Point(1,1), Point(1,3), Point(4,3), Point(4,1))
    print(r1.calc_perim())
    print(r1.calc_square())

    #task 2
    t1 = Triangle(Point(1, 1), Point(1, 4), Point(5, 1))
    print(t1.calc_perim())
    print(t1.calc_squeare())

    #task 3
    # Створення прямокутника за допомогою двох точок(діагоналі)
    r2 = Rectangle.diagonal_rectangle(Point(1, 1), Point(4, 3))
    print(r2.calc_perim())
    print(r2.calc_square())