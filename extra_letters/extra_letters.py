def find_extra(word, extra_letter):
    for elem in range(len(word)):
        if word[elem] != extra_letter[elem]:
            return extra_letter[elem]
    return extra_letter[-1]


if __name__ == '__main__':
    word = sorted(list(input()))
    extra_letter = sorted(list(input()))
    print(find_extra(word, extra_letter))
