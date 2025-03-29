#ask user for input
user_input = input("Enter your sentence or word: ")
suffix = input("Enter the suffix you want to check: ")

#ends with checker 
def endswith_checker(string: str, suffix: str) :
    return string[-len(suffix):] == suffix if len(suffix) <= len(string) else False

print(endswith_checker(user_input, suffix))
