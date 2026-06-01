cart = []


def add_to_cart(item, price, quantity):
    for product in cart:
        if product[0] == item:
            product[2] += quantity
            print(f"{item} quantity updated!")
            return

    cart.append([item, price, quantity])
    print(f"{item} added to cart!")


def view_cart():
    total = 0
    print("\nYour Cart:")

    for product in cart:
        item, price, quantity = product
        item_total = price * quantity
        total += item_total
        print(f"{item} - {quantity} x {price} = {item_total}")

    print("Total:", total)


add_to_cart("Burger", 2500, 2)
add_to_cart("Drink", 800, 1)
add_to_cart("Burger", 2500, 1)

view_cart()
