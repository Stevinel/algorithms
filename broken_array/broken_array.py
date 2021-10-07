def search_in_a_broken_array(broken_array, desired, left, right):
    mid = (left + right) // 2
    if right < left:
        return -1

    if desired == broken_array[mid]:
        return mid
    
    from_left_to_mid = search_in_a_broken_array(
        broken_array, desired, left, mid - 1
    )
    from_mid_to_right = search_in_a_broken_array(
        broken_array, desired, mid + 1, right
    )

    if broken_array[left] <= broken_array[mid]:
        if broken_array[left] <= desired < broken_array[mid]:
            return from_left_to_mid
        return from_mid_to_right
    elif broken_array[left] > broken_array[mid]:
        if broken_array[mid] < desired <= broken_array[right]:
            return from_mid_to_right
        return from_left_to_mid
    return -1


if __name__ == "__main__":
    lenght = int(input())
    desired = int(input())
    broken_array = [int(i) for i in input().split()]
    print(search_in_a_broken_array(broken_array, desired, 0, lenght - 1))
