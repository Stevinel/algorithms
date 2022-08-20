from typing import List


class Solution:
    """Runtime: 57ms"""
    def search_insert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        if len(nums) == 1:
            return nums.index(nums[0]) if target < nums[0] else 1

        for i, num in enumerate(nums):
           if num >= target:
               return i
        return len(nums)


# class Solution:
#     def search_insert(self, nums: List[int], target: int) -> int:
#         return sorted(nums + [target]).index(target)


# class Solution:
#     """Runtime: 52ms"""
#     def search_insert(self, nums: List[int], target: int) -> int:
#         i = 0
#         j = len(nums) - 1
#         while(i <= j):
#             pivot = (i + j) // 2
#             if (nums[pivot] == target):
#                 return pivot
#             elif (nums[pivot] > target):
#                 j = pivot - 1
#             else:
#                 i = pivot + 1
#         return i


if __name__ == '__main__':
    nums, target = list(map(int, input().split())), int(input())
    s = Solution()
    print(s.search_insert(nums, target))