# Simple Shopping Cart Program

item_product = input("Enter the product: ")
item_quantity = int(input("How many would you like to buy? "))
item_price = float(input("How much is it? (ex. 22.00): PHP"))

total_price = item_quantity * item_price

print(f"\nYour total price for {item_product} item is {total_price}")
print(f"{item_price:>10.2f}\n+ {item_quantity:>2} items")
print(f"----------")
print(f"= {total_price:>10.2f}")