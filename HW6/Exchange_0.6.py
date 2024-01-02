currencies = {
  "USD": {
    "buy": 30.00,
    "sell_percent": 5,
    "banknotes": {
      "1": 1,
      "5": 10,
      "10": 20,
      "20": 20,
      "50": 100,
      "100":10
    },
  },
  "EUR": {
    "buy": 40.00,
    "sell_percent": 5,
    "banknotes": {
      "1": 10,
      "5": 10,
      "10": 20,
      "20": 20,
      "50": 100,
      "100":10
    },
  },
  "PL": {
    "buy": 10.00,
    "sell_percent": 5,
    "banknotes": {
      "1": 10,
      "5": 10,
      "10": 20,
      "20": 20,
      "50": 100,
      "100":10
    },
  },
}
MULTIPLE = 50
def sell_price_calc(buy_price, sell_percent):
    """
    Функція генерує ціну продажу валюти.
    Аргументи:
        buy_price: Ціна покупки валюти
        sell_percent: Відсоток ріниці при продажі.
    Повертає:
        Ціну продажу валюти(ціна покупки + відсоток)
    """
    sell_price = buy_price + ((buy_price*sell_percent)/100)
    return sell_price

def display_currency_rates(currencies):
    """
    Функція генерує таблицю курсу обміну валют.
    Аргументи:
        currencies: Словник з валютами.
    Повертає:
        Курс обміну валют у вигляді таблиці.
    """
    result = "Курс обміну валют на сьогодні:\n"
    result += f"| Купівля | {'Валюта':^7} | {'Продаж':^7} |\n"
    result += "|---------|---------|---------|\n"
    for currency, buy_price in currencies.items():
        buy_price = currencies[currency]['buy']
        sell_price = sell_price_calc(buy_price, currencies[currency]['sell_percent'])
        result += f"| {buy_price:^7.2f} | {currency:^7} | {sell_price:^7.2f} |\n"
    result += "|---------|---------|---------|\n"
    return result

