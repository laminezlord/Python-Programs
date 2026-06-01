items = ("v", "i", "v", "i", "a", "n")

def check_items(item):
    for i in range(len(items)):
        if items[i] == item:
            return f"{item} is inside the items."
    return f"{item} is not in the items."
print("Welcome to the items checker!")
item_to_check = input("Please enter the item you want to check: ")
result = check_items(item_to_check)
print(result)   

