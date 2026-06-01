number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_of_numbers(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

def average_of_numbers(num_list):
    total = sum_of_numbers(num_list)
    average = total / len(num_list)
    return average


result = sum_of_numbers(number)
average_of_numbers = average_of_numbers(number)
print("The sum of the numbers is:", result)
print("The average of the numbers is:", average_of_numbers)



