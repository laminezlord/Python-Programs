# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# num3 = input("Enter third number: ")

# sum = float(num1) + float(num2) + float(num3)
# average = sum / 3
# product = float(num1) * float(num2) * float(num3)
# smallest = min(float(num1), float(num2), float(num3))
# largest = max(float(num1), float(num2), float(num3))
# print("The sum of the numbers is: ", sum)
# print("The average of the numbers is: ", average)
# print("The product of the numbers is: ", product)
# print("The smallest number is: ", smallest)
# print("The largest number is: ", largest)

# pseudo code
# 1. Get three numbers from the user
# 2. Calculate the sum of the numbers
# 3. Calculate the average of the numbers
# 4. Calculate the product of the numbers
# 5. Find the smallest number
# 6. Find the largest number
# 7. Print the results to the user


# number = int(input("Enter an integer: "))
# square = number ** 2

# if number > 100:
#     print("The number is greater than 100")
# elif number < 100:
#     print("The number is less than 100")
# else:
#     print("The number is equal to 100")

# if number != 100:
#     print("The number is not equal to 100")

# if square > 100:
#     print("The square is greater than 100")
# elif square < 100:
#     print("The square is less than 100")
# else:
#     print("The square is equal to 100")

# if square != 100:
#     print("The square is not equal to 100")

# pseudo code
# 1. Get an integer from the user
# 2. Calculate the square of the number
# 3. Compare the number to 100 and print the appropriate message
# 4. Compare the square to 100 and print the appropriate message

# number = int(input("Enter an integer: "))
# if number % 3 == 0:
#     print("The number is odd")
# else:    print("The number is even")


# number1 = int(input("Enter first integer: "))
# number2 = int(input("Enter second integer: "))
# if number1*3 == number2:
#     print("The first number is three times the second number")
# else:    print("The first number is not three times the second number")


# TAX CALCULATOR
# name = input("Enter your name: ")
# income = float(input("Enter your income: "))
# if income <= 30000:
#     tax = income * 0.15
# elif income >= 30000:
#     tax = income * 0.20
# print("Hello ", name, " your tax is: ", tax)

# palindrome
# number = input("Enter a 5-digit number: ")
# if number == number[::-1]:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")

# pseudo code
# 1. Get a 5-digit number from the user
# 2. Check if the number is a palindrome by comparing it to its reverse
# 3. Print the appropriate message to the user


# num = int(input("Enter a 5-digit number: "))
# a = num // 10000
# b = (num // 1000) % 10
# c = (num // 100) % 10
# d = (num // 10) % 10
# e = num % 10

# if a == e and b == d:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")


# reading numbers until a specified sum is reached
# number = 0
# total = 0
# while total < 100:
#     number = int(input("Enter a number: "))
#     total += number
# print("The total is: ", total)

# school score checker

# score = float(input("Enter the student's score: "))
# if score >= 70 and score <= 100:
#     print("The student received an A")
# elif score >= 60 and score < 70:
#     print("The student received a B")
# elif score >= 50 and score < 60:
#     print("The student received a C")
# elif score >= 0 and score < 50:
#     print("The student received a D")
# else:
#     print("Invalid score. Please enter a score between 0 and 100.")

# banking system using switch case

# print("select your preferred language: ")
# print("""1. English
#       "2. Yoruba
#       3. Hausa
#       4. Igbo
#       9. Exit""")

# menu = int(input("Enter your choice: "))
# match menu:
#     case 1:
#         print("""Welcome to the banking system
#               Please select an option:
#               1. Check balance
#               2. Deposit
#               3. Withdraw
#               4. Cheeck balance
#               9. Exit""")
#     case 2:
#         print("""Kaabo si eto isowo
#               Jowo yan aṣayan kan:
#               1. Ṣayẹwo iwọntunwọnsi
#               2. Idogo
#               3. Yọ
#               4. Ṣayẹwo iwọntunwọnsi
#               9. Jade""")
#     case 3:
#         print("""Barka da zuwa tsarin banki
#               Don Allah zaɓi zaɓi:
#               1. Duba ma'auni
#               2. Ajiya
#               3. Cire
#               4. Duba ma'auni
#               9. Fita""")
#     case 4:
#         print("""Ndewo na sistemụ akụ""
#               Biko họrọ nhọrọ:
#               1. Lelee nguzo
#               2. Tinye ego
#               3. Wepụ ego
#               4. Lelee nguzo
#               9. Pụọ""")
#     case 9:
#         print("Thank you for using the banking system")
#     case _:
#         print("Invalid choice. Please select a valid option.")


# atm machine using switch case
# from unittest import case


# initial_balance = 50000
# print("Welcome to the ATM machine")
# print("""Please select an option:
#  1. Check balance
#  2. Deposit
#  3. Withdraw
#  4. Exit""")
# menu = int(input("Enter your choice: "))
# match menu:
#  case 1:
#     print("Your balance is: ", initial_balance)
#  case 2:
#     deposit = float(input("Enter the amount to deposit: "))
#     initial_balance += deposit
#     print("Your new balance is: ", initial_balance)
#  case 3:
#      withdraw = float(input("Enter the amount to withdraw: "))
#         if withdraw > initial_balance:
#         print("Insufficient funds")
#    elif withdraw < 50000:
#        print("Transaction Limit Exceeded")
#    else:
#        print("""TRANSACTION APPROVED
#                Your new balance is: """, initial_balance)
#  case 4:
#        print("Thank you for using the ATM machine")
#  case _:
#        print("Invalid choice. Please select a valid option.")

# using while loop to print 1-10 on a line

# count = 0
# while count < 10:
#     print(count + 1)
#     count += 1

