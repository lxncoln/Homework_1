# Найти наибольший и наименьший элементы прямоугольной матрицы и поменять их местами.
def main():
    import random

    M = int(input("Введите количество строк: "))
    N = int(input("Введите количество столбцов: "))

    # Создаем матрицу случайных чисел
    A = [[random.randint(-100, 100) for _ in range(N)] for _ in range(M)]

    print("Исходная матрица:")
    for row in A:
        print(' '.join(map(str, row)))

    # Ищем минимальное и максимальное значение
    min_val = max_val = A[0][0]
    min_pos = max_pos = (0, 0)

    for i in range(M):
        for j in range(N):
            if A[i][j] < min_val:
                min_val, min_pos = A[i][j], (i, j)
            if A[i][j] > max_val:
                max_val, max_pos = A[i][j], (i, j)

    # Меняем местами элементы матрицы
    i_min, j_min = min_pos
    i_max, j_max = max_pos
    A[i_min][j_min], A[i_max][j_max] = A[i_max][j_max], A[i_min][j_min]

    print("После замены:")
    for row in A:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()