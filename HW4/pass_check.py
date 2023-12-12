import string

def secure_password(password):

  # Перевіряємо довжину пароля
  if len(password) < 12:
    print("Пароль повинен бути не менше 12 символів.")
    return False

  # Перевіряємо наявність символів в різних регістрах
  upper_letters = set(password).intersection(string.ascii_uppercase)
  lower_letters = set(password).intersection(string.ascii_lowercase)
  if not upper_letters:
    print("У паролі повинен бути хоча б один символ у верхньому регістрі.")
    return False
  if not lower_letters:
    print("У паролі повинен бути хоча б один символ у нижньому регістрі.")
    return False

  # Перевіряємо наявність цифр
  digits = set(password).intersection(string.digits)
  if not digits:
    print("У паролі повинен бути хоча б одна цифра.")
    return False

  # Перевіряємо наявність спецсимволів
  special_symbols = set(password).intersection(string.punctuation)
  if not special_symbols:
    print("У паролі повинен бути хоча б один спецсимвол.")
    return False

  return True

password = input('Введіть пароль: ')

while not secure_password(password):
  password = input('Введіть пароль: ')

if secure_password(password):
  print("Пароль безпечний.")
