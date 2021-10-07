def counting_sort(arr):
    counted_values = {'0': 0, '1': 0, '2': 0, }
    for value in arr:
        counted_values[value] += 1

    srt = []
    for i in counted_values:
        srt.extend([i] * counted_values[i])

    print(*srt)

if __name__ == '__main__':
    k = int(input())
    cloths = input().split()
    counting_sort(cloths)

# Простой вариант
# k = int(input())
# alist = [int(i) for i in input().split()]
# m = sorted(alist)
# print(*m)