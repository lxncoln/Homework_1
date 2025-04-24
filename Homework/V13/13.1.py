# Определить наименьший элемент каждой четной строки матрицы А[М, N]
def main():
    import random

    M = int(input("Введите количество строк: "))
    N = int(input("Введите количество столбцов: "))

    # Создаем матрицу случайных чисел
    A = [[random.randint(-100, 100) for _ in range(N)] for _ in range(M)]

    print("Исходная матрица:")
    for row in A:
        print(' '.join(map(str, row)))

    # Находим минимальные значения в четных строках
    results = []
    for i in range(M):
        if (i + 1) % 2 == 0:
            min_val = min(A[i])
            results.append(min_val)
            print(f"Строка {i + 1}: минимальное значение = {min_val}")

    print("Минимальные значения четных строк:", results)


if __name__ == "__main__":
    main()