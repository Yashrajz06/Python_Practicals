# 2. Create a empty set. Write a program that adds five new names to this set, modifies one existing name
#    and deletes two existing names in it.

set1 = set()
set1.add("Atharva")
set1.add("Bhuvan")
set1.add("Chinmay")
set1.add("Dinesh")
set1.add("Esha")
print(set1)
set1.add("Farhan")
set1.discard("Bhuvan")
set1.discard("Esha")
print(set1)
