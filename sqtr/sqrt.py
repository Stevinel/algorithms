class Solution:
    """Runtime: 64ms"""
    def my_sqrt(self, x: int) -> int:
        return int(x**(1/2))


# class Solution:
#     """Runtime: 3491ms"""
#     def my_sqrt(self, x: int) -> int:
#         index = 1
#         while index*index <= x:
#             index += 1
#         return index-1


# class Solution:
#     """Runtime: 66"""
#     def my_sqrt(self, x: int) -> int:
#         l, r = 0, x
        
#         while l <=r:
#             mid = (l + r) // 2
#             val = mid * mid
#             if val == x:
#                 return mid
#             if val < x:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return l - 1


if __name__ == '__main__':
    x = int(input())
    s = Solution()
    print(s.my_sqrt(x))