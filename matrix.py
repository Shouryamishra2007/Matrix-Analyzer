import numpy as np 
from sympy import Matrix

rows = int(input("Enter number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the matrix row-wise: ")

matrix = []
for i in range(rows):
    row = list(map(float, input().split()))
    matrix.append(row)

matrix = np.array(matrix)

print("\nMatrix")
print(matrix)

if rows == columns:
    det = round(np.linalg.det(matrix))
    print("\nDeterminant:", det)

    if det == 0:
        print("Matrix is singular")
    else:
        print("Matrix is invertible")
else:
    print("\nDeterminant:Not defined")


rank = np.linalg.matrix_rank(matrix, tol=1e-10)
print("Rank:", rank)

print("\nRow Echelon Form:")
sym_matrix = Matrix(matrix)
print(sym_matrix.echelon_form())