#ask user for input with multiple spaces at the beginning
user_input = input("Enter your input with multiple spaces at the beginning: ")

#scan input for spaces
def lstrip_func(user_input):
    for character, space in enumerate(user_input):
        if space != ' ':
            return user_input[character:]

#print updated string
result = lstrip_func(user_input)
print(result)

    