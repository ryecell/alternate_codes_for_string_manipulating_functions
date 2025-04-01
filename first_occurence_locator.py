#custom index function
def find_index(string, sub_string):
    for ind in range(len(string) - len(sub_string) + 1):
        if string[ind:ind+len(sub_string)] == sub_string:
            return ind
    return -1