"""
Created by Patrick Dusenge
Jan 7, 2018
Tax Calculator
I should create it in a GUI later on
"""

print("Total Price Calculator\n")
total = 0.0

price = float(input("Enter the price: "))  # Get initial price
add_more_price = str(input("Add another price (Y/N): "))  # Ask user to add more items

total += price  # Add initial price to total

# Choice evaluation
while add_more_price.lower() == 'y':  # User inputs Y for yes, loops
    price = float(input("Enter the price: "))
    add_more_price = str(input("Add another price (y/n): "))
    total += price

    while add_more_price.lower() == 'n':
        break

tax_amount = float(input("How much tax: "))  # User inputs tax

total += (total * tax_amount)  # Add tax to total


print("Total w HST: " + str(round(total, 2)))  # Total output with tax





