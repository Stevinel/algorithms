from typing import List


class Solution:
    """Runtime: 56ms"""
    def plus_one(self, digits: List[int]) -> List[int]:
        str_digits = "".join(str(number) for number in digits)
        new_number = [int(str_digits) + 1]
        new_number_with_comma = ",".join([str(nubmer) for nubmer in new_number])
        return new_number_with_comma


# class Solution:
#     """Runtime: 64ms"""
#     def plus_one(self, digits: List[int]) -> List[int]:
#         return list(map(int, str(int(''.join(map(str, digits))) + 1)))


if __name__ == '__main__':
    digits = list(map(int, input().split()))
    s = Solution()
    print(s.plus_one(digits))