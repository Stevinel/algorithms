def calculation(data):
    a, x, b, c = data
    return (a * (x ** 2)  + b * x + c)

if __name__ == "__main__":
    data = map(int, input().split())
    print(calculation(data))