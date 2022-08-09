from typing import List


class Solution:
    """First solution. Runtime: 73 ms"""
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            difference = target - num
            if num in hash_map:
                return [hash_map[num], i]
            else:
                hash_map[difference] = i


# class Solution:
#     """Second solution. Runtime: 5421 ms"""
#     def two_sum(self, nums: List[int], target: int) -> List[int]:
#         hash_map = {}
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum == target:
#                     return [i, j] 


if __name__ == '__main__':
    nums, target = list(map(int, input().split())), int(input())
    s = Solution()
    print(s.two_sum(nums, target))



        