"""
Трохи модифікував, щоб закінчувався по введеню sum , бо так логічніше.
"""

numbers_sum = 0
print('Ви можете прахувати всі послідовно введені чісла. Для підрахунку введіть sum')
while True:
    number = input("Введіть число: ")
    if number == "sum":
        break
    numbers_sum += int(number)

print("Сума введених чисел чисел:", numbers_sum)