def check_banknotes_availability(result, banknotes):
    """
    Функція перевіряє наявність банкнот для видачи валюти при обміні.
    Аргументи:
        result: Сума валюти
        banknotes: Валюта
    Повертає:
        True: Якщо банкнот достатьно для обміну
        False: Якщо банкнот не достатньо для обміну.
    """
    denominations = sorted([int(denomination) for denomination in banknotes.keys()], reverse=True)
    remaining_amount = result

    for denomination in denominations:
        if remaining_amount == 0:
            break

        # Якщо є такі купюри
        if remaining_amount >= denomination and banknotes[str(denomination)] > 0:
            # Спробуємо взяти якнайбільше купюр даного номіналу
            count = min(remaining_amount // denomination, banknotes[str(denomination)])
            remaining_amount -= count * denomination
            # Зменшимо кількість доступних купюр даного номіналу
            banknotes[str(denomination)] -= count

    # Якщо залишилася сума, не можемо видати валюту
    if remaining_amount > 0:
        return False
    else:
        return True

def buy_currency(sell_price, amount_uah, currency):
    """
    Функція реалізує купівлю валюти з вбудованим округленням результату до значення MULTIPLE
    і використовує функцію check_banknotes_availability для перевірки доступності банкнот.
    Аргументи:
        sell_price: Ціна купівлі валюти
        amunt_uah: Кількість грн для обміну в валюту
        currency: Валюта
    Повертає:
        Результат обмуні гривні в задану валюту.
    """
    banknotes = currencies[currency]['banknotes'] #Змінна для перевірки доступності банкнот
    result = amount_uah // sell_price  # кількість валюти
    change = amount_uah % sell_price  # решта
    if check_banknotes_availability(result, banknotes) == True:
        def round_currency(result, change, currency):
            """
            Функція перевіряє результат обміну, і пропонує округлення до MULTIPLE
            Аргументи:
                result: результа обміну валют
                chang: решта в грн.
                currency: валюта
            Повертає:
                Результат віповідно до рішення клієнта.
            """
            if result % MULTIPLE == 0:
                return print(f"Ви отримаєте {result:.0f} {currency}, решта {change:.2f} грн.")
            else:
                if result < MULTIPLE:
                    dif_to_multiple = MULTIPLE - result
                    add_uah = dif_to_multiple * sell_price - change
                    rounded_result = result + dif_to_multiple
                    print(f"Ви можете додати {add_uah:.2f} грн. щоб отримати {rounded_result:.0f} {currency}")
                    choise = input('Бажаєте округити? Yes | No:').capitalize()
                    while choise not in ("Yes", "No"):
                        print("Ви зробили не коректний вибір!")
                        choise = input("Yes | No: ").capitalize()
                    if choise == 'Yes':
                        extra_charge = int(input('Введіть суму доплати:'))
                        # Перевірка введеної суми
                        while extra_charge < add_uah:
                            print(f'Треба внести не меньше {add_uah}грн.')
                            extra_charge = int(input('Введіть суму доплати:'))
                        extra_change = extra_charge - add_uah
                        result = rounded_result
                        return print(f'Ви отримали {result:.0f} {currency}, ваша решта {extra_change:.2f} грн.')
                    elif choise == 'Ні':
                        return print(f"Ви отримали {result:.0f} {currency}, і {change:.2f} грн. решти!")
                else:
                    multiple_amount = result / MULTIPLE  # кратність
                    multiple_count = round((multiple_amount % 1), 2)  # різниця кратності
                    # якщо близько до MULTIPLE по математичному округленню (0.5=1)
                    if multiple_count >= 0.50:
                        difToMul = abs((multiple_count * MULTIPLE) - MULTIPLE)
                        add_uah = (difToMul * sell_price) - change
                        rounded_result = result + difToMul
                        print(f"Ви можете додати {add_uah:.2f}грн. щоб отримати {rounded_result:.0f} {currency}")
                        # Даємо вибір кліенту
                        choise = input(f'Округлити суму {currency}, Yes | No: ').capitalize()
                        # Перевірка вибор
                        while choise not in ("Yes", "No"):
                            print("Ви зробили не коректний вибір!")
                            choise = input("Yes | No: ").capitalize()
                        if choise == 'Yes':
                            extra_charge = int(input('Введіть суму доплати:'))
                            # Перевірка введеної суми
                            while extra_charge < add_uah:
                                print(f'Треба внести не меньше {add_uah}грн.')
                                extra_charge = int(input('Введіть суму доплати:'))
                            extra_change = extra_charge - add_uah
                            result = rounded_result
                            return print(f'Ви отримали {result:.0f}{currency}, ваша решта {extra_change:.2f}грн.')
                        elif choise == 'No':
                            return print(f"Ви отримали {result:.0f} {currency}, і {change:.2f} грн. решти!")
                    elif multiple_count <= 0.50:
                        difToMul = abs((multiple_count * MULTIPLE) - MULTIPLE)
                        new_result = result + difToMul
                        extra_change = (difToMul * sell_price) + change
                        print(f'Бажаєте округлити суму {currency} до {new_result}{currency} і отримати {extra_change} грн. решти?')
                        choise = input("Yes | No: ").capitalize()
                        # Перевірка введення
                        while choise not in ("Yes", "No"):
                            print("Ви зробили не коректний вибір!")
                            choise = input("Yes | No: ").capitalize()
                        if choise == 'Yes':
                            result = new_result
                            return print(f"Ви отримали {result:.0f} {currency}, і {extra_change:.2f} грн. решти!")
                        elif choise == 'No':
                            return print(f"Ви отримали {result:.0f} {currency}, і {change:.2f} грн. решти!")

        return round_currency(result, change, currency)
    else:
        return print('Не вистачає банкнот для обміну!')


def sell_currency(price, amount_currency):
    """
    Функція реалізує обмін валюти на грн.
    Аргументи:
        price: сума грн за 1 валюти
        amount_currency: кількість валюти
    Повертає:
    Суму грн. за кількість валюти
    """
    get_uah = (amount_currency * price)
    return get_uah

def main():
    print(display_currency_rates(currencies))

    name = input("Введіть ваше ім'я: ").capitalize()

    print(f'{name}, яку валюту бажаєте купити/продати?')
    print('Доступні валюти: ' + ','.join(list(currencies.keys())))

    user_input = input('Введіть бажану валюту: ').upper()
    if user_input not in list(currencies.keys()):
        print('Не вірна валюта')

    else:
        currency = user_input #зберігаємо обрану валюту
        operation = input("Яку операцію ви хочете виконати? (Buy/Sell): ").capitalize()
        while operation not in ('Buy','Sell'):
            print('Обрана неіснуюча операція!')
            operation = input("Яку операцію ви хочете виконати? (Buy/Sell): ").capitalize()
        if operation == 'Buy':
            sell_price = sell_price_calc(currencies[currency]["buy"], currencies[currency]["sell_percent"])
            amount_uah = int(input('Введіть суму гривні: '))
            buy_currency(sell_price, amount_uah, currency)
        else:
            price = int(currencies[currency]["buy"])
            amount_currency = int(input(f'Введіть кілкість {currency}, які хочете обміняти: '))
            get_uah = sell_currency(price, amount_currency)
            print(f'Ви отримали {get_uah} грн.!')
if __name__ == "__main__":
    main()