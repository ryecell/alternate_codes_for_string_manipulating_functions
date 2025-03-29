#swapcase function without swapcase
def custom_swapcase(s: str) -> str:
    result = []
    
    for char in s:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result.append(chr(ord(char) - 32))
        elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result.append(chr(ord(char) + 32))
        else:
            result.append(char)  # Keep non-alphabet characters unchanged

    return "".join(result)