#ask user for inputs
user_string = input("Enter your string: ")
sub_string_to_find = input("Enter substring to locate first occurence of: ")

#custom index function
def find_index(string, sub_string):
    for ind in range(len(string) - len(sub_string) + 1):
        if string[ind:ind+len(sub_string)] == sub_string:
            return ind
    return -1

index = find_index(user_string, sub_string_to_find)
if index != -1:
    print(f"The substring '{sub_string_to_find}' first appears at index {index} in the string.")
else:
    print(f"The substring '{sub_string_to_find}' was not found in the string.")