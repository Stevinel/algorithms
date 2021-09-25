def cazino(data):
    a, b, c = data
    y = [a, b, c]
    counter = 0
    counter2 = 0
    for elem in y:
        if elem % 2 == 0:
            counter += 1
        elif elem % 2 != 0:
            counter2 += 1
    if counter == 3 or counter2 ==3:
        return("WIN")
    return("FAIL")
    

if __name__ == '__main__':
    data = map(int, input().split())
    print(cazino(data))
