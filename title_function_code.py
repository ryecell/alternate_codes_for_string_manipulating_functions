#ask user for input
user_text = input("Enter your text: ")

#create custom tite function using def()
def custom_title(string):
    words = string.split()
    capitalized_words = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    return ' '.join(capitalized_words)

#convert then print
result = custom_title(user_text)
print(result)