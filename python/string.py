def count_digits_and_letters(string):
    digits = 0
    letters = 0
    for char in string:
        if isdigit(char):
            digits += 1
        elif isalpha(char):
            letters += 1
    if digits >= 0:
        print("The number of digits in this string is:", digits)
    if letters >= 0:
        print("The number of letters in this string is:", letters)

def isalpha(char):
    if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
        return True
    else:
        return False

def isdigit(char):
    if char >= '0' and char <= '9':
        return True
    else:
        return False

string = input("Enter a string: ")
count_digits_and_letters(string)