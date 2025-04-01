#ask user for input to align
align_word = input("Enter word to align: ")
width = int(input("Enter the length of your parameter: "))

#alignement function
def right_align(string: str, width: int) -> str:
    
    if len(string) >= width:
        return string  # No padding needed
    
    return " " * (width - len(string)) + string

print(right_align(align_word, width))
