def check_parenthes(string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets[closing_brackets.index(char)] != stack.pop():
                return False

    return not stack



assert check_parenthes("(())") == True
assert check_parenthes(")(") == False
assert check_parenthes("()(") == False
assert check_parenthes(")())") == False
assert check_parenthes("") == True
assert check_parenthes("asasa(dsdsd)(") == False
assert check_parenthes("skaslka[{ddfdfsdd}()]") ==True
assert check_parenthes("}{kdlsds(p[])") == False