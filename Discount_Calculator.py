"""
 A shop gives a 10% discount on items over $100.
 Write a program that takes a price and tells the customer how much they pay after the discount
"""
price = float(input("Enter the price: "))
if price > 100:
    discount = price * 0.1
    price = price - discount
    print(f"After discount, you will pay {price:,.2f}")
else:
    print(f"After discount, you will pay {price:,.2f}")
print("Thank you for shopping")

