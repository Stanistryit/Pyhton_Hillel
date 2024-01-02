def unlist(l):
    flat_list = []
    for sublist in l:
        if isinstance(sublist, list):
            flat_list.extend(unlist(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

# assert flatten_list([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
assert unlist(["H", ["l"], ["l"], ["e"], "l"]) == ["H", "l", "l", "e", "l"]