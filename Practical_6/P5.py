def process_grades():
    grades = [85, 92, 78, 65, 88]
    for grade in grades:
        if grade >= 90:
            print(f"{grade} is excellent!")
        elif grade >= 80:
            pass
        else:
            print(f"{grade} needs improvement")
process_grades()