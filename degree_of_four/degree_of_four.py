def power_of_four(num):
    if num == 0:
        return False
    while num != 1:
            if num % 4 != 0:
                return False
            num = num // 4
    return True


if __name__ == "__main__":
    num = int(input())
    print(power_of_four(num))
