def int_matrix(mas):
    return list(map(int, mas))


def determinant_operation(matrix, dim):
    if dim == '2 на 2':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if not all([i.isdigit() for i in matrix]):
            return 'Введите в поля цифры'
        matrix = int_matrix(matrix)
        det = matrix[0] * matrix[3] - matrix[2] * matrix[1]
        return 'Детерминант матрицы: ' + str(det)
    elif dim == '3 на 3':
        if any([i == '' for i in matrix]):
            return 'Введите значения во все поля'
        if not all([i.isdigit() for i in matrix]):
            return 'Введите в поля цифры'
        matrix = int_matrix(matrix)
        det = matrix[0] * (matrix[4] * matrix[8] - matrix[5] * matrix[7]) - matrix[1] * (matrix[3] * matrix[8] - matrix[5] * matrix[6]) + matrix[2] * (matrix[3] * matrix[7] - matrix[6] * matrix[4])
        return 'Детерминант матрицы: ' + str(det)
    return 'Что-то пошло не так'
