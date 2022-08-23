class Solution:
    """Runtime: 53 ms"""
    def add_binary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a, b = str(input()), str(input())
    s = Solution()
    print(s.add_binary(a, b))