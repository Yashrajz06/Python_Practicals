students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 88, 94],
    "David": [76, 84, 79]
}

print("{:<10} {:<10} {:<10} {:<10}".format("Name", "Subject 1", "Subject 2", "Subject 3"))
print("-" * 40)
for name, marks in students.items():
    print("{:<10} {:<10} {:<10} {:<10}".format(name, marks[0], marks[1], marks[2]))
