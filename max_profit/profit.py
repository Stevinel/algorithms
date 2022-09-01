from typing import List


class Solution:
    """Runtime: 965ms"""
    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        best_price_to_buy = prices[0]

        for price in prices:
            if price < best_price_to_buy:
                best_price_to_buy = price
            elif price > best_price_to_buy:
                profit = price - best_price_to_buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit


# class Solution:
#     """Runtime: 2973ms"""
#     def max_profit(self, prices: List[int]) -> int:
#         if len(prices) <= 1:
#             return 0

#         elif prices[::-1] == sorted(prices):
#             return 0

#         profit = 0
#         while prices:
#             buy = min(prices)
#             index_buy = prices.index(buy)
#             sell = max(prices[index_buy:])
#             if index_buy == len(prices) - 1:
#                 prices = prices[:index_buy]
#             elif profit <= sell - buy:
#                 profit = sell - buy
#                 prices = prices[:index_buy]
#             prices = prices[:index_buy]
#         return profit


if __name__ == '__main__':
    prices = list(map(int, input().split()))
    s = Solution()
    print(s.max_profit(prices))