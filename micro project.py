# price = int(input("Enter the price of the item: "))
# quality = int(input("Enter the quantity of the item: "))
# tax = 1.00 * price * quantity
# price += tax
# if price > 1000:
#     discount = price * 0.10
#     final_price = price - discount
#     totalbill = final_price * quality
#     print(int("Final price to be paid: ", totalbill))
#     print(f"Discount applied: {discount}")
# else:
#     final_price = price
#     print("No discount applied.")
#     print(f"Final price to be paid: {final_price * quality:.1f}")
# errors not fixed trying new againnnnnnnnnn
    
    
price = float(input("Enter the Price of the item: "))
    
quantity = int(input("Enter the Quantity of the item: "))
    
tax = 0.10 * price * quantity
price = price + tax
if price > 1000:
    dicount = price * 0.10
    price = float(f"{price:1f}")
    print(f"Price before dicount (with tax): {price}")
    if price > 1000:
        discount = price * 0.10
        final_price = price - discount
        totalbill = final_price * quantity
        print(f"Discount applied: {discount:.1f}")
        print(f"Final price to be paid: {totalbill:.1f}")
    else:
        final_price = price
        print("No discount applied.")
        print(f"Final price to be paid: {final_price * quantity:.1f}")