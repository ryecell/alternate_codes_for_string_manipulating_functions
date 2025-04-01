#ask user for input
user_input = input("Enter your string with multiple spaces at the back: ")

#rstrip function
def remove_trailing_spaces(string):
    index = len(string) - 1
    while index >= 0 and string[index] == ' ':
        index -= 1
    return string[:index + 1]

print(remove_trailing_spaces(user_input))
