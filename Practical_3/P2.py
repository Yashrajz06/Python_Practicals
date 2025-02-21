#Logical Operators
# and, or and not.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
age = int(input("Enter age: "))
if num1 > 10 and num2 < 20:
    print("Both conditions are True")
elif num1 > 10 or num2 < 20:
    print("One of the conditions is True")
else:
    print("Both conditions are False")

if not age < 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

