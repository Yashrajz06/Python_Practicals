# A set contains names which begins with a or b. Write a program to separate out names in two sets. One with a
# and another containing beginning with b.

names = {"Avinash", "Bob", "Aryan", "Binny", "Atharva", "Bhuvan"}
a_names = set()
b_names = set()
for name in names:
    if name[0].lower() == "a":
        a_names.add(name)
    else:
        b_names.add(name)

print("Names starting with A: ",a_names)
print("Names starting with B:",b_names)
