# Задана квадратная матрица. Переставить строку с максимальным
# элементом на главной диагонали со строкой с заданным номером m.
def main():
    import random

    N = int(input("Введите размер матрицы: "))
    M = int(input("Номер строки для обмена (1..n): ")) - 1

    A = [[random.randint(-100, 100) for _ in range(N)] for _ in range(N)]

    print("Исходная матрица:")
    for row in A:
        print(' '.join(map(str, row)))

    # Ищем максимальный элемент на главной диагонали
    max_val = A[0][0]
    max_row = 0
    for i in range(N):
        if A[i][i] > max_val:
            max_val, max_row = A[i][i], i

    # Меняем строки
    A[max_row], A[M] = A[M], A[max_row]

    print(f"После замены строк {max_row + 1} и {M + 1}:")
    for row in A:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()