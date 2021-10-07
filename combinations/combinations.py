KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }


def combinations(number, result):
    if len(number) == 1:
        for i in KEYBOARD[number]:
            print(result + i, end=' ')
    elif len(number) > 1:
        for char in KEYBOARD[number[0]]:
            print(number[1:])
            combinations(number[1:], result + char)


if __name__ == '__main__':
    n = str(input())
    combinations(n, '')