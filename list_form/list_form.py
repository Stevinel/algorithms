def list_form(number_len, number, another_number):
    number_list = int(''.join(number))
    summma = str(number_list + another_number)
    return ' '.join(summma)


if __name__ == '__main__':
    number_len = int(input())
    number = list(map(str, input().split()))
    another_number = int(input())
    print(list_form(number_len, number, another_number))
