def merge_sort(arr: list, left: int, right: int):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
    moving_to_left = arr[left:mid]
    moving_to_right = arr[mid:right]
    k, i, j = left, 0, 0

    while left + i < mid and mid + j < right:
        if moving_to_left[i] <= moving_to_right[j]:
            arr[k] = moving_to_left[i]
            i = i + 1
        else:
            arr[k] = moving_to_right[j]
            j = j + 1
        k = k + 1
    if left + i < mid:
        while k < right:
            arr[k] = moving_to_left[i]
            i = i + 1
            k = k + 1
    else:
        while k < right:
            arr[k] = moving_to_right[j]
            j = j + 1
            k = k + 1
    return arr


if __name__ == '__main__':
    arr = [0, 3, 4, 5, 1, 2]
    merge_sort(arr, 0, len(arr))
    print(*arr)