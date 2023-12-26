import json
from decimal import Decimal, getcontext
getcontext().prec = 6
MULTIPLE = 50

def load_currencies(file_path='currencies.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_sell_price(buy_price, sell_percentage):
    buy_price = buy_price + (buy_price * sell_percentage / 100)
    return buy_price

def display_currency_rates(currencies):
    print("Курс обміну валют на сьогодні:")
    print(f"| Купівля | {'Валюта':^7} | {'Продаж':^7} |")
    print("|---------|---------|---------|")
    for currency, buy_price in currencies['UAH']['buy'].items():
        sell_price = calculate_sell_price(buy_price, currencies['UAH']['sell_percentage'].get(currency, 0))
        print(f"| {buy_price:^7.2f} | {currency:^7} | {sell_price:^7.2f} |")
    print("|---------|---------|---------|")

def buy_currency(buy_price, amount_uah):
    buy_price = Decimal(buy_price)
    amount_uah = Decimal(amount_uah)
    result = amount_uah // buy_price
    change = amount_uah % amount_uah
    return result, change

def sell_currency(sell_price, amount_currency):
    return amount_currency * sell_price

def round_currency_amount(result, change, buy_price):
    buy_price = Decimal(buy_price)
    if result < MULTIPLE:
        dif_to_multiple = MULTIPLE - result
        add_uah = dif_to_multiple * buy_price - change
        rounded_result = result + dif_to_multiple
        return rounded_result, add_uah
    else:
        multiple_amount = result / MULTIPLE
        multiple_count = round(multiple_amount % 1, 2)

        if multiple_count >= 0.50:
            dif_to_multiple = MULTIPLE * (1 - multiple_count)
            add_uah = dif_to_multiple * buy_price
            rounded_result = result + dif_to_multiple
        else:
            dif_to_multiple = MULTIPLE * multiple_count
            add_uah = dif_to_multiple * buy_price
            rounded_result = result - dif_to_multiple

        return rounded_result, add_uah

def main():
    currencies = load_currencies()
    display_currency_rates(currencies)

    name = input("Введіть ваше ім'я: ")

    print(f'{name}, яку валюту бажаєте купити/продати?')
    print("Доступні валюти: " + ', '.join(currencies['UAH']['buy'].keys()))

    user_input = input("Введіть потрібну валюту: ").upper()
    found_currency = currencies['UAH']['buy'].get(user_input)

    if found_currency is not None:
        operation = input("Яку операцію ви хочете виконати? (Buy/Sell): ").capitalize()

        if operation == 'Buy':
            sell_percentage = currencies['UAH']['sell_percentage'].get(user_input, 0)
            buy_price = calculate_sell_price(currencies['UAH']['buy'][user_input], sell_percentage)
            amount_uah = int(input('Введіть кількість гривні: '))
            result, change = buy_currency(buy_price, amount_uah)
            rounded_result, add_uah = round_currency_amount(result, change, buy_price)
            print(f"Ви отримаєте {rounded_result:.0f} {user_input}, решта {add_uah:.2f} грн.")

        elif operation == 'Sell':
            sell_price = found_currency
            amount_currency = int(input(f'Введіть кількість {user_input}: '))
            result = sell_currency(sell_price, amount_currency)
            print(f"Ви отримали {result:.2f} грн.")

        else:
            print("Некоректна операція. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
