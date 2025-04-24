#Определить номера строк матрицы R[M, N], хотя бы один элемент
#которых равен с, и элементы этих строк умножить на d
def main():
    import random

    M = int(input("Введите количество строк: "))
    N = int(input("Введите количество столбцов: "))
    c = int(input("Введите значение С: "))
    d = int(input("Введите множитель D: "))

    R = [[random.randint(-100, 100) for _ in range(N)] for _ in range(M)]

    print("Исходная матрица:")
    for row in R:
        print(' '.join(map(str, row)))

    changed = []
    for i in range(M):
        if c in R[i]:
            changed.append(i + 1)
            R[i] = [x * d for x in R[i]]

    print(f"Измененные строки: {changed}")
    for row in R:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()