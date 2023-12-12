number = int(input("Введіть число від 1 до 100: "))

while 0 == number <= 101:
  print("Число має бути в діапазоні від 1 до 100.")
  number = int(input("Введіть число від 1 до 100: "))

for i in range(1, 11):
  print(f"{number} * {i} = {number * i}")
