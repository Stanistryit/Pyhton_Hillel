def absolute_diff(numbers, target):
    return sum(abs(num - target) for num in numbers)

assert absolute_diff([1, 2, 2, 1], 1) == 2
