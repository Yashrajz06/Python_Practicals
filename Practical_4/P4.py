# If ages of Ram, Shyam and Ajay are input through the keyboard,
# write a program to determine the youngest of the three.
Ram = input("Enter Age of Ram: ")
Shyam = input("Enter Age of Shyam: ")
Ajay = input("Enter Age of Ajay: ")

if Ram < Shyam and Ram < Ajay:
    print("The youngest person is Ram")
elif Shyam < Ram and Shyam < Ajay:
    print("The youngest person is Shyam")
else:
    print("The youngest person is Ajay")
