class Solution:
    """Runtime: 53ms"""
    def is_valid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []
        if len(s) % 2: 
            return False

        for b in s:
            if b in brackets:
                stack.append(b)
            elif len(stack) == 0 or brackets[stack.pop()] != b:
                return False
        return len(stack) == 0


# class Solution:
#     """Runtime: 74ms"""
#     def is_valid(self, s: str) -> bool:
#         if len(s) % 2: 
#             return False

#         while len(s) > 0:
#             l = len(s)
#             s = s.replace('()','').replace('{}','').replace('[]','')
#             if l == len(s): return False
#         return True


if __name__ == '__main__':
    brackets = str(input())
    s = Solution()
    print(s.is_valid(brackets))