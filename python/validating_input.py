passes = 0
total_inputs = 5

for i in range(total_inputs):
    while True:
        value = input(f"Enter 1 or 2 (input {i+1}/{total_inputs}): ")
        if value in ('1', '2'):
            passes += 1
            break
        print("Invalid input. Try again.")

failures = total_inputs - passes
print(f"Passes: {passes}, Failures: {failures}")