def non_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None


print(non_repeating_char("swiss"))
print(non_repeating_char("dadar"))
