class Solution:
    def convert_to_title(self, column_number: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alph_lenght = 26
        index = column_number - 1

        if index < alph_lenght:
            return alphabet[index]
        else:
            return self.convert_to_title(index // alph_lenght) + alphabet[index % alph_lenght]


if __name__ == '__main__':
    column_number = int(input())
    s = Solution()
    print(s.convert_to_title(column_number))