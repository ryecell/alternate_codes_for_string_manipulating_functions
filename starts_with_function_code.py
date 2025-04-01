#ask user for input
user_input = input("Enter your sentence or word: ")
prefix = input("Enter the suffix you want to check: ")

#cusom startswith function code
def starts_with(string, prefix):
    if len(prefix) > len(string):
        return False
    for char in range(len(prefix)):
        if string[char] != prefix[char]:
            return False
    return True

print(starts_with(user_input, prefix))
