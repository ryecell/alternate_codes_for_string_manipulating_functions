#ask user for input
user_input = input("Enter your input: ")

#check if characters in input is uppercase
def lower_case(string: str) -> str:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    return all(char in lowercase for char in string if char.isalpha())

print(lower_case(user_input))