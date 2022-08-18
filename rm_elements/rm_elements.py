from typing import List


class Solution:
    """Runtime: 67ms"""
    def remove_element(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
 

# class Solution:
#     """Runtime: 41ms"""
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.remove_element(nums))