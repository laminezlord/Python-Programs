num = int(input("Enter a five digit number: "))
if num < 10000 or num > 99999:
    print("Enter a five digit number")
else:
    d1 = num // 10000
    d2 = (num % 10000) // 1000
    d3 = (num % 1000) // 100
    d4 = (num % 100) // 10
    d5 = num % 10
    if d1 == d5 and d2 == d4:
        print("the number is a Palindrome")
    else:
        print("the number is not a Palindrome")
