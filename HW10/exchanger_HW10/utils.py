import json



def cal_sell_cource(cource, mul):
    """
        Розраховує курс продажу для кожної валюти в зазначеному словнику курсів.

        Parameters:
        - cource (dict): Словник курсів валют, який буде оновлено.
        - mul (float): Коефіцієнт, на який буде збільшено кожен курс.

        Returns:
        - dict: Оновлений словник курсів з новими значеннями курсів продажу.
    """
    for curr_name in cource.keys():  # UAH, USD,
        for sec_curr, rate in cource[curr_name]["buy"].items():
            cource[curr_name]["sell"].update({sec_curr: round(rate * (1 + mul), 2)})
    return cource


def get_curr_cource(path="data/currency_course.json"):
    """
        Зчитує словник курсів валют з файлу JSON.

        Parameters:
        - path (str): Шлях до файлу JSON із курсами валют.

        Returns:
        - dict: Словник курсів валют.
    """
    with open(path, "r") as file:
        return json.load(file)


def get_curr_bank(path="data/bank.json"):
    """
        Зчитує словник банків з файлу JSON.

        Parameters:
        - path (str): Шлях до файлу JSON із списком банків.

        Returns:
        - dict: Словник банків.
    """
    with open(path, "r") as file:
        return json.load(file)


def exchange(amount, cource, operation, old_curr, new_curr):
    """
    Обчислює обмінну операцію для заданої суми, валют та курсів.

    Parameters:
    - amount (float): Сума для обміну.
    - cource (dict): Словник курсів валют.
    - operation (str): Операція обміну ("buy" або "sell").
    - old_curr (str): Вихідна валюта.
    - new_curr (str): Цільова валюта.(автоматично переводиться у верхній регістр)

    Returns:
    - float: Сума в цільовій валюті після обміну.
    """
    return amount * cource[old_curr][operation][new_curr.upper()]


def input_data(questions):
    """
        Функція для введення даних на основі списку питань.

        Parameters:
        - questions (tuple): Кортеж з питань, які повинні бути задані користувачеві.

        Returns:
        - list: Список відповідей на питання користувача.
    """
    answers = []
    index = 0

    while index < len(questions):
        item = questions[index]

        if item["question"] is None:
            answers.append(item.get("fixture"))
            index += 1
        else:
            value = input(item["question"] + " ")
            if value.lower() == "back":
                while index > 0:
                    index -= 1
                    if questions[index]["question"] is not None:
                        break
                if answers:
                    # Знаходимо індекс питання, на яке повертає back
                    back_index = index
                    # Видаляємо всі відповіді, які були дані на питаннях, на які повертає back
                    answers = answers[:back_index]
            elif value.lower() == "reset":
                return input_data(questions)
            else:
                if "func" in item:
                    validated_input = item["func"](value)
                    if validated_input is not None:
                        answers.append(validated_input)
                        index += 1
                else:
                    answers.append(value)
                    index += 1

    return answers