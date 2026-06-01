initial_balance = 50000
print("Welcome to the ATM machine")
print("""Please select an option:
 1. Check balance
 2. Deposit
 3. Withdraw
 4. Exit""")
menu = int(input("Enter your choice: "))
match menu:
  case 1:
        print("Your balance is: ", initial_balance)
  case 2:
        deposit = float(input("Enter the amount to deposit: "))
        initial_balance += deposit
        print("Your new balance is: ", initial_balance)
  case 3:
        withdraw = float(input("Enter the amount to withdraw: "))
        if withdraw > initial_balance:
            print("Insufficient funds")
        elif withdraw> 50000:
            print("Transaction Limit Exceeded")
        else:
            initial_balance -= withdraw
            print("""TRANSACTION APPROVED
                     Your new balance is: """, initial_balance)
  case 4:
        print("Thank you for using the ATM machine")
  case _:
        print("Invalid choice. Please select a valid option.")