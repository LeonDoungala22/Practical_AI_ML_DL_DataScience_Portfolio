# Linear Algebra Cheat Sheet for Machine Learning and AI

Welcome to the Linear Algebra Cheat Sheet for Machine Learning and Artificial Intelligence! This concise resource provides fundamental concepts of linear algebra essential for understanding machine learning and artificial intelligence.

This cheat sheet provides a simplified overview of the essential linear algebra concepts used in machine learning and artificial intelligence, along with code examples using NumPy.

For a more detailed cheat sheet with LaTeX formulas and additional examples, please visit :
- [Linear algebra cheat sheet for deep learning](https://towardsdatascience.com/linear-algebra-cheat-sheet-for-deep-learning-cd67aba4526c)
- [Cheatsheet – Matrix with examples ](https://solutionhacker.com/cheatsheet-matrix/)
- [Linear algebra - Matrix cheat sheet](https://pmt.physicsandmathstutor.com/download/Maths/A-level/Further/Core-Pure/Edexcel/CP1/Cheat-Sheets/Ch.6%20Matrices.pdf)

## Table of Contents

1. [Introduction](#introduction)
2. [Scalars, Vectors, and Matrices](#scalars-vectors-and-matrices)
3. [Basic Operations](#basic-operations)
4. [Matrix Operations](#matrix-operations)
5. [Matrix Properties](#matrix-properties)
6. [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
7. [Singular Value Decomposition (SVD)](#singular-value-decomposition-svd)
8. [Numpy Code Examples](#numpy-code-examples)

## 1. Introduction

- **Scalars**: Single numbers.
- **Vectors**: Arrays of numbers with direction.
- **Matrices**: Rectangular arrays of numbers.

## 2. Scalars, Vectors, and Matrices

- Scalars, vectors, and matrices are fundamental building blocks.
- Example:
  - Scalar: $a = 5$
  - Vector: **v** = [1, 2, 3]
  - Matrix: **A** = [[1, 2], [3, 4]]
    
[Image illustration](https://res.cloudinary.com/practicaldev/image/fetch/s--oTgfo1EL--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://raw.githubusercontent.com/adhiraiyan/DeepLearningWithTF2.0/master/notebooks/figures/fig0201a.png)

## 3. Basic Operations

- **Addition and Subtraction**: Element-wise.
- **Scalar Multiplication**: Multiply a scalar by a vector or matrix.
- **Matrix Multiplication**: The dot product of rows and columns.
- **Transpose**: Reverses the rows and columns.
- Examples:
  - **v₁** + **v₂** = [1, 2, 3] + [4, 5, 6] = [5, 7, 9]
  - 2 * **v** = 2 * [1, 2, 3] = [2, 4, 6]
  - **A** · **B** = [[19, 22], [43, 50]]
  - Transpose of **A** = [[1, 3], [2, 4]]
 
    
![basics operations image illustration](https://i.pinimg.com/736x/5f/bc/90/5fbc904d49daefbab279bc628e66a401.jpg)


## 4. Matrix Properties

- **Identity Matrix (I)**: A square matrix with 1s on the diagonal and 0s elsewhere.
- **Inverse Matrix**: Exists if the determinant is not zero.
- **Determinant**: A scalar value associated with a square matrix.
- **Trace**: The sum of the diagonal elements.
- Examples:
  - 2x2 Identity Matrix = [[1, 0], [0, 1]]
  - If **A** is invertible, **A** · **A**⁻¹ = **I**
  - det([[1, 2], [3, 4]]) = -2
  - trace([[1, 2], [3, 4]]) = 5

## 5. Matrix Operations

- **Matrix Transposition**: Rows become columns and vice versa.
- **Matrix Rank**: The maximum number of linearly independent rows/columns.
- Examples:
  - Transpose of **A** = [[1, 3], [2, 4]]
  - Rank of a matrix.

## 6. Eigenvalues and Eigenvectors

- **Eigenvalues**: Scalars that represent how a matrix scales a vector.
- **Eigenvectors**: Vectors that remain in the same direction after transformation.
- Example:
  - For matrix **A**, the eigenvalues $\lambda_1$ and $\lambda_2$ represent the scaling factors.
    
![Illustration](https://i.ytimg.com/vi/3En5TP2zL8I/maxresdefault.jpg)


## 7. Singular Value Decomposition (SVD)

- **SVD**: Factorizes a matrix into three matrices - **U**, **Σ**, and **V**ᵀ.
- **U**: Left singular vectors, orthogonal.
- **Σ** (Sigma): Diagonal matrix with singular values.
- **V**ᵀ: Right singular vectors, orthogonal.

![Illustration](https://github.com/LeonDoungala22/AI-and-Automation-Training/assets/97343625/16afd449-f84f-461e-8696-28605e59bf94)
)



## 8. Numpy Code Examples

Here are some code examples using the popular Python library NumPy:

```python
import numpy as np

# Introduction
# Scalars, Vectors, and Matrices
scalar = 5
v = np.array([1, 2, 3])
A = np.array([[1, 2], [3, 4]])

# Basic Operations
# Addition and Subtraction, Scalar Multiplication, Matrix Multiplication, Transpose
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
result_addition = v1 + v2
result_subtraction = v1 - v2
result_scalar_multiplication = 2 * v
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result_matrix_multiplication = np.dot(A, B)
result_transpose = A.T

# Matrix Properties
# Identity Matrix, Inverse Matrix, Determinant, Trace
identity_matrix = np.array([[1, 0], [0, 1]])
A = np.array([[1, 2], [3, 4]])
A_inverse = np.linalg.inv(A)
det_A = np.linalg.det(A)
trace_A = np.trace(A)

# Matrix Operations
# Matrix Transposition
A = np.array([[1, 2], [3, 4]]
result_transpose = A.T

# Eigenvalues and Eigenvectors
# Example: Computing eigenvalues and eigenvectors of a matrix A
A = np.array([[2, -1], [4, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)

# Singular Value Decomposition (SVD)
# Example: Computing SVD of a matrix A
A = np.array([[1, 2], [3, 4]])
U, S, Vt = np.linalg.svd(A)
