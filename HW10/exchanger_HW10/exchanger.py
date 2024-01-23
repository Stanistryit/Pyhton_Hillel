# TODO add bank calculation
# TODO  додати табличку з курсами
# TODO заппропонувати ще покращення обміника
# TODO check cource so u can't earn money by exchange
"""
+) Беремо звідкісь ззовні курс покупки
+) Розраховуємо курс продажу
) Мати змогу Міняти націнку, чи робити знижку
+) Мати змогу обмінювати різні валюти в майбутьому але зараз лише відносно гривні
+) Мати змогу міняти операцію купівля\продаж
) Мати змогу в командному промті написати ресет і почати опитування знову, в майбутьному написати бек і переввезти
минуле значення при цьому зберігаючи старе
) Мати змогу виводити на екран табло з курсом валют
) чи можемо видати чи ні. (банк)
"""
from utils import exchange, get_curr_cource, get_curr_bank, cal_sell_cource, input_data
from settings import INPUT_QUESTIONS

"""
{
    "UAH": {
        "buy": {
            "USD": 40,
            "EUR": 36,
            "PLN": 6
        },
        "sell": {}
    },
    "USD":.....,
    "EUR":.....,
}
"""
"""
Задача виключно на фунціях
Типи даних не зміні

"""
#ми можемо маніпулювати націнкою і знижкою,. через змінну mul





#каже нам що це скрипт, який треба виконувати
if __name__ == '__main__':
    # cource = get_curr_cource()
    # cource = cal_sell_cource(cource, 0.05)
    # amount = 1600
    # operation = "buy"
    # old_curr = "UAH"
    # new_curr = "USD"
    # result = exchange(amount, cource, operation, old_curr, new_curr)
    # print(f"We will give you for {operation} {amount} {new_curr} for {result} {old_curr} ")
    #
    # amount = 1600
    #
    # result = exchange(amount, cource, operation, old_curr, new_curr)
    # print(f"We will give you for {operation} {amount} {new_curr} for {result} {old_curr} ")

    cource = get_curr_cource()
    cource = cal_sell_cource(cource, 0.05)
    amount = 1600
    operation = "buy"
    old_curr = "UAH"
    new_curr = "USD"
    answers = input_data(INPUT_QUESTIONS)
    amount, operation, old_curr, new_curr = answers
    result = exchange(amount, cource, operation, old_curr, new_curr)
    #exchange(*answers)
    print(f"We will give you for {operation} {amount} {new_curr} for {result} {old_curr} ")

