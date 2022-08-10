class Solution:
    """Runtime: 110 ms"""
    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# class Solution:
#     def is_palindrome(self, x: int) -> bool:
#         """Runtime: 89 ms"""
#         if x < 0 or (x > 0 and x % 10 == 0):
#             return False

#         result = 0
#         while x > result:
#             result = result * 10 + x % 10
#             x = x // 10
#         return x == result or x == result // 10


if __name__ == '__main__':
    x = int(input())
    s = Solution()
    print(s.is_palindrome(x))
