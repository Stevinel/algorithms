from typing import List


class Solution:
    """Runtime: 83ms"""
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs: return ""
        short_word = min(strs, key=len)
        len_short_word = len(short_word)

        for i in strs:
            if i.startswith(short_word):
                continue
            while not i.startswith(short_word[:len_short_word]):
                len_short_word -= 1
        return short_word[:len_short_word] or ""


# class Solution:
#     """Runtime: 64ms"""
#     def longest_common_prefix(self, strs: List[str]) -> str:
#         if not strs: return ""

#         min_word, max_word = min(strs), max(strs)
                
#         for i, letter in enumerate(min_word):
#             if letter != max_word[i]:  
#                 return min_word[:i]
#         return min_word


# class Solution:
#     """Runtime: 57ms"""
#     def longest_common_prefix(self, strs: List[str]) -> str:
#         pre = strs[0]

#         for i in strs:
#             while not i.startswith(pre):
#                 pre = pre[:-1]

#         return pre


if __name__ == '__main__':
    strs = list(map(str, input().split()))
    s = Solution()
    print(s.longest_common_prefix(strs))