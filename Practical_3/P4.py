#Swapping variables using ^ Bitwise XOR operator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")
num1 ^= num2
num2 ^= num1
num1 ^= num2
print(f"After swapping: num1 = {num1}, num2 = {num2}")

if num1 & 1 == 0:
    print(f"{num1} is even.")
else:
    print(f"{num1} is odd.")