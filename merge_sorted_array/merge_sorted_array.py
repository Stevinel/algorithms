from typing import List


class Solution:
    """Runtime: 49ms"""
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            nums1
        
        elif m == 0:
            nums1[:] = nums2

        else:
            nums1[:] = nums1[:m] + nums2
            nums1[:] = sorted(nums1)


# class Solution:
#     """Runtime: 48ms"""
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """

#         tmp_nums1 = nums1[:m]  # copy the non zero elements of nums1

#         p1 = 0
#         p2 = 0

#         for p in range(n + m):

#             if p2 >= n or (p1 < m and tmp_nums1[p1] <= nums2[p2]):
#                 nums1[p] = tmp_nums1[p1] 
#                 p1 += 1
#             else:
#                 nums1[p] = nums2[p2]
#                 p2 += 1


if __name__ == '__main__':
    nums1, m = list(map(int, input().split())), int(input())
    nums2, n = list(map(int, input().split())), int(input())
    s = Solution()
    print(s.merge(nums1, m, nums2, n))
