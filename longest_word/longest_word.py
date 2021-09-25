def longest_word(text_len, text):
    text_list = text.split(' ')
    count = 0
    for elem in text_list:
        if len(elem) > count:
            count = len(elem)
            longest_word = elem
    return f'{longest_word}\n{len(longest_word)}'


if __name__ == "__main__":
    text_len = int(input())
    text = str(input())
    print(longest_word(text_len, text))
