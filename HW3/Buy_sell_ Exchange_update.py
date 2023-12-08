# Введення змінних
currencies = []
for currency, buy_price in [
    ("USD", 37.75),
    ("EUR", 40),
    ("PL", 9),
    ("BTC", 1),
    ("CAD", 10),
]:
    sell_price = buy_price * 1.05
    currencies.append((currency, buy_price, sell_price))

# Константи
MULTIPLE = 50

# Ідентифікація та привітання з клієнтом
print("Вас вітає обмін валют!")
name = input("Введіть ваше ім'я: ")

# Таблиця курсу валют
print(f"{name}, курс обміну валют на сьогодні:")
print(f"| Купівля | {'Валюта':^7} | {'Продаж':^7} |")
print("|---------|---------|---------|")
for currency, buy_price, sell_price in currencies:
    print(f"| {buy_price:^7.2f} | {currency:^7} | {sell_price:^7.2f} |")
print("|---------|---------|---------|")

# Вибір валюти
print(f'{name}, яку валюту бажаєте купити/продати?')
print("Доступні валюти: " + ', '.join(currency_info[0] for currency_info in currencies))
while True:
    user_input = input("Введіть потрібну валюту: ").upper()
    found_currency = None
    for currency_info in currencies:
        if user_input == currency_info[0]:
            found_currency = currency_info
            break

    if found_currency is not None:
        #вибір операції
        print("Яку операцію ви хочете виконати?")
        print("1. Купівля")
        print("2. Продаж")
        operation = str(input("Введіть назву операції: "))
        while operation not in (1, 2):
            print("Ви зробили не коректний вибір!")
            operation = str(input("Введіть назву операції: "))
        if operation == 'Купівля':
            buy_price = found_currency[1]
            amount_uah = int(input('Введіть кількість гривні: '))
            result = amount_uah // buy_price #кількість валюти
            change = amount_uah % buy_price #решта
            print(f"Ви отримаєте {result:.0f} {found_currency[0]}, решта {change:.2f} грн.")
            # обробка результату
            #Якщо сума результату меньша за MULTIPLE
            if result < MULTIPLE:
                difToMul = abs(result - MULTIPLE)
                add_uah = (difToMul * buy_price) - change
                new_result = result + difToMul
                print(f"Ви можете додати {add_uah:.2f}грн. щоб отримати {new_result:.0f} {found_currency[0]}")
                # Даємо вибір кліенту
                choise = input(f'Округлити суму {found_currency[0]}, Так | Ні: ')
                while choise not in ("Так", "Ні"):
                    print("Ви зробили не коректний вибір!")
                    choise = input("Так | Ні: ")
                if choise == 'Так':
                    extra_charge = int(input('Введіть суму доплати:'))
                    #Перевірка введеної суми
                    while extra_charge < add_uah:
                        print(f'Треба внести не меньше {add_uah}грн.')
                        extra_charge = int(input('Введіть суму доплати:'))
                    extra_change = extra_charge - add_uah
                    print(f'Ви отримали {new_result:.0f} {found_currency[0]}, ваша решта {extra_change:.2f} грн.')
                    break
                elif choise == 'Ні':
                    print(f"Ви отримали {result:.0f} {found_currency[0]}, і {change:.2f} грн. решти!")
            #Якщо більша за MULTIPLE
            else:
                multiple_amount = result / MULTIPLE # кратність
                multiple_count = round((multiple_amount % 1), 2) #різниця кратності
                #якщо близько до MULTIPLE по математичному округленню (0.5=1)
                if multiple_count >= 0.50:
                    difToMul = abs((multiple_count * MULTIPLE) - MULTIPLE)
                    add_uah = (difToMul * buy_price) - change
                    new_result = result + difToMul
                    print(f"Ви можете додати {add_uah:.2f}грн. щоб отримати {new_result:.0f} {found_currency[0]}")
                #Даємо вибір кліенту
                    choise = input(f'Округлити суму {found_currency[0]}, Так | Ні: ')
                #Перевірка вибор
                    while choise not in ("Так", "Ні"):
                        print("Ви зробили не коректний вибір!")
                        choise = input("Так | Ні: ")
                    if choise == 'Так':
                        extra_charge = int(input('Введіть суму доплати:'))
                        #Перевірка введеної суми
                        while extra_charge < add_uah:
                            print(f'Треба внести не меньше {add_uah}грн.')
                            extra_charge = int(input('Введіть суму доплати:'))
                        extra_change = extra_charge - add_uah
                        print(f'Ви отримали {new_result:.0f}{found_currency[0]}, ваша решта {extra_change:.2f}грн.')
                        break
                    elif choise == 'Ні':
                        print(f"Ви отримали {result:.0f} {found_currency[0]}, і {change:.2f} грн. решти!")
                        break
                # якщо далеко до MULTIPLE по математичному округленню (0.5=1, 0.4=0)
                elif multiple_count <= 0.50:
                    difToMul = abs((multiple_count * MULTIPLE) - MULTIPLE)
                    new_result = result + difToMul
                    extra_change = (difToMul * buy_price) + change
                    print(f'Бажаєте округлити суму {found_currency[0]} до {new_result}{found_currency[0]} і отримати {extra_change} грн. решти?')
                    choise = input("Так | Ні: ")
                    #Перевірка введення
                    while choise not in ("Так", "Ні"):
                        print("Ви зробили не коректний вибір!")
                        choise = input("Так | Ні: ")
                    if choise == 'Так':
                        print(f"Ви отримали {new_result:.0f} {found_currency[0]}, і {extra_change:.2f} грн. решти!")
                        break
                    elif choise == 'Ні':
                        print(f"Ви отримали {result:.0f} {found_currency[0]}, і {change:.2f} грн. решти!")
                        break
        #Продаж валюти
        elif operation == 'Продаж':
            sell_price = found_currency[2]
            amount_currency = int(input(f'Введіть кількість {found_currency[0]}: '))
            result = amount_currency * sell_price
            print(f"Ви отримали {result:.2f} грн.")
            break
        else:
            print("Невірна валюта. Спробуйте ще раз.")
