def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        rew = []
        matrix.append(rew)
        for j in range(m):
            matrix[i].append(value)
        print(matrix)

get_matrix(4,6,8)


