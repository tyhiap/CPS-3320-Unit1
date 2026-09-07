item_price_str = input("How much is an item at the store? ")
item_price = float(item_price_str)

quantity_str = input("How many items would you like to purchase? ")
quantity = int(quantity_str)

subtotal = item_price * quantity
sales_tax_rate = 0.06625  # New Jersey's sales tax of 6.625%
salesTax = subtotal * sales_tax_rate
total = subtotal + salesTax

print("Original Price: $" + str(item_price))
print("Quantity: " + str(quantity))
print("Tax: $" + str(salesTax))
print("Total with tax: $" + str(total))
