## Maximum Profit
## LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
## Given a list of daily stock prices, calculate the maximum possible
## profit by finding the optimal buy & sell days (remembering that the
## sell day must always be after the buy day).
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        if len(prices) < 2:
            return profit
        bi=0
        si=1

        while si < len(prices):
            curProfit=prices[si]-prices[bi]
            if curProfit <= 0:
                bi=si
            elif curProfit > profit:
                profit=curProfit
            si+=1
        return profit
s=Solution()
print(s.maxProfit([3,2,6,5,0,3]))
