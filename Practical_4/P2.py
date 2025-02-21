# Write a program to check whether a triangle is valid or not, when
# the three angles of the triangle are entered through the keyboard.
a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

if a + b + c == 180:
    print("The triangle is valid.")
else:
    print("The triangle is invalid.")