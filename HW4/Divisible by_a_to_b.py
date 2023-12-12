#Введення чисел a і b
a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))
#Перевірка, чи a менше b. Якщо так, то змінні a і b поміняються місцями
if a > b:
  a, b = b, a
#Перевірка, чи числа a і b знаходяться в діапазоні від 1 до 199
if not 0 < a < 200 or not 0 < b < 200:
  #Якщо будь-яка з умов не виконується, то виводиться повідомлення про помилку
  print("Числа a і b повинні бути в діапазоні від 1 до 199.")
else:
  #Створення списку для зберігання чисел, які діляться на задане число
  groups = []
  #Цикл для перебору чисел від a + 1 до b
  for divisor in (2, 3, 4, 5, 6):
    group = []
    for i in range(a + 1, b):
      if i % divisor == 0:
        group.append(i)
        #Якщо довжина списку досягла 10, то він виводиться на екра
        if len(group) == 10:
          print(f"Divisible by {divisor}:", ", ".join(map(str, group)))
          group = []
    if group:
      print(f"Divisible by {divisor}:", ", ".join(map(str, group[:10])))

