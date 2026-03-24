string = input("Enter a string: ")
digits = 0
letters = 0

for char in string:
  if char.isdigit():
   digits += 1
  if char.isalpha():
   letters += 1
print("The number of digits in this string is: ", digits)
print("The number of letters in this string is: ", letters)


