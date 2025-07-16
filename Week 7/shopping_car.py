items = []
prices = []
total = 0

while True:
    item = input("Enter an item to add to the shopping cart (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Enter the price for {item}: R "))
    
    items.append(item)
    prices.append(price)
    total += price
    
print("Shopping Cart Summary:")
for i in range(len(items)):
    print(f"{items[i]}: R {prices[i]:.2f}")

print()
print(f"Total: R {total:.2f}")