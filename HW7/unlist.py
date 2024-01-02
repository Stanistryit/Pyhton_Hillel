def unlist(lst):
    result = []

    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        elif isinstance(item, str):
            result.extend(list(item))
        else:
            result.append(item)

    return result

# Перевірка

assert unlist([['Vlad', 'Kira'], ['Dima', 'Dasha', ['Nikita']], 'Vova']) == ['Vlad', 'Kira', 'Dima', 'Dasha', ['Nikita'], 'V', 'o', 'v', 'a']
