# Given a point (x, y), write a program to
# find out if it lies on the Xaxis, Y-axis or on the origin.
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x == 0 and y == 0:
    print("Point lies on the origin")
elif x == 0:
    print("Point lies on the Y-axis")
elif y == 0:
    print("Point lies on the X-axis")
