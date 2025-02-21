def print_odd_numbers():
    for num in range(1, 10):
        if num % 2 == 0:
            continue
        print(f"{num} is odd")

print_odd_numbers()