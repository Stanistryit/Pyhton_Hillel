class Currency:

   def __init__(self, UAH: float, USD: float, EUR: float, PL: float) -> None:
       self.UAH: float = UAH
       self.USD: float = USD
       self.EUR: float = EUR
       self.PL: float = PL

   def summary(self) -> str:
       return f"У мене є {self.UAH} гривень, {self.USD} доларів, {self.EUR} євро і {self.PL} злотих."

   def __getitem__(self, key: str) -> float:
       if key not in ["UAH", "USD", "EUR", "PL"]:
           raise KeyError(f"Невірна валюта: {key}")
       return getattr(self, key)

   def __add__(self, other: "Currency") -> "Currency":
       if not isinstance(other, Currency):
           raise TypeError("Додати можна тільки два об'єкти класу Currency")
       new_saving = Currency(
           self.UAH + other.UAH,
           self.USD + other.USD,
           self.EUR + other.EUR,
           self.PL + other.PL,
       )
       return new_saving

   def __str__(self) -> str:
       return (
           f"Сума двух банків: {self.UAH} гривень, {self.USD} доларів, {self.EUR} євро і {self.PL} злотих."
       )

   def equival(self, currency: str) -> str:
       if currency not in ["UAH", "USD", "EUR", "PL"]:
           raise KeyError(f"Невірна валюта: {currency}")
       result = self[currency]
       for other_currency in ["UAH", "USD", "EUR", "PL"]:
           if other_currency != currency:
               result += getattr(self, other_currency) * exchange_rates[other_currency][currency]
       return str(round(result, 2)) + ' ' + currency

   def __eq__(self, other: "Currency") -> bool:
       if not isinstance(other, Currency):
           return False
       return self.equival("UAH") == other.equival("UAH")


# Курс валют
exchange_rates = {
    'UAH': {'USD': 0.026, 'EUR': 0.024, 'PL': 0.10},
    'USD': {'UAH': 37.5, 'EUR': 0.92, 'PL': 4.02},
    'EUR': {'UAH': 41, 'USD': 1.09, 'PL': 4.37},
    'PL': {'UAH': 10, 'USD': 0.25, 'EUR': 0.23}
}

my_saving = Currency(10, 20, 30, 40)

# Виводить банк
print(my_saving.summary())
# Виведе: У мене є 33 гривні, 100 доларів, 200 євро і 100 злотих.

# Виводить кількість конкретної валюти в банку
print('PL в банку: ' + str(my_saving.PL))
# Виведе: PL в банку: 40

# Виводить банк в заданій валюті.
print(my_saving.equival("UAH"))  # Виведе: 2350.0 UAH
print(my_saving.equival("USD"))  # Виведе: 62.96 USD
print(my_saving.equival("EUR"))  # Виведе: 57.84 EUR
print(my_saving.equival("PL"))  # Виведе: 252.6 PL

your_saving = Currency(50, 60, 70, 80)
print(my_saving + your_saving) # Виводить: Сума двух банків: 43 гривень, 120 доларів, 230 євро і 140 злотих.

'''
Еквівалентне порівняння двох банків. 
Зробив дуже простій приклад, бо треба підгоняти коректно курс валют. 
А я використовував майже реальний, що заважає це зробити
'''
my_saving2 = Currency(1000,0,0,0)
your_saving2 = Currency(0,0,0,100)

print(my_saving2.equival("UAH") == your_saving2.equival('UAH')) #Варіант реалізації без зайвих функцій (не красивий)
print(my_saving2 == your_saving2) # Варіант реалізації через функцію __eq__





