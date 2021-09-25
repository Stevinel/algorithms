def factorization(num):
    i = 2
    array = []
    while i * i <= num:
        while num % i == 0:
            array.append(i)
            num = num // i
        i += 1
    if num > 1:
        array.append(num)
    return(((' '.join(str(x) for x in array))))

if __name__ == '__main__':
    num = int(input())
    print(factorization(num))