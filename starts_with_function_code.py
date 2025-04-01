#cusom startswith function code
def starts_with(string, prefix):
    if len(prefix) > len(string):
        return False
    for char in range(len(prefix)):
        if string[char] != prefix[char]:
            return False
    return True
