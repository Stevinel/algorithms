def find_empty_location(lenght, numbers):
    new_arr = [0] * lenght

    if numbers[0] != 0:
        new_arr[0] = lenght

    for i in range(1, lenght):
        if numbers[i] == 0:
            new_arr[i] = 0
        else:
            new_arr[i] = new_arr[i - 1] + 1

    for i in range(lenght-2, -1, -1):
        if numbers[i] == 0:
            new_arr[i] = 0
        else:
            new_arr[i] = min(new_arr[i], new_arr[i + 1] + 1)
    return new_arr


if __name__ == "__main__":
    lenght = int(input())
    numbers = [int(i) for i in input().split()]
    print(*find_empty_location(lenght, numbers))
