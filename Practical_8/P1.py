list1 = [(1,2,3),(),(4,5,6)]
newList = [num for num in list1 if num]
print("Original List: " , list1)
print("After removing empty tuple: ",newList)