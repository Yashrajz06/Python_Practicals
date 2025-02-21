#Program to Get mean, mod, and median of the list
#add random 10 integers to the list
import random as rm
list1=[ rm.randint(1,100) for _ in range(10)]
print(list1)
def mean(list1):
    return sum(list1)/len(list1)
def mod(list1):
    return max(list1)-min(list1)
def median(list1):
    list1.sort()
    if len(list1)%2==0:
        return (list1[len(list1)//2]+list1[len(list1)//2-1])/2
    else:
        return list1[len(list1)//2]
print("Mean:",mean(list1))
print("Mod:",mod(list1))
print("Median:",median(list1))