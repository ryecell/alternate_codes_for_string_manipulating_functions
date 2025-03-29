#get string input
string_input = input("Enter your string: ")
suffix = input("Enter what you want to remove: ")

#update string with removed suffix
if string_input.endswith(suffix):
    string_input = string_input.replace(suffix, '')
else:
    pass
print(string_input)
