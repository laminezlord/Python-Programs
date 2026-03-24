num = int(input("Enter a 5-digit number: "))
a = num // 10000
b = (num // 1000) % 10
c = (num // 100) % 10
d = (num // 10) % 10
e = num % 10
 
if a == e and b == d:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")


    #pseudo code
# 1. Get a 5-digit number from the user
# 2. Check if the number is a palindrome by comparing it to its reverse
# 3. Print the appropriate message to the user