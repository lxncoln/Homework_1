# Среди тех строк целочисленной матрицы, которые содержат только
# нечетные элементы, найти строку с максимальной суммой модулей элементов
def main():
    import random

    M = int(input("Введите количество строк: "))
    N = int(input("Введите количество столбцов: "))

    # Создаем матрицу случайных чисел с нечетными элементами
    A = []
    for _ in range(M):
        row = [random.randrange(-99, 99, 2) for _ in range(N)]
        A.append(row)

    print("Матрица:")
    for row in A:
        print(' '.join(f"{x:3}" for x in row))

    max_sum = -1
    best_row = -1

    for i in range(M):
        current_sum = sum(abs(x) for x in A[i])
        if current_sum > max_sum:
            max_sum, best_row = current_sum, i

    if best_row != -1:
        print(f"Строка {best_row + 1} имеет максимальную сумму модулей: {max_sum}")
        print("Элементы:", ' '.join(map(str, A[best_row])))
    else:
        print("Нет подходящих строк")


if __name__ == "__main__":
    main()