import re


class Solution:
    """Runtime: 72ms"""
    def is_palindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-zA-Z0-9]', '', s)
        return res.lower() == res.lower()[::-1]


# class Solution:
#     """Runtime: 39ms"""
#     def is_palindrome(self, s: str) -> bool:
#         s = [i for i in s.lower() if i.isalnum()]
#         return s == s[::-1]


if __name__ == '__main__':
    string = str(input())
    s = Solution()
    print(s.is_palindrome(string))