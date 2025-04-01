#ask user for string input and string to count
string_input = input("Enter your string: ")
string_to_count = input("Enter substring you want to count: ")

#custom counter function
def count_occurrences(string, sub_string):
    count = 0
    for char in range(len(string) - len(sub_string) + 1):
        if string[char:char+len(sub_string)] == sub_string:
            count += 1
    return count

print(count_occurrences(string_input,string_to_count))