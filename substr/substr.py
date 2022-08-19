class Solution:
    """Runtime: 40ms"""
    def str_str(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0
        return -1 if needle not in haystack else haystack.find(needle)


# class Solution:
#     """Runtime: 63ms"""
#     def str_str(self, haystack: str, needle: str) -> int:
#         for i in range(0, len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
#         return -1


if __name__ == '__main__':
    haystack, needle = str(input()), str(input())
    s = Solution()
    print(s.str_str(haystack, needle))