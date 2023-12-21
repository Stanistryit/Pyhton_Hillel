#
# def rotate_matrix(matrix, degrees):
#     """
#     Функція перевертає матрицю на задану кількість градусів.
#     Функція перевертає на кратну 90 кількість градусів, і має перевірку.
#     Аргументи:
#         matrix: Матриця для перевороту.
#         degrees: Кількість градусів кратна 90
#     Повертає:
#         Перевертуну матрицю на задану кількість градусів
#     """
#     if degrees % 90 != 0 or degrees not in [90, 180, 270]:
#         return print('Введена кількість градусів не кратна 90')
#     rotations = degrees // 90
#     for _ in range(rotations):
#         num_rows = len(matrix)
#         num_cols = len(matrix[0])
#         rotated_matrix = []
#         for _ in range(num_cols):
#             row = [0] * num_rows
#             rotated_matrix.append(row)
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 rotated_matrix[j][len(matrix) - 1 - i] = matrix[i][j]
#         matrix = rotated_matrix
#     return matrix
def rotate_matrix(matrix, degree):
    if degree == 90:
        rotate = range(len(matrix)-1, -1, -1)
    elif degree == 180:
        rotate = range(len(matrix) - 1, -1, -1)
        matrix = rotate_matrix(matrix, 90)
    elif degree == 270:
        rotate = range(len(matrix))
        matrix = rotate_matrix(matrix, 180)
    else:
        return print('Значення degree повинно бути кратне 90, 180 або 270')
    new_matrix = []
    for i in range(len(matrix)):
        new_line = []
        for j in rotate:
            new_line.append(matrix[j][i])
        new_matrix.append(new_line)
    if new_matrix:
        return new_matrix
    else:
        print("Помилка!")
# mat1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# mat3 = []
# for i in range(len(mat1)):
#     new_line = []
#     for j in range(len(mat1)-1, -1, -1):
#         new_line.append(mat1[j][i])
#     mat3.append(new_line)
# print(mat3)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix, 271))
# assert rotate_matrix(matrix, 90) == [[7, 4, 1],
#                                             [8, 5, 2],
#                                             [9, 6, 3]]
# assert rotate_matrix(matrix, 180) == [[9, 8, 7],
#                                              [6, 5, 4],
#                                              [3, 2, 1]]
# assert rotate_matrix(matrix, 270) == [[3, 6, 9],
#                                              [2, 5, 8],
#                                              [1, 4, 7]]

