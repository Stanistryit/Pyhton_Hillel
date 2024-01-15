def less_then_n_count(lst):
    result = []

    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[j] < lst[i]:
                count += 1
        result.append(count)

    return result

assert less_then_n_count([6, 5, 4, 8]) == [2, 1, 0, 3]
assert less_then_n_count([7, 7, 7, 7]) == [0, 0, 0, 0]
assert less_then_n_count([1, 2, 3, 4]) == [0, 1, 2, 3]