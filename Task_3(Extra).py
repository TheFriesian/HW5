import random

matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]

for row in matrix:
    print(row)

sum_main_diagonal = sum(matrix[i][i] for i in range(10))
print("\nSum of the main diagonal:", sum_main_diagonal)

side_diagonal = [matrix[i][9 - i] for i in range(10)]
print("\nMinimum value of the side diagonal:", min(side_diagonal))
print("Maximum value of the side diagonal:", max(side_diagonal))

column_index = int(input("\nEnter column index (0-9): "))
print([matrix[i][column_index] for i in range(10)])

row_index = int(input("\nEnter row index (0-9): "))
print(matrix[row_index])

col1 = int(input("\nEnter first column index for swapping (0-9): "))
col2 = int(input("Enter second column index for swapping (0-9): "))
for i in range(10):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

row1 = int(input("\nEnter first row index for swapping (0-9): "))
row2 = int(input("Enter second row index for swapping (0-9): "))
matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

print("\nUpdated matrix:")
for row in matrix:
    print(row)
