from typing import List


class Solution:
    """Runtime: 241ms"""
    def remove_duplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


# class Solution:
#     """Runtime: 163ms"""
#     def remove_duplicates(self, nums: List[int]) -> int:
#         nums[:] = sorted(set(nums))
#         return len(nums)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.remove_duplicates(nums))