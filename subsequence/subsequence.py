def sub(string1, string2):
    x, y = 0, 0
    while x < len(string1) and y < len(string2):
        if string1[x] == string2[y]:
            x += 1
            y += 1
        else:
            y += 1
    if x == len(string1):
        return True
    return False

  
if __name__ == '__main__':
    x = str(input())
    y = str(input())
    print(sub(x, y))
