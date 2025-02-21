#while purchasing certain items a discount of 10% is offered if the quantity purchased is more than 1000
#It quantity and price per item are input through the keyboard, write a program to calculate total expenses

# quantity = int(input("Enter the quantity: "))
# price = float(input("Enter price: "))
# #quantity * price - quantity * price * discount / 100
# totalPrice = quantity * price
# discount = totalPrice * 0.1
#
# if quantity > 1000:
#     totalPrice = totalPrice - discount
#
# print("TotalExpense:",totalPrice)
#Write a program that prints a numbers from 1 to 10 using a
# n infinite loop. All numbers should get printed in the same line

# i = 1
# while i > 0:
#     if i == 11:
#         break
#     print(i,end=" ")
#     i+=1

#Given a point (x,y) write a program to find out if it lies on the x-axis, y-axis or on the origin

x = int(input("ENter x: "))

y = int(input("Enter y: "))

if x==0:
    print("It lies on Y axis")
elif y==0:
    print("It lies on X axis")
elif x==0 and y==0:
    print("It lies on the origin")
else:
    print("Not on any axis.")

#Write a program that prints all uniquq combinates of 1 , 2 and 3
# i ,j,k = 1,1,1
# while i <= 3:
#     while j <= 3:
#         while k <=3:
#             str1 = str(i)+str(j)+str(k)
#             print(str1)
#             k+=1
#         j+=1
#     i+=1


