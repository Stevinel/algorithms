def generate_ps(n, left, right, result):
    if left + right == 2 * n:
        print(result)
    if left < n:
        generate_ps(n, left + 1, right, result + '(')
    if right < left:
        generate_ps(n, left, right + 1, result + ')')


if __name__ == '__main__':
    n = int(input())
    generate_ps(n, 0, 0, '')
 