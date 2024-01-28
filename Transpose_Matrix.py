# Original matrix represented as a list of lists
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Transpose the matrix using list comprehension and nested loops
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

#print the original matrix
print("Original Matrix is:")
for row in matrix:
    print(row)

# Print the transposed matrix
print("Transpose of matrix is")
for row in transposed_matrix:
    print(row)
