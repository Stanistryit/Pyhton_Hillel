def unlist(l):
    flat_list = []
    for sublist in l:
        if isinstance(sublist, list):
            flat_list.extend(unlist(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

# Перевірка

assert unlist([['Vlad', 'Kira'], ['Dima', 'Dasha', ['Nikita']], 'Vova']) == ['Vlad', 'Kira', 'Dima', 'Dasha', 'Nikita', 'Vova']
assert unlist(["H", ["l"], ["l"], ["e"], "l"]) == ["H", "l", "l", "e", "l"]