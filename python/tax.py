name = input("Enter your name: ")
income = float(input("Enter your income: "))
if income <= 30000:
    tax = income * 0.15
elif income >= 30000:
    tax = income * 0.20
print("Hello ", name, " your tax is: ", tax)