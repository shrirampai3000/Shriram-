#check if the character is only a alpha-numeric

character = input("Enter a character: ")

if character.isalnum():
    print(f"'{character}' is alphanumeric.")
else:
    print(f"'{character}' is not alphanumeric.")
