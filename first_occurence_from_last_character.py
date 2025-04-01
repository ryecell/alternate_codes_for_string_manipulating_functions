#ask user for inputs
user_string = input("Enter your string: ")
sub_string_to_find = input("Enter substring to locate first occurence of: ")

#tweaking some of the code used for index() function to start from the last character
def find_rindex(string, substring):
    for ind in range(len(string) - len(substring), -1, -1):
        if string[ind:ind+len(substring)] == substring:
            return ind
    return -1

index = find_rindex(user_string, sub_string_to_find)
if index != -1:
    print(f"The substring '{sub_string_to_find}' first appears at index {index} in the string.")
else:
    print(f"The substring '{sub_string_to_find}' was not found in the string.")