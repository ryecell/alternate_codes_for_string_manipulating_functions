#ask user for input
user_input = input("Enter your sentence: ")

#converts all characters in string to lowercase using a dictionary
def upper(string: str) -> str:
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    mapping = {lower: upper for lower, upper in zip(lowercase, uppercase)}
    
    return "".join(mapping[char] if char in mapping else char for char in string)

print(upper(user_input))
