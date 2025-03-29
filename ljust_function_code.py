#ask user for input to align
align_word = input("Enter word to align: ")
fill_sentence = input("Enter the rest of your sentence: ")
width = int(input("Enter the length of your spacing: "))

#alignement function
def left_align(string: str, width: int) -> str:
    
    if len(string) >= width:
        return string  # No padding needed
    
    return string + " " * (width - len(string))

print(left_align(align_word, width) + fill_sentence)

