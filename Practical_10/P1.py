# 1. Create a dictionary called students containing names and ages.
# Copy the dict into stud. Empty the
#     student dictionary as student stud contains the data.

students = {
    "Yashraj": "23",
    "Rohan": "22",
    "Anuj": "19",
    "Aryan": "18",
}
stud = students.copy()
students.clear()
print("After Copying Dictionary:",stud)
print("Clearing original Dictionary:",students)