# 7% investment returns
principal = float(input("Enter the initial investment amount: "))
intrest = 0.07

print("Year/tAmount")
for year in range(1, 31):
    amount = principal * (1 + intrest) ** year
    print(f"{year}\t{amount:.2f}")
