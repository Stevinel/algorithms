def sort_bubble(length, array):
    for i in range(length):
        changed = False
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                changed = True

        if changed == False:
            if i == 0:
                print(*array)
            break
        print(*array)


if __name__ == '__main__':
    size = int(input())
    list_number = [int(i) for i in input().split()]
    sort_bubble(size, list_number)