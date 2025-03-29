# ask user for input
string_to_align = input("Enter the string you want to align: ")
width = int(input("Enter the width of your sentence: "))

#centering the string
def custom_center(string: str, width: int, fillchar: str = " "):
    if len(fillchar) != 1:
        raise ValueError("fillchar must be a single character")
    
    if len(string) >= width:
        return string  # No padding needed

    total_padding = width - len(string)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    return (fillchar * left_padding) + string + (fillchar * right_padding)

print(custom_center(string_to_align, width))
