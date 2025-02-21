queue = list()
def addItem(item):
    queue.append(item)

def removeItem():
    queue.pop(0)
while True:
    i = input("1. Add Item\n2. Remove Item\n3. Display Queue\n4. Exit\n")
    if i == "1":
        addItem(input("Enter item: "))
    elif i == "2":
        removeItem()
    elif i == "3":
        print(queue)
    else:
        break
