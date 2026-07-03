# Matrix Analyzer

A Python-based linear algebra tool that performs fundamental matrix operations such as determinant calculation, rank computation, invertibility checking, and Row Echelon Form conversion.

## Features

- Accepts user-defined matrices of any size.
- Computes the determinant of square matrices.
- Determines whether a matrix is invertible or singular.
- Calculates the rank of the matrix.
- Converts the matrix into Row Echelon Form (REF).
- Supports decimal and floating-point values.

## Technologies Used

- Python
- NumPy
- SymPy

## Project Structure

```text
Matrix-Analyzer/
│
├── matrix.py
├── README.md
```

## How It Works

1. The user enters the dimensions of the matrix.
2. Matrix elements are entered row by row.
3. The program displays the matrix.
4. If the matrix is square:
   - The determinant is calculated.
   - The program checks whether the matrix is invertible.
5. The rank of the matrix is computed.
6. The matrix is transformed into Row Echelon Form.

## Example

### Input

```text
Enter number of rows: 3
Enter number of columns: 3

Enter the matrix row-wise:
1 2 3
4 5 6
7 8 9
```

### Output

```text
Matrix
[[1. 2. 3.]
 [4. 5. 6.]
 [7. 8. 9.]]

Determinant: 0
Matrix is singular
Rank: 2

Row Echelon Form:
(Matrix([
[1, 2, 3],
[0, 1, 2],
[0, 0, 0]]), (0, 1))
```

## Mathematical Concepts Covered

- Determinant Calculation
- Matrix Rank
- Matrix Invertibility
- Singular and Non-Singular Matrices
- Row Echelon Form (REF)
- Linear Algebra Fundamentals

## Applications

- Solving systems of linear equations
- Engineering computations
- Data science and machine learning preprocessing
- Scientific computing
- Numerical analysis

## Installation

Clone the repository:

```bash
git clone https://github.com/Shouryamishra2007/Matrix-Analyzer.git
```

Install dependencies:

```bash
pip install numpy sympy
```

Run the application:

```bash
python matrix.py
```

## Future Improvements

- Add Reduced Row Echelon Form (RREF) computation.
- Compute eigenvalues and eigenvectors.
- Support matrix addition, subtraction, and multiplication.
- Add matrix inverse calculation.
- Build a graphical user interface.
- Add support for matrix visualization.

## Learning Outcomes

This project demonstrates:

- Implementation of linear algebra concepts using Python.
- Numerical computation with NumPy.
- Symbolic mathematics using SymPy.
- User input handling and validation.
- Mathematical problem solving.

## Author

**Shourya Mishra**

GitHub: https://github.com/Shouryamishra2007
