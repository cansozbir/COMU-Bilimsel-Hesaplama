from random import randint as rand


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()


def create_augmented_matrix(equations):
    augmented = equations[:-1]  # equations[-1] = results
    iter = 0
    for row in augmented:
        row.append(equations[-1][iter])  # concatenate horizontally
        iter += 1
    return augmented


def linear_system_solver(inp):
    m = create_augmented_matrix(inp)
    for i in range(len(m)):  # ust ucgen matris
        for j in range(len(m) - 1, i, -1):
            t = m[j][i] / m[i][i]
            for k in range(len(m[0])):
                m[j][k] -= t * m[i][k]

    for i in range(len(m) - 1, 0, -1):  # alt ucgen mastris
        for j in range(i - 1, -1, -1):
            t = m[j][i] / m[i][i]
            for k in range(len(m[0])):
                m[j][k] -= t * m[i][k]
    for i in range(len(m)):
        m[i][-1] /= m[i][i]
        m[i][i] /= m[i][i]
    print_matrix(m)
    return m


# Test
A1 = [2, 4]     # 2x + 4y = 8
A2 = [3, 4]     # 3x + 4y = 9
A_res = [8, 9]

B1 = [4, 5, 8]      # 2x + 5y + 8z = 14
B2 = [3, 4, 10]     # 3x + 4y + 10z =
B3 = [8, 4, 12]     # 8x + 4y + 12z = 16
B_res = [14, 32, 16]

C1 = [2, 5, 8, 6]
C2 = [3, 4, 10, 5]
C3 = [8, 7, 12, 9]
C4 = [9, 17, 8, 12]
C_res = [14, 32, 16, 5]

# Listenin son elemani sonuclari icermelidir.

# linear_system_solver([A1, A2, A_res])
# linear_system_solver([B1, B2, B3, B_res])
linear_system_solver([C1, C2, C3, C4, C_res])
