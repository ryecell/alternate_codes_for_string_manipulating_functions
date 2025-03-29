#get string input
string_input = input("Enter your string: ")
prefix = input("Enter prefix you want to remove: ")

#update string with removed prefix
if string_input.startswith(prefix):
    string_input = string_input.replace(prefix, '')
else:
    pass

print(string_input)
