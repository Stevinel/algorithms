from typing import List


class Solution:
    """Runtime: 297ms"""
    def single_number(self, nums: List[int]) -> int:
        x = {e: 0 for e in nums}
        for i in nums:
            x[i] += 1
        return list(x.keys())[list(x.values()).index(1)]


# class Solution:
#     """Runtime: 281ms"""
#     def single_number(self, nums: List[int]) -> int:
#         xor_result = 0
#         for x in nums:
#             xor_result ^= x
            
#         return xor_result


# class Solution:
#     """Runtime: 1487ms"""
#     def single_number(self, nums: List[int]) -> int:
#         x = []
#         for i in nums:
#             if i in x:
#                 x.remove(i)
#             else:
#                 x.append(i)
#         return x[0]


# class Solution:
#     """Runtime: 9005ms"""
#     def single_number(self, nums: List[int]) -> int:
#         x = {e: nums.count(e) for i, e in enumerate(nums)}
#         return(list(x.keys())[list(x.values()).index(1)])


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    s = Solution()
    print(s.single_number(nums))