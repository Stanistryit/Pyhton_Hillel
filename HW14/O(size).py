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



def eye_matrix_v2(size):
    # Використання генератора для створення рядків матриці
    for x in range(size):
        yield [1 if x == y else 0 for y in range(size)]


def test_eye_matrix_v2(size, expected_matrix):
    gen = eye_matrix_v2(size)
    for expected_row in expected_matrix:
        assert next(gen) == expected_row
    try:
        next(gen)
        assert False
    except StopIteration:
        pass

# Тестування функції
test_eye_matrix_v2(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
test_eye_matrix_v2(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])



