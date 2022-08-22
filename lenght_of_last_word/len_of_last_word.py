class Solution:
    """Runtime: 59ms"""
    def length_of_last_word(self, s: str) -> int:
        return len(s.split()[-1])


# class Solution:
#     """Runtime: 53ms"""
#     def length_of_last_word(self, s: str) -> int:
#         count = 0
#         switch = False

#         for char in s[::-1]:
#             if char != ' ':
#                 count += 1
#                 switch = True
#             elif switch:
#                 break
#         return count


if __name__ == '__main__':
    string = str(input())
    s = Solution()
    print(s.length_of_last_word(string))
