A = [[2, -1, 5, 1],
     [3, 2, 2, -6],
     [1, 3, 3, -1],
     [5, -2, -3, 3]]

X = [['x1'],
     ['x2'],
     ['x3'],
     ['x4']]

B = [[-3],
     [-32],
     [-47],
     [49]]

# AX = B


def delete_column(A, column_num):  # for determinant with cofactor expansion
    matrix = []
    for row in range(len(A)):
        matrix.append([])
        for col in range(len(A[row])):
            if col != column_num:
                matrix[row].append(A[row][col])
    return matrix


def det(A):
    delta = 0
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[1][0] * A[0][1]
    else:
        for i in range(len(A)):
            # it'll delete first row and i th column for every iteration
            delta += A[0][i] * ((-1)**(2 + i)) * det(delete_column(A, i)[1:])
    return delta


def replace_column(A, column, column_num):  # for cramer's rule
    matrix = []
    for row in range(len(A)):
        matrix.append([])
        for col in range(len(A[row])):
            if col != column_num:
                matrix[row].append(A[row][col])
            else:
                matrix[row].append(column[row][0])
    return matrix


def cramer_solver(A, X, B):
    results = {}
    detA = det(A)
    for i in range(len(X)):
        results[X[i][0]] = det(replace_column(A, B, i)) / detA
    return results


results = cramer_solver(A, X, B)
print(results)
