"""
Згенерувати 100 випадкових цілих чисел, записати їх в csv(10 стовбчиків) та json(10 строк по 10 чисел)
Зчитати данні зі двох істочників. Підрахувати середне за кожною строкою з кожного файлу. Вивести результат в таблику
 на екран типу:

 lineNum json_ave csv_ave
       0   10        11
       1   12        44
"""
import csv
import json
import random


def generate_and_write_csv(file_path):
    with open(file_path, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        for _ in range(100):
            row = [random.randint(1, 100) for _ in range(10)]
            csv_writer.writerow(row)


def generate_and_write_json(file_path):
    with open(file_path, mode="w") as json_file:
        json_data = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]
        json.dump(json_data, json_file)


def calculate_averages(file_path, file_type):
    averages = []
    with open(file_path, mode="r") as data_file:
        if file_type == "csv":
            data_reader = csv.reader(data_file)
        elif file_type == "json":
            data = json.load(data_file)
            data_reader = iter(data)
        else:
            raise ValueError("Не вірний тип файлу. Підхоить лише 'csv' або 'json'.")

        for line_num, row in enumerate(data_reader):
            row = [int(x) for x in row]
            average = round(sum(row) / len(row))
            averages.append((line_num, average))

    return averages


def display_table(averages_json, averages_csv):
    print(f"{'lineNum':<8}{'json_ave':<10}{'csv_ave':<10}")
    for line_num in range(10):
        json_average = next(average for num, average in averages_json if num == line_num)
        csv_average = next(average for num, average in averages_csv if num == line_num)
        print(f'{line_num:<8}{json_average:<10}{csv_average:<10}')


#Генерація та запис випадкових чисел у CSV та JSON
csv_file_path = "random_numbers.csv"
json_file_path = "random_numbers.json"
generate_and_write_csv(csv_file_path)
generate_and_write_json(json_file_path)

# Зчитування та обчислення середнього значення за кожним рядком для CSV та JSON
averages_json = calculate_averages(json_file_path, "json")
averages_csv = calculate_averages(csv_file_path, "csv")

# Виведення результату у табличному вигляді
display_table(averages_json, averages_csv)
