quantity = int(input("Enter the quantity: "))
price = float(input("Enter price: "))
#Forumulae
# quantity * price - quantity * price * discount / 100
totalPrice = quantity * price
discount = totalPrice * 0.1

if quantity > 1000:
    totalPrice = totalPrice - discount
print("TotalExpense:",totalPrice)