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
print(f'{name}, яку валюту бажаєте придбати?')
print("Доступні валюти: " + ', '.join(currency_info[0] for currency_info in currencies))
while True:
    user_input = input("Введіть потрібну валюту: ").upper()
    found_currency = None
    for currency_info in currencies:
        if user_input == currency_info[0]:
            found_currency = currency_info
            break

    if found_currency is not None:
        buy_price = found_currency[1]
        amount_uah = int(input('Введіть кількість гривні: '))
        result = amount_uah // buy_price
        change = amount_uah % buy_price

        # Результат обміну
        print(f'Сума отриманої валюти = {result:^1} {found_currency[0]}')
        print(f"Ваша решта = {change:>12} UAH")
        break
    else:
        print("Невірна валюта. Спробуйте ще раз.")
