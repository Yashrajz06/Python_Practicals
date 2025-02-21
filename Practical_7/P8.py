mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9,10]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9,10]]
result1 = []
print("Matrix 1: ",mat1)
print("Matrix 2: ",mat2)
for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[i])):
        row.append(mat1[i][j] + mat2[i][j])
    result1.append(row)

print("Resultant Matrix",result1)