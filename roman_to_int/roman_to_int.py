class Solution:
    """Runtime: 62ms"""
    def roman_to_int(self, s: str) -> int:
        result = 0 
        prevous_number = 0
        roman_nums = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000
        }

        for symbol in s[::-1]:
            if roman_nums[symbol] >= prevous_number:
                result += roman_nums[symbol]
            else:
                result -= roman_nums[symbol]
            prevous_number = roman_nums[symbol]
        return result
        

# class Solution:
#     """Runtime: 54 ms"""
#     def roman_to_int(self, s: str) -> int:
#         roman_nums = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         s = s.replace('IV', 'IIII') \
#             .replace('IX', 'VIIII') \
#             .replace('XL', 'XXXX') \
#             .replace('XC', 'LXXXX') \
#             .replace('CD', 'CCCC') \
#             .replace('CM', 'DCCCC')
#         return sum(map(roman_nums.get, s))


if __name__ == '__main__':
    s = str(input())
    solution = Solution()
    print(solution.roman_to_int(s))


