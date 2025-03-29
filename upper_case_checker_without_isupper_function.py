#ask user for input
user_input = input("Enter your input: ")

#check if characters in input is uppercase
def upper(string: str) -> str:
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return all(char in uppercase for char in string if char.isalpha())

print(upper(user_input))