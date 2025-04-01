#ask user for input to align
user_input = input("Enter your string: ")
width = int(input("Enter the length of your parameter: "))

#alignement function
def custom_zfill(string: str, width: int) -> str:
    
    if len(string) >= width:
        return string  # No padding needed
    
    return "0" * (width - len(string)) + string

print(custom_zfill(user_input, width))
