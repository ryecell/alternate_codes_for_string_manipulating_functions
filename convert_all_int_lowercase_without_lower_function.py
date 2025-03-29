#ask user for input
user_input = input("Enter your sentence: ")

#converts all characters in string to lowercase using a dictionary
def lower(string: str) -> str:
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    mapping = {upper: lower for upper, lower in zip(uppercase, lowercase)}
    
    return "".join(mapping[char] if char in mapping else char for char in string)

print(lower(user_input))
