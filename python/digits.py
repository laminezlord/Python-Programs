# step 1
highest = None
lowest = None

# step 2
numbers = input("Enter a list of numbers separated by spaces: ").split()

# step 3
for number in numbers:
    # step 4
    if highest is None or number > highest:
        highest = number
    # step 5
    if lowest is None or number < lowest:
        lowest = number

# step 6
print("Highest number:", highest)
print("Lowest number:", lowest)

# pseudo code
# 1. initialize the highest and lowest variables to None
# 2. collect input using function .split() ->
# it is used for seperating and turning string into substring
# 3. for each number, compare it to the current highest and lowest values
# 4. if the number is greater than the current highest, update the highest variable
# 5. if the number is less than the current lowest, update the lowest variable
# 6. after the loop, print the highest and lowest values
