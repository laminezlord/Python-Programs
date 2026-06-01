inventory = ["Laptop", "Keyboard", "Mouse", "Monitor"]

def check_inventory(item):
    for i in range(len(inventory)):
        if inventory[i] == item:
            return f"{item} is inside the inventory."
    return f"{item} is not in the inventory."

print("Welcome to the inventory checker!")

item_to_check = input("Please enter the item you want to check: ")
result = check_inventory(item_to_check)
print(result)