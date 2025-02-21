names = ["Rohit", "Virat", "Rahul", "Hardik"]
roll_numbers = [101, 102, 103, 104]
marks = [85, 90, 78, 88]
student_data = list(zip(names, roll_numbers, marks))
print("List of tuples (Name, Roll Number, Marks):")
print(student_data)
names_tuple, roll_numbers_tuple, marks_tuple = zip(*student_data)
print("\nTuple of Names:", names_tuple)
print("Tuple of Roll Numbers:", roll_numbers_tuple)
print("Tuple of Marks:", marks_tuple)
