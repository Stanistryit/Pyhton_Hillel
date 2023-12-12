a = input("Введіть число a: ")
b = input("Введіть число b: ")

while not a.isdigit() or not b.isdigit():
  print("Ви ввели не ціле число. Спробуйте ще раз.")
  a = input("Введіть число a: ")
  b = input("Введіть число b: ")

a = int(a)
b = int(b)

if a > b:
  a, b = b, a

for i in range(a + 1, b):
  print(i)