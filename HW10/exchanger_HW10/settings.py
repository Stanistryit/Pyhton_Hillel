from validators import validate_num, validate_str

INPUT_QUESTIONS = (
    {"question": "введіть сумму", "func": validate_num},
    {"question": "введіть операцію s ->sell|b ->buy", "func": validate_str},
    # TODO зробити односимвольні аліаси для валют
    {"question": None, "fixture": "UAH", "func": validate_str},
    {"question": "Введіть валюту(USD|EUR|PLN)", "fixture": "USD", "func": validate_str},
)
