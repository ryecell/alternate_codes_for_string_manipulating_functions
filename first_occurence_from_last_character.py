
#tweaking some of the code used for index() function to start from the last character
def find_rindex(s, sub):
    for i in range(len(s) - len(sub), -1, -1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1
