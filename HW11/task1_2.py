import math

class VectorOperations:
    def __init__(self, vector1, vector2):
        """
        Ініціалізація класу VectorOperations.

        Parameters:
        - vector1 (list): Перший вектор.
        - vector2 (list): Другий вектор.
        """
        self.vector1 = vector1
        self.vector2 = vector2

    def add_vectors(self):
        """
        Додає два вектори.

        Returns:
        - list: Результат додавання векторів.
        """
        return [v1 + v2 for v1, v2 in zip(self.vector1, self.vector2)]

    def subtract_vectors(self):
        """
        Віднімає другий вектор від першого.

        Returns:
        - list: Результат віднімання векторів.
        """
        return [v1 - v2 for v1, v2 in zip(self.vector1, self.vector2)]

    def scalar_multiply(self, scalar):
        """
        Множить вектор на скаляр.

        Parameters:
        - scalar (float): Скаляр, на який буде помножений вектор.

        Returns:
        - list: Результат скалярного множення вектора.
        """
        return [v * scalar for v in self.vector1]

    @staticmethod
    def dot_product(vector1, vector2):
        """
        Знаходить скалярний добуток двох векторів.

        Parameters:
        - vector1 (list): Перший вектор.
        - vector2 (list): Другий вектор.

        Returns:
        - float: Скалярний добуток векторів.
        """
        return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    def vector_length(self, vector):
        """
        Підраховує довжину вектора.

        Parameters:
        - vector (list): Вектор, для якого потрібно обчислити довжину.

        Returns:
        - float: Довжина вектора.
        """
        return math.sqrt(sum(v ** 2 for v in vector))

    def compare(self):
        """
        Порівнює довжину двох векторів.

        Returns:
        - str: Повідомлення про те, який вектор довший.
        """
        length_vector1 = self.vector_length(self.vector1)
        length_vector2 = self.vector_length(self.vector2)

        if length_vector1 == length_vector2:
            return "Вектори мають однакову довжину."
        elif length_vector1 > length_vector2:
            return "Перший вектор довший."
        else:
            return "Другий вектор довший."


vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

operations = VectorOperations(vector1, vector2)

result_add = operations.add_vectors()
result_subtract = operations.subtract_vectors()
result_scalar_multiply = operations.scalar_multiply(2)
result_dot_product = VectorOperations.dot_product(vector1, vector2)

#Перевірка за допомогою ассертів (task1)
assert result_add == [5, 7, 9]
assert result_subtract == [-3, -3, -3]
assert result_scalar_multiply == [2, 4, 6]
assert result_dot_product == 32

#Порівняння довжин векторів(task2)
result_compare = operations.compare()
assert result_compare == "Другий вектор довший."

print("Тести пройдено успішно!")
