

#rstrip function
def remove_trailing_spaces(s):
    index = len(s) - 1
    while index >= 0 and s[index] == ' ':
        index -= 1
    return s[:index + 1]
