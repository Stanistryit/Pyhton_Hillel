# Цікаво = 9
# Складно = 6


# Введення змінних
UAH_USD = 37.75
UAH_EUR = 40
UAH_PL = 9
sell_precent = 1.05
usd_uah = UAH_USD * sell_precent
eur_uah = UAH_EUR * sell_precent
pl_uah = UAH_PL * sell_precent
# Ідентифікація та привітання з кліентом
print("Вас вітає обмін валют!")
name = str(input("Введіть ваше ім'я: "))
# Таблиця курсу валют
print(f"{name}, курс обміну валют на сьогодні:")
print(f"| {"Купівля":} | {"Валюта":^7} | {"Продаж":^7} |")
print("|---------|---------|---------|")
print(f"| {UAH_USD:^7.2f} | {'USD':^7} | {usd_uah:^7.2f} |")
print(f"| {UAH_EUR:^7.2f} | {'EUR':^7} | {eur_uah:^7.2f} |")
print(f"| {UAH_PL:^7.2f} | {'PL':^7} | {pl_uah:^7.2f} |")
print("|---------|---------|---------|")
# Вибір валюти
print(f'{name} яку валюту бажаете придбати?')
currency = input("USD, EUR, PL: ")
# Якщо не корекнтно ввели валюту
while currency not in ("USD", "EUR", "PL"):
    print("Ви ввели не коректну валюту.")
    currency = input("USD, EUR, PL: ")
#Обмін на долари
if currency == str("USD"):
    print(f"Ви обрали валюту USD")
    amount_uah = int(input('Введить кількість гривні: '))
    result = round(amount_uah // UAH_USD)
    change = round(amount_uah % UAH_USD)
# Обмін на євро
elif currency == str('EUR'):
    print(f"Ви обрали валюту EUR")
    amount_uah =int(input('Введить кількість гривні: '))
    result = round(amount_uah // UAH_EUR)
    change = round(amount_uah % UAH_EUR)
#Обмін на злоті
elif currency == str("PL"):
    print(f"Ви обрали валюту PL")
    amount_uah = int(input('Введить кількість гривні: '))
    result = round(amount_uah // UAH_PL)
    change = round(amount_uah % UAH_PL)
#Результат обміну

print(f'Сума отриманої валюти = {result:^1} {currency}')
print(f"Ваша решта =  {change:>11} UAH")
