rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows-i) + "* " * i)

print("Inverted Triangle")

for i in range(rows, 0, -1):
    print(" " * (rows-i) + "* " * i)

