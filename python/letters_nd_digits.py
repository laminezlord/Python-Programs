string = input("Enter a string: ")
digits = 0
letters = 0
for char in string:
     if char.isdigit():
         digits += 1
     elif char.isalpha():
         letters += 1
print("Number of digits in the string:", digits)
print("Number of letters in the string:", letters)
