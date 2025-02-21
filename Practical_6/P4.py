def print_multiples_of_three():
    for i in range(1, 20):
        if i % 3 != 0:
            continue
        print(f"{i} is a multiple of 3")

print_multiples_of_three()