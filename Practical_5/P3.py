# A five digit number is entered through the keyboard.
# Write a program to obtain the reverse number and to determine
# whether the original number and reverse numbers are equal or not
num = int(input("Enter a five digit number: "))
orinum = num
new_num = 0
while num > 0:
    digit = num % 10
    new_num = new_num * 10 + digit
    num = num // 10
print("Reverse number is: ", new_num)
if orinum == new_num:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")