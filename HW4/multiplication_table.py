number = int(input("Введіть число від 1 до 100: "))

while number < 1 or number > 100:
  print("Число має бути в діапазоні від 1 до 100.")
  number = int(input("Введіть число від 1 до 100: "))

for i in range(1, 10):
  print(f"{number} * {i} = {number * i}")
