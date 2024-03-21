class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        res = 0
        for p in prices:
            if min < p:
                res += p - min
            min = p
        return res
