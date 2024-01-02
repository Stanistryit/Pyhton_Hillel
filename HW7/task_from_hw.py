
def check_curr_recursive(kasa, amount, keys=None):
    if keys is None:
        keys = list(kasa.keys())

    if not keys:
        return amount == 0

    key = keys[0]
    max_amount = min(amount // key, kasa[key])
    return check_curr_recursive(kasa, amount - key * max_amount, keys[1:])

assert check_curr_recursive({500:1, 100:2, 1:10}, 200) == True
assert check_curr_recursive({100:2, 1:10}, 211) == False
assert check_curr_recursive({100:2, 2:10}, 201) == False
assert check_curr_recursive({100:2, 1:10}, 57) == False