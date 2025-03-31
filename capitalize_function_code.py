#ask user for input
user_text = input("Enter a string: ")

#capitalize function
def custom_capitalize(letter):
    if not letter:
        return ""
    
    first_letter = letter[0].upper()
    rest_of_string = letter[1:].lower()
    
    return first_letter + rest_of_string

result = custom_capitalize(user_text)
print(f"Capitalized string: {result}")
