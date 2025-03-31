#ask user for input
user_input = input("Enter a string in different casing: ")

#swapcase function without swapcase
def custom_swapcase(string: str) -> str:
    result = []
    
    for char in string:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result.append(chr(ord(char) - 32))
        elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)  # Keep non-alphabet characters unchanged

    return "".join(result)

print(custom_swapcase(user_input))