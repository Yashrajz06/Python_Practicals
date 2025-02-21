# ~ - not (also called complement operator)
# << - left shift, >> - right shift
# & - and, | - or, ^ - xor
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Binary of {a}: {bin(a)}")
print(f"Binary of {b}: {bin(b)}\n")
print(f"{a} & {b} = {a & b}  (Bitwise AND)")
print(f"{a} | {b} = {a | b}  (Bitwise OR)")
print(f"{a} ^ {b} = {a ^ b}  (Bitwise XOR)")
print(f"~{a} = {~a}  (Bitwise NOT of {a})")
print(f"{a} << 1 = {a << 1}  (Left Shift by 1)")
print(f"{a} >> 1 = {a >> 1}  (Right Shift by 1)")
