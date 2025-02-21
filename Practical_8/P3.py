items = [("Mobile", 75000.50), ("Tablet", 45000.75), ("PC", 30000.00),
         ("Headphone", 15000.25), ("Keyboard", 5000.99)]

sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
print("Items sorted by price in descending order:")
for item in sorted_items:
    print(item)
