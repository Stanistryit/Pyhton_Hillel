def balanced_substrings(s):
    result = []
    count_L = 0
    count_R = 0
    current_substring = ""

    for char in s:
        current_substring += char

        if char == "L":
            count_L += 1
        elif char == "R":
            count_R += 1

        if count_L == count_R:
            result.append(current_substring)
            current_substring = ""
            count_L = 0
            count_R = 0

    return result

assert balanced_substrings("LRLRLRLRRRRLLLLRRLRLRLRLR") == ['LR', 'LR', 'LR', 'LR', 'RRRLLL', 'LR', 'RL', 'RL', 'RL', 'RL']
