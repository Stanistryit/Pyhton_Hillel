def flatten_list(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        elif isinstance(item, str):
            result.extend(list(item))
        else:
            result.extend(flatten_list([item]))

    return result

# Перевірка
input_data = ['Vova']
expected_output = ['V', 'o', 'v', 'a']
assert flatten_list(input_data) == expected_output
