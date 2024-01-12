def roman_to_decimal(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_number = 0

    prev_value = 0

    for numeral in reversed(roman_numeral):
        value = roman_numerals[numeral]

        if value < prev_value:
            decimal_number -= value
        else:
            decimal_number += value

        prev_value = value

    return decimal_number


# асерти
assert roman_to_decimal('XIV') == 14
assert roman_to_decimal('MMXXIV') == 2024

