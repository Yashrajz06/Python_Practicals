A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

union_set = A | B
print("Union (A | B):", union_set)
intersection_set = A & B
print("Intersection (A & B):", intersection_set)
symmetric_diff_set = A ^ B
print("Symmetric Difference (A ^ B):", symmetric_diff_set)
difference_set = A - B
print("Difference (A - B):", difference_set)
A |= B
print("In-place Union (A |= B):", A)
A = {1, 2, 3, 4, 5}
A &= B
print("In-place Intersection (A &= B):", A)
A = {1, 2, 3, 4, 5}
A ^= B
print("In-place Symmetric Difference (A ^= B):", A)
A = {1, 2, 3, 4, 5}
A -= B
print("In-place Difference (A -= B):", A)
universal_set = set(range(10))
A = {2, 4, 6, 8}
complement_set = universal_set - A  # Simulating NOT operation
print("Complement (~A using universal set):", complement_set)
