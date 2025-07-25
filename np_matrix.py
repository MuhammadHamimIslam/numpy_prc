import numpy as np

def take_inp(prompt):
    while True:
        try:
            data = float(input(prompt))
            return data
        except ValueError:
            print("Enter a valid value")

help_msg = """
1. Matrix Addition
2. Matrix Subtraction
3. Matrix dot product
4. Matrix Inverse
5. Determinet of matrix
6. Trace of Matrix
7. Matrix Solve Ax = B
8. Matrix Transpose
"""

def take_matrix_inp(): 
    row = int(input("Enter row for matrix: "))
    col = int(input("Enter column for matrix: "))
    
    # take matrix input
    mat = [[take_inp(f"Enter value for {i}×{j}: ") for i in range(col)] for j in range(row)]
    
    # make numpy array
    return np.array(mat)

def main():
    print(help_msg)
    choice = input("Choose one operation: ")
    
    match choice: 
        case "1":
            print("Enter values for matrix 1")
            matrix1 = take_matrix_inp()
            print("Enter values for matrix 2")
            matrix2 = take_matrix_inp()
            print(matrix1 + matrix2)
        case "2":
            print("Enter values for matrix 1")
            matrix1 = take_matrix_inp()
            print("Enter values for matrix 2")
            matrix2 = take_matrix_inp()
            print(matrix1 - matrix2)
        case "3":
            print("Enter values for matrix 1")
            matrix1 = take_matrix_inp()
            print("Enter values for matrix 2")
            matrix2 = take_matrix_inp()
            print(matrix1 @ matrix2)
        case "4":
            print("Enter values for matrix")
            matrix = take_matrix_inp()
            print(np.linalg.inv(matrix))
        case "5":
            print("Enter values for matri")
            matrix = take_matrix_inp()
            print(np.linalg.det(matrix))
        case "6":
            print("Enter values for matrix")
            matrix = take_matrix_inp()
            print(np.linalg.trace(matrix))
        case "7":
            print("Enter values for matrix 1")
            A = take_matrix_inp()
            print("Enter values for matrix 2")
            B = take_matrix_inp()
            print(np.linalg.solve(A, B))
        case "8":
            print("Enter values for matrix")
            matrix = take_matrix_inp()
            print(matrix.T)
        case _:
            print("Invalid choice")
            print(help_msg)

if __name__ == '__main__':
    main()