#  Составить программу, которая заполняет квадратную матрицу порядка
# n натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по спирали».
def main():
    n = int(input("Введите размер матрицы: "))
    A = [[0] * n for _ in range(n)]

    num = 1
    layers = (n + 1) // 2

    for layer in range(layers):
        # Верх (слева направо)
        for j in range(layer, n - layer):
            A[layer][j] = num
            num += 1

        # Право (сверху вниз)
        for i in range(layer + 1, n - layer):
            A[i][n - layer - 1] = num
            num += 1

        # Низ (справа налево)
        for j in range(n - layer - 2, layer - 1, -1):
            A[n - layer - 1][j] = num
            num += 1

        # Лево (снизу вверх)
        for i in range(n - layer - 2, layer, -1):
            A[i][layer] = num
            num += 1

    print("Матрица по спирали:")
    for row in A:
        print(' '.join(f"{x:3}" for x in row))


if __name__ == "__main__":
    main()