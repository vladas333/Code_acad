# Create a function that returns only strings with unique characters

def any_string(x = input("Please enter any word: ")):
    unique_characters = set(x)
    print(unique_characters)

any_string()