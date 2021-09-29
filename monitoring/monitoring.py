def monitoring():
    string_quantity = int(input())
    number_of_colums = int(input())
    matrix = []

    for elem in range(string_quantity):
        num = [int(k) for k in input().split(' ')]
        matrix.append(num)
    new_matix = [[0] * string_quantity for _ in range(number_of_colums)]

    for i in range(string_quantity):
        for j in range(number_of_colums):
            new_matix[j][i] = matrix[i][j]

    for row in new_matix:
        print(*row)

if __name__ == '__main__':
    monitoring()
