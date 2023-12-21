"""
згенерувати квадратну матрицю 'око' - всі значення 0-лі а по діагоналі 1ки

"""
def eye_matrix(size):
  # Створює матрицю з 0 розміром `size` x `size`
  matrix = []
  for i in range(size):
    row = []
    for j in range(size):
      row.append(0)
    matrix.append(row)
  # Заповнює діагональ одиницями
  for i in range(size):
    for j in range(size):
      if i == j:
        matrix[i][j] = 1
  return matrix

assert eye_matrix(3) == [[1, 0, 0], 
                         [0, 1, 0],
                         [0, 0, 1]]
assert eye_matrix(4) == [[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]

"""
Написати програму яка знаходить друге найменше число в списку. 
1) з використанням методів списків, та вбудованих функцій
2) без використання методів списків
"""

def second_smallest_0(array):
    """
    Знаходить друге найменьше унікальне число в списку.
    Аргументи:
        array: список чисел.
    Повертає:
        Друге унікальне найменьше число.
    """
    array = sorted(set(array))
    return array[1]

assert second_smallest_0([1, 1, 2, 2, 3]) == 2
assert second_smallest_0([-1, 10, -2, 2]) == -1
def second_smallest_1(array):
  second_smallest = []
  for i in array:
    if i not in second_smallest:
      if second_smallest and i < second_smallest[-1]:
        second_smallest[-1], i = i, second_smallest[-1]
      else:
        second_smallest.append(i)
  return second_smallest[1]

assert second_smallest_1([1, 1, 2, 2, 3]) == 2
assert second_smallest_1([-1, 10, -2, 2]) == -2
"""
написати програму яка перетворює список на строку
1) без методів строк 
2) з =)
"""

def list_to_string(array):
        """
        Перетворює список на строку.
        Аргументи:
          array: Список, який потрібно перетворити.
        Повертає:
          Строку, утворену з елементів списку.
        """
        string = ""
        for e in array:
            string += str(e)
        return string

assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"
def list_to_string_1(array):
    string = ""
    for element in array:
        if isinstance(element, str):
            string += element
        else:
            string += f"{element}"

    return string
assert list_to_string_1(["l", "i", "s", "t"]) == "list"
assert list_to_string_1(["l", "i", "s", "t", 5, 1.1]) == "list51.1"
"""
написати програму, яка приймає два списки та видає новий список зі спільними унікальними елементами
"""

def list_intercection(list1, list2):
  """
  Знаходить спільні унікальні елементи двох списків.
  Аргументи:
    list1: Перший список.
    list2: Другий список.
  Повертає:
    Новий список зі спільними унікальними елементами якщо вони є.
    None якщо спільних єлементів немає.
  """
  set1 = set(list1)
  set2 = set(list2)
  intersection = set1 & set2
  new_list = list(intersection)
  if new_list:
    return new_list
  else:
    return None

assert list_intercection([1, 1, 1, 2], [1, 3, 4]) == [1, ]
assert list_intercection(["foo", 1, "bar"], [2, 3, 4]) == None
assert list_intercection(["foo", 1, "bar"], []) == None
assert list_intercection(["foo", 1, "bar"], [4, "foo", 7]) == ["foo", ]

"""
Із списку, цілі числа з'єднати в одне число
варіант із зірочкою - заборонено переведення із строкового в числовий тип і навпаки
"""

def join_ints(my_list):
  int_list = []
  for i in my_list:
    if isinstance(i, int):
      int_list.append(i)
  ints = ""
  for e in int_list:
    ints += str(e)
  return int(ints)

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143

"""
Реалізувати метод строк split() самостійнр
"""
def my_split(s, sep=" "):
  """
  Функція split()
  Аргументи:
    s: Строка.
    sep: Символ роздільника.
  """
  result = []
  i = 0
  while i < len(s):
    if s[i] != sep:
      start = i
      while i < len(s) and s[i] != sep:
        i += 1
      result.append(s[start:i])
    i += 1
  if s[-1] == sep:
    result.append("")
  return result


assert my_split("Karamba", "a") == ['K', 'r', 'mb', '']

"""
Бонусне завдання
Взяти програму повернення матриці з лекції, та зробити на її основі фунцію, що повертає матрицю, на довільне(кратне 90)
число градусув. Асерти на вас.


Спробував зробити через зміну порядку символів в кортежах.
"""
def rotate_matrix(matrix, degree):
    """
    Функція перевертає матрицю на задану кількість градусів.
    Функція перевертає на кратну 90 кількість градусів, і має перевірку.
    Аргументи:
        matrix: Матриця для перевороту.
        degrees: Кількість градусів кратна 90
    Повертає:
        Перевертуну матрицю на задану кількість градусів
    """
    if degree == 90:
        rotate = range(len(matrix) - 1, -1, -1)
    elif degree == 180:
        rotate = range(len(matrix) - 1, -1, -1)
        matrix = rotate_matrix(matrix, 90)
    elif degree == 270:
        rotate = range(len(matrix) - 1, -1 , -1)
        matrix = rotate_matrix(matrix, 180)
    else:
        return print('Значення degree повинно бути кратне 90, 180 або 270')
    new_matrix = []
    for i in range(len(matrix)):
        new_line = []
        for j in rotate:
            new_line.append(matrix[j][i])
        new_matrix.append(new_line)
    return new_matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

assert rotate_matrix(matrix, 90) == [[7, 4, 1],
                                            [8, 5, 2],
                                            [9, 6, 3]]
assert rotate_matrix(matrix, 180) == [[9, 8, 7],
                                             [6, 5, 4],
                                             [3, 2, 1]]
assert rotate_matrix(matrix, 270) == [[3, 6, 9],
                                             [2, 5, 8],
                                             [1, 4, 7]]