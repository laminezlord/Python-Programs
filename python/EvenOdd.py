def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0   

number = 19
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{(number)} is odd.")