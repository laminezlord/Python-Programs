numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def largest_number(num_list):
    largest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
    return largest




def smallest_number(num_list):
    smallest = num_list[0]
    for num in num_list:
        if num < smallest:
            smallest = num
    return smallest




largest = largest_number(numbers)
smallest = smallest_number(numbers)
print("The largest number is: ", largest)
print("The smallest number is: ", smallest)