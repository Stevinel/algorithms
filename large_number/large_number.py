def compare_digits(num1, num2):
    a = str(num1)
    b = str(num2)
    if a+b > b+a:
        return True
    return False


def biggest(length_arr, arr):
    if length_arr == 1:
        result = ''.join(map(str, arr))
    for element in range(length_arr):
        num = arr[element]
        index = element
        while index > 0 and compare_digits(num, arr[index-1]):
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = num
    result = ''.join(map(str, arr))
    print(result)


if __name__ == '__main__':
    n = int(input())
    m = [int(i) for i in input().split()]
    biggest(n, m)