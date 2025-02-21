# 4. Write a program to create a set containing 10 random generated numbers in the range 15 to 45.
#     Count how many of these numbers are less than 30. Delete all numbers which are greater than 35.
import random as random
set1 = set()
for i in range(10):
    set1.add(random.randint(15, 45))

count = 0
for i in set1:
    if i < 30:
        count += 1

set2 = set()

for i in set1:
    if i > 35:
        set2.add(i)

set1 = set1 - set2
print("Result:",set1)