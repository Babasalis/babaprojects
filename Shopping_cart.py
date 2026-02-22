"""
Create a Cart class for an online shop where you can add items, 
remove items, and calculate the total price including a 15% tax
"""
#create a class cart
class Cart():
    # initiate attributes
    def __init__(self, tax = 0.15) :
        self.items = {}
        self.tax = tax
    # create addItem function to add items to the function
    def addItem(self, item, price, quantity = 1) :
        #If the item already exists in the cart, increment its quantity by one
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}
    # create removeItem function to remove items from the function
    def removeItem(self, item):
        #Verify if the item exists in the cart and has a quantity greater than one
        if item in self.items and self.items[item]['quantity'] > 1:
            #Reduce the number of quantity by one
            self.items[item]['quantity'] -= 1
        #Verify if the item exists in the cart and has a quantity of exactly one
        elif item in self.items and self.items[item]['quantity'] == 1:
            #Delete the item entirely
            del self.items[item]
        else:
            return "Item not found"
    #create totalPrice to calculate the total price and add the 15% tax
    def totalPrice(self):
        #check to make sure the self.items dictionary isn't empty
        if not self.items:
            return "No items added"
        else:
            total = sum(detail['price'] * detail['quantity'] for detail in self.items.values())
            print(f"Your total price without tax is ${total:.2f}")
            taxed_total = total * self.tax
            print(f"Additional tax for this purchase ${taxed_total:.2f}")
            return f"Your total price including tax is: {total + taxed_total:.2f}"

#Create an instance of the class and save it under ola a customer
ola = Cart()
#These are the items ola bought
ola.addItem("PS5", 400, 2)
ola.addItem("Fifa", 50)
print(ola.removeItem("Call of Duty"))
ola.addItem("GTA 5", 40)
print(ola.totalPrice())
