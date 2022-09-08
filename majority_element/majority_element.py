from typing import List


class Solution:
    """Runtime: 169ms"""
    def majority_element(self, nums: List[int]) -> int:
        x = {i:0 for i in nums}
        for i in nums:
            x[i] += 1
        return max(x, key=x.get)


# class Solution:
#     """Runtime: 168ms"""
#     def majority_element(self, nums: List[int]) -> int:
#         sol = None
#         cnt = 0
#         for i in nums:
#             if cnt == 0:
#                 sol = i
#             cnt += (1 if i == sol else -1)
#         return sol


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.majority_element(nums))