# Ordering product in grocery (trying to learn dictionaries)

products = {"apple" : 26.50,
            "lemon": 28.50,
            "cabbage" : 48.00,
            "eggplant": 22.80,
            "bread" : 18.30,
            "milk": 26.00}

cart = []
total_price = 0

while True:
    print("\n---------GROCERY STORE---------\n")
    for key, value in products.items():
        print(f"{key.title()}: PHP {value}")
    print("\n---------------------------")

    if not cart:
        print(f"No items in your cart, please order one")
    else:
        print(f"Current items in your cart: {cart}")

    print("\nPress E to order")
    item = input("Select an item you wanted to order: ").lower()

    if item == "e":
        print("\n---------GROCERY STORE---------\n")
        for key, value in products.items():
            print(f"{key.title()}: PHP {value}")
        print("\n---------RECEIPT---------\n")
        if not cart:
            print(f"No items in your cart, please order one")
        else:
            print(f"Current items in your cart: {cart}")

        for item in cart:
            total_price += products.get(item)

        print(f"Total price: PHP {total_price:.2f}")
        print("\n---------------------------")
        break
    elif products.get(item) is not None:
        cart.append(item)
    else:
        continue
