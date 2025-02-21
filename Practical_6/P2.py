def find_number():
    numbers = [1, 3, 5, 7, 9, 11, 13, 15]
    search_for = 9

    for num in numbers:
        if num == search_for:
            print(f"Found the number {search_for}!")
            break
        print(f"Checking number {num}")

find_number()